from operator import mul
from typing import List, TypedDict
from langgraph.graph import StateGraph
from functools import reduce
from IPython.display import Image, display

class AgentState(TypedDict):
    values: List[int]
    name: str
    operation: str
    result:str

def operation_values(state:AgentState)->AgentState:
    if(state["operation"]=="+"):
        state["result"] = state["name"] + ", Your result is " + str(sum(state["values"]))
    elif(state["operation"]=="*"):
        state["result"] = state["name"] + ", Your result is " + str(reduce(mul ,state["values"]))
    return state

graph=StateGraph(AgentState)
graph.add_node("operation_values", operation_values)
graph.set_entry_point("operation_values")
graph.set_finish_point("operation_values")
app=graph.compile()
display(Image(app.get_graph().draw_mermaid_png()))

result=app.invoke({"values":[1,2,3,4], "name":"Varuuu!!!", "operation":"+"})
result2=app.invoke({"values":[1,2,3,4], "name":"Varuuu!!!", "operation":"*"})
print(result["result"])
print(result2["result"])