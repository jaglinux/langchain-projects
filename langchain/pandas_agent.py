from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

import pandas as pd
import os
import numpy as np

df = pd.read_csv("./langchain/titanic.csv")
df['Age'] = df['Age'].fillna(int(df['Age'].mean()))
df['Age'] = df['Age'].apply(np.ceil).astype(int)

agent = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

agent.invoke("caculate minimum age")

# > Entering new AgentExecutor chain...
# Invoking: `python_repl_ast` with `{'query': "df['Age'].min()"}`
# 1The minimum age in the dataframe is 1.
# > Finished chain.