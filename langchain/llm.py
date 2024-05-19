from langchain_openai import ChatOpenAI
import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

llm = ChatOpenAI(temperature=0.1, api_key=OPENAI_API_KEY, verbose=True)
response = llm.invoke("are people going to movie theatre or watch in TV")

print(response)