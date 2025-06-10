from fastapi import FastAPI
from pydantic import BaseModel
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.chains.llm_math.base import LLMMathChain
from langchain.memory import ConversationBufferMemory
import os

app = FastAPI()

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

search = DuckDuckGoSearchRun()
llm_math = LLMMathChain(llm=llm)

tools = [
    Tool(name="Search", func=search.run, description="Websuche"),
    Tool(name="Calculator", func=llm_math.run, description="Berechnungen")
]

# NEU: Memory hinzufügen
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Agent mit Memory
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str

@app.post("/ask", response_model=AskResponse)
def ask_agent(req: AskRequest):
    response = agent.run(req.question)
    return AskResponse(answer=response)

