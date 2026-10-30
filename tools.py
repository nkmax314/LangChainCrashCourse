from typing import Any, dict

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool
from tavily import TavilyClient

load_dotenv()
tavily_client = TavilyClient()


@tool
def web_search(query: str) -> dict[str, Any]:
    return tavily_client.search(query)


@tool
def print_document(name: str) -> str:
    """use this tool to generate the proper document for your student"""
    return f"this is the document of {name}"


agent = create_agent(
    model="gpt-5-nano",
    tools=[print_document],
    system_prompt=" you are a teacher who want to use your\
                        tools to generate the right document for your students",
)

response = agent.invoke(
    {"messages": [HumanMessage(content="HEllo I am a student and my name is Neeraj")]}
)
print("AI response")
print(response["messages"][-1].content)

print("--------------details -------------------")
print(response["messages"])
