from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# Define the model
model=ChatOpenAI()


template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='Write a 5 pointer summary on the following text. /n {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':'black holes'})

chain.get_graph().print_ascii()

print(result)

