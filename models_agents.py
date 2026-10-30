from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import AIMessage, HumanMessage

load_dotenv()

model = init_chat_model(model="gpt-5-nano", temperature=1.0)

agent = create_agent(model=model)

for token, metadata in agent.stream(
    {
        "messages": [
            HumanMessage("what is the capital of italy. "),
            AIMessage("Rome (Italian: Roma)."),
            HumanMessage("Give me more about it."),
        ]
    },
    stream_mode="messages",
):
    if token.content:
        print(token.content, end="", flush=True)

# response = agent.invoke(
#     {
#         "messages": [
#             HumanMessage("what is the capital of italy. "),
#             AIMessage("Rome (Italian: Roma)."),
#             HumanMessage("Give me more about it."),
#         ]
#     }
#     )

# print(response["messages"][-1].content)
