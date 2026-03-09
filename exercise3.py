from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name:str
    age:int
    skills:List[str]
    final: str

def first_node(state:AgentState)->AgentState:
    state["final"] = "Hey " + state["name"] + "! You are awesome."
    return state

def second_node(state:AgentState)->AgentState:
    state["final"] = state["final"] + " You are " + str(state["age"]) + " years old."
    return state

def third_node(state:AgentState)->AgentState:
    state["final"] = state["final"] + " You are good at : " + ", ".join(state["skills"]) + "!"
    return state

graph=StateGraph(AgentState)
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.add_node("third_node", third_node)
graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.add_edge("second_node", "third_node")
graph.set_finish_point("third_node")
app=graph.compile()
result=app.invoke({"name":"Varuuu!!!", "age":20, "skills":["python", "machine learning", "deep learning"]})
print(result["final"])

