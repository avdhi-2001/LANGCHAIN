from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

# Define the model
model=ChatOpenAI()

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt=18, description="The age of the person")
    city: str = Field(description="The city in which the person lives")   

parser = PydanticOutputParser(pydantic_object=Person)

prompt= PromptTemplate(
    template="generate the name, age and city of a {place} cricketer \n {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# chain= prompt | model | parser

# final=chain.invoke({'place':'indian'})

template=prompt.invoke({'place': 'indian'})

final=model.invoke(template)

print(final)
