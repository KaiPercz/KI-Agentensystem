from langchain_community.llms import OpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.chains.llm_math.base import LLMMathChain

llm = OpenAI(temperature=0)
search = DuckDuckGoSearchRun()
llm_math = LLMMathChain(llm=llm)

tools = [
    Tool(name="Search", func=search.run, description="Nutze das Internet"),
    Tool(name="Rechne", func=llm_math.run, description="Führe komplexe Berechnungen durch"),
]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

