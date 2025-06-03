from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch, RunnableLambda

load_dotenv()

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description="Give the feedback")

model = ChatOpenAI()

parser = PydanticOutputParser(pydantic_object=Feedback)
str_parser = StrOutputParser()

prompt = PromptTemplate(
    template="Classify the sentiment of given feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

classifier_chain = prompt | model | parser

'''
branch = RunnableBranch(
    (condition1, chain1),
    (condition2, chain2),
    .
    .
    .  
    default chain
)
'''

prompt2 = PromptTemplate(
    template="Give appropriate response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Give appropriate  response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | str_parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | str_parser),
    RunnableLambda(lambda x: "No sentiment found.")
)

chain = classifier_chain |branch_chain
feedback = "This is the worst product ever"
result = chain.invoke({"feedback": feedback})

print(result)
chain.get_graph().print_ascii()