
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt1= PromptTemplate(
    template='Generate a joke on the {topic}',
    input_variables=['topic']
)

def count_words(topic):
    return len(topic.split())

chain=RunnableSequence(prompt1, model, parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'count_words': RunnableLambda (count_words)
})

final_chain=RunnableSequence(chain,parallel_chain)

result=final_chain.invoke({'topic':"Scientist"})

print(result['count_words'])