from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4",temperature=0.9,max_completion_tokens=10)

result=model.invoke("what is the capital of India?")

print(result.content)

# from langchain_anthropic import ChatAnthropic

# from dotenv import load_dotenv

# load_dotenv()

# model=ChatAnthropic(model="gpt-4",temperature=0.9,max_completion_tokens=10)

# result=model.invoke("what is the capital of India?")

# print(result.content)
