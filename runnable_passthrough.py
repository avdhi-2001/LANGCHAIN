from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt1= PromptTemplate(
    template='Generate a joke on the {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='generate explanation for the joke - {text}',
    input_variables=['text']
)


joke_gen_chain=RunnableSequence(prompt1, model, parser)

chain=RunnableParallel({
    'explanation': RunnableSequence(prompt2, model, parser),
    'joke': RunnablePassthrough()

})

final_chain=RunnableSequence(joke_gen_chain, chain)

result=final_chain.invoke({'topic':'AI'})

print(result)