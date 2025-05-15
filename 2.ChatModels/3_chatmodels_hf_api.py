from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    max_new_tokens=10
)

model = ChatHuggingFace(llm=llm, verbose=True)

result = model.invoke("What is the capital of India?")

print(result.content)