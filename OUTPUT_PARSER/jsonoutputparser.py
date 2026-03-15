from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

load_dotenv()


model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
    template='give name, age and city of indian cricketer \n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)
# partial variable is not sent at runtime(nor send by the user) but is used to format the prompt template. It is a way to include additional information in the prompt without having to pass it as an input variable at runtime.
#flaw about json output parser is that i does'nt support schema enforce that means i decides its own schema we can customise it
# template.format() is used to format the prompt template with the provided input variables and partial variables. It replaces the placeholders in the template with the corresponding values from the input variables and partial variables.
# prompt = template.format()

# result = model.invoke(prompt)

# final = parser.parse(result.content)

chain = template | model | parser

result = chain.invoke({})

print(result)
