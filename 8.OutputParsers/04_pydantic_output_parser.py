from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class User(BaseModel):
    name: str = Field(description="Name of the person.")
    age: int = Field(gt=18, description="Age of the person.")
    city: str = Field(description="City where the person belong to.")
    
parser = PydanticOutputParser(pydantic_object=User)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional character in {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({"topic": "Star Wars"})

print(result)
