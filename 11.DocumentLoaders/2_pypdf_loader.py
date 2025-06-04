from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("11.DocumentLoaders/React01.pdf")

doc = loader.load()

print(doc[0].page_content)
print("--"* 50)
print(doc[1].metadata)