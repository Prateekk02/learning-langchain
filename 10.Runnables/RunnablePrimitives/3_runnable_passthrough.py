from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template="Explain the joke on {topic}",
    input_variables=['topic']
)

joke_chain = prompt1 | model | parser
explainer_chain = prompt2 | model | parser

parallel_chain = RunnableParallel({
    'explainer': explainer_chain,
    'joke': RunnablePassthrough()
})

final_chain = joke_chain | parallel_chain

result = final_chain.invoke({"topic":"Anakin"})
print(result['explainer'])
print("--"*50)
print(result['joke'])