from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name:str
    age:int
    final:str

def first_node(stage:AgentState)->AgentState:
    stage["final"] = stage["name"] + ", you are " + str(stage["age"])
    return stage

def second_node(stage:AgentState)->AgentState:
    stage["final"] = stage["final"] + " years old"
    return stage

graph=StateGraph(AgentState)
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.set_finish_point("second_node")
app=graph.compile()
result=app.invoke({"name":"Varuuu!!!", "age":20})
print(result["final"])