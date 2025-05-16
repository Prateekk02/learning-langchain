from langchain_core.prompts import ChatPromptTemplate



chat_template = ChatPromptTemplate([
    ("system","You are a helpful {domain} expert"),
    ("human", "In simple term explain about {topic}")
])

prompt = chat_template.invoke({
    'domain': 'star wars',
    'topic' : 'The elders'
})

print(prompt)