from typing import TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    name:str

def compliment_user(state:AgentState)->AgentState:
    state['name'] = state['name'] + ", you are learning AgentAI"
    return state

graph=StateGraph(AgentState)

graph.add_node("compliment_user", compliment_user)

graph.set_entry_point("compliment_user")
graph.set_finish_point("compliment_user")

app=graph.compile()
result = app.invoke({"name":"Varuuu!!!"})

print(result["name"])
