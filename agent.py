from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.chains.llm_math.base import LLMMathChain

def build_agent():
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    tools = [Tool.from_function(func=LLMMathChain(llm=llm).run, name="Calculator", description="Useful for math")]
    
    agent = initialize_agent(
        tools,
        llm,
        agent="chat-conversational-react-description",
        verbose=True
    )
    return agent
