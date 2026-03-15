from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI()

template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='write a 5 line summary on the following text /n {text}',
    input_variables=['text']
)

prompt1=template1.invoke({'topic':"openai"})
result1=model.invoke(prompt1)

prompt2=template2.invoke({'text':result1.content})
result2=model.invoke(prompt2)

print(result1.content)