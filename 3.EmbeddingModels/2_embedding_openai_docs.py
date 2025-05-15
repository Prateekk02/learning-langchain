from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

docs = [
    "Order 66 was executed by Darth Vader",
    "Anakin was the choosen one.",
    "Senator Palpatine is Darth Sedious"
]
result = embedding.embed_documents(docs)

print(str(result))

 