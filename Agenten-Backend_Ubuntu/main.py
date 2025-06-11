import os
import json
from uuid import uuid4
from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chains import LLMMathChain
from langchain.tools import DuckDuckGoSearchRun
from langchain.memory import ConversationBufferMemory

# 📁 Speicherverzeichnis für Sessions
SESSION_DIR = "sessions"
os.makedirs(SESSION_DIR, exist_ok=True)

# 📦 FastAPI App
app = FastAPI()

# 🧠 Tools initialisieren
llm = OpenAI(temperature=0)
search = DuckDuckGoSearchRun()
llm_math = LLMMathChain(llm=llm, verbose=False)

tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="Nützlich für Web-Recherchen"
    ),
    Tool(
        name="Rechner",
        func=llm_math.run,
        description="Für mathematische Berechnungen"
    )
]

# 🧾 Session-Modell
class AskRequest(BaseModel):
    question: str
    session_id: str | None = None

# 🧠 Agenten-Speicher pro Sitzung
agent_sessions = {}

# 🔁 Lade gespeicherte Verläufe (falls vorhanden)
def load_or_create_agent(session_id: str):
    if session_id in agent_sessions:
        return agent_sessions[session_id]

    memory = ConversationBufferMemory(memory_key="chat_history")
    session_file = os.path.join(SESSION_DIR, f"{session_id}.json")

    # Verlauf wiederherstellen
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            data = json.load(f)
            for m in data.get("memory", []):
                memory.chat_memory.add_user_message(m["user"])
                memory.chat_memory.add_ai_message(m["ai"])

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=False
    )

    agent_sessions[session_id] = agent
    return agent

# 💾 Speicherfunktion
def save_session(session_id: str):
    agent = agent_sessions.get(session_id)
    if not agent:
        return

    history = agent.memory.chat_memory.messages
    memory_dump = []
    for i in range(0, len(history), 2):
        user_msg = history[i].content if i < len(history) else ""
        ai_msg = history[i+1].content if i+1 < len(history) else ""
        memory_dump.append({"user": user_msg, "ai": ai_msg})

    with open(os.path.join(SESSION_DIR, f"{session_id}.json"), "w") as f:
        json.dump({"memory": memory_dump}, f, indent=2)

# 🚦 API Endpoint
@app.post("/ask")
async def ask(request: AskRequest):
    session_id = request.session_id or str(uuid4())
    agent = load_or_create_agent(session_id)
    response = agent.run(request.question)
    save_session(session_id)
    return {"session_id": session_id, "response": response}

# ❤️‍🔥 Root-Test
@app.get("/")
def root():
    return {"message": "Agenten-Backend läuft."}
