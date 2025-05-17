from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Create chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# Load chat history
chat_history = []
with open("6.ConsoleChatbotApplication/chat_history.txt") as f:
    chat_history.extend(f.readlines())

# Create Prompt
prompt = chat_template.invoke({"chat_history": chat_history, "query": "Where is my refund?"})

print(prompt)
