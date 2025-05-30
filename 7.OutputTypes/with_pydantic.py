from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()


review = ""

with open("7.OutputTypes/complex_review.txt") as f:
    review = f.read()


# Schema
class Review(BaseModel):
    
    key_themes: list[str] = Field(description= "Write down all the key themes discussed in the review in a list." )
    summary: str = Field(description="A brief summary of the review.")
    sentiment: Literal["pos", "neg"] = Field(description= "Return sentiment of the review either negative or negative")
    pros: Optional[list[str]] = Field(description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(description="Write down all the cons inside a list")
    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(review)

print(type(result))