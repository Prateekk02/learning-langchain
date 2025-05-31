from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age, and city of a fictional character \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser 
result = chain.invoke({})
print(result)