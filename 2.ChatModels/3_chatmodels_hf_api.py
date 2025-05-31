from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    max_new_tokens=10
)

model = ChatHuggingFace(llm=llm, verbose=True)

result = model.invoke("What is the capital of India?")

print(result.content)
# print(result)