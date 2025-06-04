from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="11.DocumentLoaders/Directory",
    glob="*.pdf",
    loader_cls=PyPDFLoader     # type: ignore
) 

doc = loader.load()
print(doc)

print("------"*10)

print(len(doc))