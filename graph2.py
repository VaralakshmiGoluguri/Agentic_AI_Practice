from typing import List, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    values : List[int]
    name: str
    result: str

def sum_values(state:AgentState)->AgentState:
    state["result"] = state["name"] + ", Your sum is " + str(sum(state["values"]))
    return state
graph=StateGraph(AgentState)
graph.add_node("sum_values", sum_values)
graph.set_entry_point("sum_values")
graph.set_finish_point("sum_values")
app=graph.compile()
result=app.invoke({"values":[1,2,3,4], "name":"Varuuu!!!"})
print(result["result"])

