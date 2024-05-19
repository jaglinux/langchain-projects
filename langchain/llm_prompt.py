from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

llm = ChatOpenAI(temperature=0.1)
prompt = ChatPromptTemplate.from_messages([
    ("system", "Generate joke"),
    ("human", "{inputs}")
])

chain = prompt | llm  

response = chain.invoke("dog")

print(response)