from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

url = "https://rocm.docs.amd.com/en/latest/what-is-rocm.html"

loader = WebBaseLoader(url)
docs = loader.load()

llm = ChatOpenAI(temperature=0.1)
prompt = ChatPromptTemplate.from_template("""
    Answer the user's question:
    Context: {context}
    Question : {input}
    """)

chain = prompt | llm

response = chain.invoke({
    "context" : [docs],
    "input" : "how many compilers and runtime, list them"
})

print(response)
