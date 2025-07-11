from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

template = PromptTemplate(
    template='Generate 5 lines of given {topic} ',
    input_variables=['topic']    
)

model = ChatOpenAI()
parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({'topic': 'Andor - Star Wars'}) 

print(result)
chain.get_graph().print_ascii()