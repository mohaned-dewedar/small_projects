from dotenv import load_dotenv
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferWindowMemory
from langchain.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from langchain.schema.messages import SystemMessage
from langchain.agents import AgentExecutor
from tools import RankCountriesTool , PlotScatterTool , PlotPairPlotTool , PlotContinentTool
from langchain.callbacks import StreamlitCallbackHandler

load_dotenv()

@st.cache_resource()
def setup_once():
    llm = ChatOpenAI(temperature=0,streaming=True)
    memory = ConversationBufferWindowMemory(memory_key="memory", return_messages=True, output_key="output",k=3)
    system_message = SystemMessage(content=(f"You are an agent helping users answer questions about the World Happiness Report.Your job is to only choose which tool and use that context, dont answer with your knowledge"))
    tools = [RankCountriesTool(),PlotScatterTool(),PlotPairPlotTool(),PlotContinentTool()]
    prompt = OpenAIFunctionsAgent.create_prompt(
                system_message=system_message,
                extra_prompt_messages=[MessagesPlaceholder(variable_name="memory")]
            )
        
    agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent,memory=memory,tools=tools)

    return agent_executor

def ask(agent):
    if prompt := st.chat_input():
        st.chat_message("user").write(prompt)
        with st.chat_message("assistant"):
            st_callback = StreamlitCallbackHandler(st.container())
            response = agent.run(prompt, callbacks=[st_callback])
            st.write(response)

agent = setup_once()
st.title("World Happiness Report")
st.write("This is a tool to help you answer questions about the World Happiness Report")

ask(agent)
