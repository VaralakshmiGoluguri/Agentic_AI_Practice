from random import randint
from typing import TypedDict,List
from langgraph.graph import START, END, StateGraph

class AgentState(TypedDict):
    name:str
    num:List[int]
    counter:int


def greet_node(state:AgentState)->AgentState:
    state['name'] = state['name'] + ", you are learning AgentAI"
    state["counter"]=0
    state["num"] = []
    return state

def random_node(state:AgentState)->AgentState:
    state["num"].append(randint(0,100))
    state["counter"]+=1
    return state

def should_continue(state:AgentState)->AgentState:
    if state["counter"]<10:
        return "loop"
    else:
        return "exit"

graph = StateGraph(AgentState)
graph.add_node("greet_node",greet_node)
graph.add_node("random_node", random_node)
graph.add_edge("greet_node", "random_node")

graph.add_conditional_edges(
    "random_node",
    should_continue,
    {
        "loop":"random_node",
        "exit": END
    }
)

graph.set_entry_point("greet_node")
app=graph.compile()
print(app.invoke({"name":"Varuuu!!!","num":[],"counter":0}))