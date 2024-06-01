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

# [SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], template='You are a friendly assistant')), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], template='{input}')), MessagesPlaceholder(variable_name='agent_scratchpad')]


# > Entering new AgentExecutor chain...

# Invoking: `tavily_search_results_json` with `{'query': 'current weather in San Ramon California'}`


# [{'url': 'https://www.weatherapi.com/', 'content': "{'location': {'name': 'San Ramon', 'region': 'California', 'country': 'United States of America', 'lat': 37.78, 'lon': -121.98, 'tz_id': 'America/Los_Angeles', 'localtime_epoch': 1717230684, 'localtime': '2024-06-01 1:31'}, 'current': {'last_updated_epoch': 1717230600, 'last_updated': '2024-06-01 01:30', 'temp_c': 12.2, 'temp_f': 54.0, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 8.1, 'wind_kph': 13.0, 'wind_degree': 320, 'wind_dir': 'NW', 'pressure_mb': 1011.0, 'pressure_in': 29.86, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 80, 'cloud': 0, 'feelslike_c': 11.3, 'feelslike_f': 52.3, 'windchill_c': 9.0, 'windchill_f': 48.2, 'heatindex_c': 10.3, 'heatindex_f': 50.5, 'dewpoint_c': 7.5, 'dewpoint_f': 45.4, 'vis_km': 11.0, 'vis_miles': 6.0, 'uv': 1.0, 'gust_mph': 11.5, 'gust_kph': 18.5}}"}]The current weather in San Ramon, California is as follows:
# - Temperature: 12.2°C (54.0°F)
# - Condition: Clear
# - Wind: 13.0 km/h from the NW
# - Pressure: 1011.0 mb
# - Humidity: 80%
# - Visibility: 11.0 km
# - UV Index: 1.0

# It is currently nighttime in San Ramon.

# > Finished chain.
# {'input': 'what is the current weather in San Ramon in California', 'output': 'The current weather in San Ramon, California is as follows:\n- Temperature: 12.2°C (54.0°F)\n- Condition: Clear\n- Wind: 13.0 km/h from the NW\n- Pressure: 1011.0 mb\n- Humidity: 80%\n- Visibility: 11.0 km\n- UV Index: 1.0\n\nIt is currently nighttime in San Ramon.'}
