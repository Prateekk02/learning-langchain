from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI()


review = ""

with open("7.OutputTypes/simple_review.txt") as f:
    review = f.read()


# Schema
class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review."]
    sentiment: Annotated[str, "Return sentiment of the review either negative, positive or neutral"]
    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke(review)

print(result)