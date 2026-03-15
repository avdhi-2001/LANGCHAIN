from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model=ChatOpenAI()

parser= StrOutputParser()

loader=PyPDFLoader('dl-curriculum.pdf')

docs= loader.load()

print(docs[0])

print(docs[0].page_content)

print(len(docs))

print(docs[0].metadata)

# it does'nt work well when we have scanned images in pdf
