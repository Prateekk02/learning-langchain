from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()   

url = "https://www.flipkart.com/apple-iphone-16-black-256-gb/p/itm86da1977dcdf1?pid=MOBH4DQFZCJJXUFG&lid=LSTMOBH4DQFZCJJXUFGO5DY3W&marketplace=FLIPKART&q=apple+mobiles&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&fm=organic&iid=2b25b0b4-15c9-4dff-a7b1-4802f074e523.MOBH4DQFZCJJXUFG.SEARCH&ppt=clp&ppn=laptops-store&ssid=o5fv37jqcg0000001749046254804&qH=cb603b9543d774e1"

loader = WebBaseLoader(url)
doc = loader.load()
model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Answer the {question} from the {doc}", 
    input_variables=['question', 'doc'] 
) 

chain = prompt | model | parser

result = chain.invoke({
    "question": "What are the best features of this mobile",
    "doc": doc[0].page_content
}) 

print(result)

