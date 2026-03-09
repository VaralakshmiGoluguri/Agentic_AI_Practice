from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    number1:int
    number2:int
    number3:int
    number4:int
    operation1:str
    operation2:str
    final1:int
    final2:int

def add_node1(state:AgentState)->AgentState:
    state["final1"] = state["number1"] + state["number2"]
    return state

def subtract_node1(state:AgentState)->AgentState:
    state["final1"] = state["number1"] - state["number2"]
    return state

def add_node2(state:AgentState)->AgentState:
    state["final2"] = state["number3"] + state["number4"]
    return state

def subtract_node2(state:AgentState)->AgentState:
    state["final2"] = state["number3"] - state["number4"]
    return state

def router1(state:AgentState)->str:
    if state["operation1"] == "+":
        return "add1"
    elif state["operation1"] == "-":
        return "subtract1"
    return "add1"  # Default case

def router2(state:AgentState)->str:
    if state["operation2"] == "+":
        return "add2"
    elif state["operation2"] == "-":
        return "subtract2"
    return "add2"  # Default case

graph = StateGraph(AgentState)
graph.add_node("add1", add_node1)
graph.add_node("subtract1", subtract_node1)
graph.add_node("add2", add_node2)
graph.add_node("subtract2", subtract_node2)
graph.add_node("router1", lambda state:state)
graph.add_node("router2", lambda state:state)

graph.add_edge(START,"router1")
graph.add_conditional_edges(
    "router1",
    router1,
    {
        "add1": "add1",
        "subtract1": "subtract1"
    }
)
graph.add_edge("add1", "router2")
graph.add_edge("subtract1", "router2")
graph.add_conditional_edges(
    "router2",
    router2,
    {
        "add2": "add2",
        "subtract2": "subtract2"
    }
)
graph.add_edge("add2", END)
graph.add_edge("subtract2", END)

app=graph.compile()
print(app.invoke({"number1":10, "number2":20, "number3":30, "number4":40, "operation1":"+", "operation2":"-", "final1":0, "final2":0}))
