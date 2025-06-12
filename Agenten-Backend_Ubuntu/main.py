from fastapi import FastAPI, Request
from pydantic import BaseModel
from uuid import UUID
import os
import json
from typing import Dict

from langchain_community.llms import OpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.chains.llm_math.base import LLMMathChain

# 🔁 Ab LangChain v0.1.13 muss langchain_community genutzt werden
from langchain_community.llms import OpenAI as CommunityOpenAI
from langchain_community.tools import DuckDuckGoSearchRun as CommunitySearch

app = FastAPI()

# 🧠 In-Memory-Verwaltung aller Sessions
sessions: Dict[str, Dict] = {}

# 📁 Session-Dateien speichern in diesem Ordner
SESSION_DIR = "sessions"
os.makedirs(SESSION_DIR, exist_ok=True)

# 🔑 OpenAI-Key aus ENV holen (ggf. .env nutzen)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class AskRequest(BaseModel):
    question: str
    session_id: str  # UUID in String-Form

def create_agent(session_id: str):
    # Tools und LLM initialisieren
    search = CommunitySearch()
    llm = CommunityOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="Search engine for current information."
        ),
        Tool(
            name="Calculator",
            func=LLMMathChain(llm=llm).run,
            description="Useful for mathematical calculations."
        )
    ]

    memory = ConversationBufferMemory(memory_key="chat_history")

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=False
    )

    return {"agent": agent, "memory": memory}

def save_session(session_id: str):
    session_data = sessions[session_id]
    memory = session_data["memory"]
    filepath = os.path.join(SESSION_DIR, f"{session_id}.json")
    with open(filepath, "w") as f:
        json.dump(memory.chat_memory.messages, f, default=str, indent=2)

def load_session(session_id: str):
    filepath = os.path.join(SESSION_DIR, f"{session_id}.json")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            messages = json.load(f)
        return messages
    return []

@app.post("/ask")
def ask(request: AskRequest):
    session_id = request.session_id

    if session_id not in sessions:
        sessions[session_id] = create_agent(session_id)

    agent = sessions[session_id]["agent"]

    try:
        answer = agent.run(input=request.question)
        save_session(session_id)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
