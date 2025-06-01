from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="Give a detailed report about {topic}",
    input_variables=['topic']    
)
prompt2 = PromptTemplate(
    template="Give a 5 pointer summary of {topic}",
    input_variables=['topic']
) 

parser = StrOutputParser()


chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "A Study in Scarlet"})

print(result)

chain.get_graph().print_ascii()