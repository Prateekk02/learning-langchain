from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()


review = ""

with open("7.OutputTypes/complex_review.txt") as f:
    review = f.read()


# Schema
class Review(TypedDict):
    key_themes : Annotated[list[str], "Write down all the key themes discussed in the review in a list."]
    summary: Annotated[str, "A brief summary of the review."]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative or negative"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(review)

print(result)