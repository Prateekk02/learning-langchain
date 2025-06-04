from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda, RunnableBranch
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

class Category(BaseModel):
    category : Literal['complain', 'refund', 'general']  = Field(description="Classify the category")  
    
pydantic_parser = PydanticOutputParser(pydantic_object=Category)
    
model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Classify the {Email} in one of the category 'complain', 'refund', 'general' \n {format_instruction}",
    input_variables=['Email'],
    partial_variables={'format_instruction': pydantic_parser.get_format_instructions()}
)

category_chain = prompt | model | pydantic_parser

complain_prompt = PromptTemplate(
    template="Respond to the {Email} according to the complain.",
    input_variables=['Email']
)
refund_prompt = PromptTemplate(
    template="Respond to the {Email} for refund.",
    input_variables=['Email']
)
general_prompt = PromptTemplate(
    template="Respond for the query asked in the {Email} ",
    input_variables=['Email']
)

# branch = RunnableBranch(
#     (lambda x : x['category'] == 'complain', complain_prompt | model | parser),
#     (lambda x : x['category'] == 'refund', refund_prompt | model | parser),
#     (lambda x : x['category'] == 'general', general_prompt | model | parser),
#     RunnableLambda(lambda x: 'Category cannot be specified.')
# )
branch = RunnableBranch(
    (lambda x : x.category == 'complain', complain_prompt | model | parser),
    (lambda x : x.category == 'refund', refund_prompt | model | parser),
    (lambda x : x.category == 'general', general_prompt | model | parser),
    RunnableLambda(lambda x: 'Category cannot be specified.')
)

final_chain = category_chain | branch

refund_email = '''
Dear Customer Support Team,

I hope this message finds you well. I recently purchased a Lightsaber (Order #LSB-47291) from your online store, but unfortunately, the product does not meet my expectations.

Upon unboxing, I noticed that the blade does not light up consistently and the hilt has minor scratches. Given these issues, I would like to request a full refund in accordance with your return policy.

Please advise me on the return process and any additional steps I need to take. I look forward to resolving this matter quickly.

Best regards


'''

complain_email = '''
Subject: Product Complaint – Defective Lightsaber Received

Dear Support Team,

I'm writing to express my disappointment regarding a recent purchase from your store. The Lightsaber I received not only arrived later than expected, but the sound effects are completely non-functional, and the activation button is unresponsive.

Given the premium pricing and reputation of your products, this experience is frustrating. I expect higher quality control for something marketed as a collector's item.

I would appreciate immediate assistance in either replacing the item or escalating this issue to your quality assurance team.

Sincerely
'''

general_email = '''
Subject: Question About My New Lightsaber – Order #LSB-47412

Hi there,

I recently received my Lightsaber (Order #LSB-47412), and it's absolutely amazing! However, I had a few general questions about its features.

Can the blade color be changed manually?

Is there a way to recharge the battery without removing it from the hilt?

Do you offer any accessories like stands or display cases?

Looking forward to your response and any tips you can share on maintaining the saber.

Best regards
'''

refund_result = final_chain.invoke({"Email": refund_email})
complain_result = final_chain.invoke({"Email": complain_email})
general_result = final_chain.invoke({"Email": general_email})

print(refund_result)
print("*"*100) 
print(complain_result)
print("*"*100) 
print(general_result)


