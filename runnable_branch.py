# It is basically the if else statement to langchain

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt1= PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='summarize the following text \n {text}',
    input_variables=['text']
)


report_genration_sequence=RunnableSequence(prompt1, model, parser)

def count_words(topic):
    return len(topic.split())

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(prompt2, model, parser) ),
    RunnablePassthrough()
)

final_chain= RunnableSequence(report_genration_sequence,branch_chain)

print(final_chain.invoke({"topic":"Russia vs Ukraine"}))

