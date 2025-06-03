from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough

load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a funny joke on {topic}",
    input_variables=['topic']
)

joke_chain = prompt | model | parser

def word_count(paragraph: str) -> int:
    words = paragraph.strip().split()
    return (len(words)) 

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = joke_chain | parallel_chain

result = final_chain.invoke({"topic":"Star Wars"})

print(result['joke'])
print("__" * 50)
print(result['word_count'])