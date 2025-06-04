from  langchain_community.document_loaders import TextLoader

loader = TextLoader("11.DocumentLoaders/starwar.txt", encoding='utf-8')

doc = loader.load()
print(doc)