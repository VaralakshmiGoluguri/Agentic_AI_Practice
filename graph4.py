from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    number1: int
    number2: int
    result: int
    operation: str

def add_node(state: AgentState) -> AgentState:
    state["result"] = state["number1"] + state["number2"]
    return state

def subtract_node(state: AgentState) -> AgentState:
    state["result"] = state["number1"] - state["number2"]
    return state

def router(state: AgentState) -> str:
    if state["operation"] == "+":
        return "add"
    elif state["operation"] == "-":
        return "subtract"
    return "add"  # Default case

# Create the graph
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("add", add_node)
graph.add_node("subtract", subtract_node)
graph.add_node("router", lambda state: state)  # Pass-through node

# Define the graph flow
graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router",
    router,
    {
        "add": "add",
        "subtract": "subtract"
    }
)
graph.add_edge("add", END)
graph.add_edge("subtract", END)

# Compile the graph
app = graph.compile()

# Test cases
result = app.invoke({"number1": 10, "number2": 20, "operation": "+", "result": 0})
print("10 + 20 =", result["result"])

result2 = app.invoke({"number1": 20, "number2": 10, "operation": "-", "result": 0})
print("20 - 10 =", result2["result"])