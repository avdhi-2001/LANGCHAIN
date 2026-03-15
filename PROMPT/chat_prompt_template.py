from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage

chat_template=ChatPromptTemplate(
    ('system','you are a helpful customer support agent'),
    #it will take the chat history and put it in the prompt,basically it is used to retrieve the chat history and put it in the prompt,so that the model can use it to generate the response
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')

)

chat_history=[]
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)

prompt=chat_template.invoke({'chat_history': chat_history,'query':'what is the capital of India?'})

print(prompt)