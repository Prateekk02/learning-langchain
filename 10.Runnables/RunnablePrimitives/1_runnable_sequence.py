from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()
prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Make the {topic} a serious conversation",
    input_variables=['topic']
) 
chain1 = prompt1 | model | parser
chain2 = prompt2 | model | parser

print(chain1.invoke({"topic": "Anakin didn't had high ground."}))
chain = RunnableSequence(chain1, chain2)

result = chain.invoke({"topic": "Anakin"})
print('*'* 50)
print(result)
  
 