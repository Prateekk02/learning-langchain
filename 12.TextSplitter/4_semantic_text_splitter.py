from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
splitter = SemanticChunker(
    OpenAIEmbeddings(), 
    breakpoint_threshold_type='standard_deviation',
    breakpoint_threshold_amount=0.5
) 

text='''
The global economy is undergoing a rapid transformation driven by advancements in artificial 
intelligence and automation. At the same time, environmental activists are raising concerns 
about the accelerating loss of biodiversity due to deforestation and climate change, urging 
policymakers to take immediate action.

Meanwhile, in the realm of neuroscience, researchers have made a breakthrough in understanding 
how short-term memories are encoded and retrieved in the human brain. This discovery could pave 
the way for new treatments for cognitive disorders like Alzheimer’s and enhance brain-computer
interface technologies.
'''

doc = splitter.create_documents([text])
print(len(doc))
print("**"*50)
print(doc)