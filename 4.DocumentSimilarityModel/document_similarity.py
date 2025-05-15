from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np    

load_dotenv()

document = [
    "Yoda speaks in a unique object-subject-verb syntax, setting him apart linguistically in the galaxy.",
    "The Millennium Falcon famously made the Kessel Run in less than twelve parsecs, showcasing its speed and Han Solo's piloting skills.",
    "Darth Vader began his journey as Anakin Skywalker, a heroic Jedi Knight before turning to the dark side.",
    "Chewbacca's iconic voice is a creative blend of bear, walrus, lion, badger, and other animal sounds.",
    "Stormtroopers' armor design was inspired by the earlier Clone Troopers who fought for the Galactic Republic."
]

query = "Kessel Run parsecs"

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

doc_embedding = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted((list(enumerate(scores))), key=lambda x: x[1]) [-1]


print(f"User: {query}")
print(f"AI: {document[index]}") 
