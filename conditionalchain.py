from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# Define the model
model1=ChatOpenAI()

parser1=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description=' Give the sentiment of the feedback')

parser2=PydanticOutputParser(pydantic_object=Feedback)

template1=PromptTemplate(
    template='classify the following feedback into positive, negative. /n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

classification_chain= template1 | model1 | parser2

result=classification_chain.invoke({'feedback':'I love this product!'}).sentiment

prompt2=PromptTemplate(
    template='Write a response to the positive feedback: {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='Write a response to the negative feedback: {feedback}',
    input_variables=['feedback']
)


branch_chain=RunnableBranch(
    # the runnable function we enter two values one is condition and other is chain
    (lambda x:x.sentiment=='positive', prompt2 | model1 | parser1),
    (lambda x:x.sentiment=='negative', prompt3 | model1 | parser1),
    RunnableLambda(lambda x: "could not find the sentiment of the feedback")
)

chain=classification_chain | branch_chain

print(chain.invoke({'feedback':'I love this product!'}))