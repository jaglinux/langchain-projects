import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_community.tools.tavily_search import TavilySearchResults

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
TAVILY_API_KEY = os.environ['TAVILY_API_KEY']

llm = ChatOpenAI(temperature=0.1)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
print(prompt.messages)

search_tool = TavilySearchResults(max_results=1)
tools = [search_tool]
 
agent = create_openai_functions_agent(llm=llm, prompt=prompt, tools=tools)
agentExecutor = AgentExecutor(agent=agent, tools=tools, verbose=True)

response = agentExecutor.invoke({
    "input": "what is the current weather in San Ramon in California"
    }
)

print(response)