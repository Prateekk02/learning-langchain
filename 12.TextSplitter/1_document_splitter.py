from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("11.DocumentLoaders/React01.pdf")

doc = loader.load()
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
) 
result = splitter.split_documents(doc)
print(result)