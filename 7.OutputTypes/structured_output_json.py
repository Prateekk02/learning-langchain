from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOpenAI()
review = ""

with open("7.OutputTypes/complex_review.txt") as f:
    review = f.read()
    
#Json Schema is defined here just like json_schema.json file.

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(review)

print(type(result))