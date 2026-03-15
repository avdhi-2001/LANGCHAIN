from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model=ChatOpenAI()

loader=CSVLoader(file_path='Social_Network_Ads (1).csv')

docs=loader.load()

print(len(docs))

print(docs[0])

print(docs[1].page_content)