from langchain_community.document_loaders import CSVLoader

path = ""
loader = CSVLoader(file_path= path)

doc = loader.load()
print(doc[0]) 
