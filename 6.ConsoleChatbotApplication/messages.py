from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a comic book nerd who has vast knowledge regarding Star wars"),
    HumanMessage(content="Tell me about relation between Grand Admiral Thrawn with Darth Vader and who defeated him at the end?")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))



print(messages)