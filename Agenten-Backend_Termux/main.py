from fastapi import FastAPI, Request
from pydantic import BaseModel
from uuid import uuid4
import os, json
from typing import Dict
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.utilities import DuckDuckGoSearchAPIWrapper
from langchain.tools import DuckDuckGoSearchRun, LLMMathChain
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Datenmodell für Anfragen
class AskRequest(BaseModel):
    question: str
    session_id: str = None

# globale Sitzungsstruktur
SESSIONS: Dict[str, dict] = {}
SESSION_DIR = "sessions"
os.makedirs(SESSION_DIR, exist_ok=True)

# LLM- und Tools-Konfiguration
def create_agent(session_id: str):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    search = DuckDuckGoSearchRun(api_wrapper=DuckDuckGoSearchAPIWrapper())
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="Suche nach aktuellen Informationen."
        ),
        Tool(
            name="Calculator",
            func=LLMMathChain(llm=llm).run,
            description="Führe mathematische Berechnungen durch."
        )
    ]
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return initialize_agent(
        tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory
    )

def load_session(session_id: str):
    path = os.path.join(SESSION_DIR, f"{session_id}.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {"chat_history": []}

def save_session(session_id: str, memory):
    path = os.path.join(SESSION_DIR, f"{session_id}.json")
    messages = memory.buffer_as_messages if hasattr(memory, 'buffer_as_messages') else []
    json.dump(
        {"chat_history": [
            {"type": m.type, "content": m.content} for m in messages
        ]}, open(path, "w"), indent=2
    )

@app.post("/ask")
async def ask(request: AskRequest):
    session_id = request.session_id or str(uuid4())
    if session_id not in SESSIONS:
        agent = create_agent(session_id)
        # Sessionzustand laden
        memory_data = load_session(session_id)
        for msg in memory_data.get("chat_history", []):
            if msg["type"] == "human":
                agent.memory.chat_memory.add_user_message(msg["content"])
            elif msg["type"] == "ai":
                agent.memory.chat_memory.add_ai_message(msg["content"])
        SESSIONS[session_id] = agent
    else:
        agent = SESSIONS[session_id]

    response = agent.run(request.question)
    save_session(session_id, agent.memory)
    return {"session_id": session_id, "answer": response}
