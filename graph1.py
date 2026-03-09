from typing import Dict, TypedDict
from langgraph.graph import StateGraph #framework that helps to build and manage stateful workflows


#Way to define the state of the graph
class AgentState(TypedDict):
    message : str


#Way to define the node
def greeting_node(state: AgentState) -> AgentState:#will returns the updated state
    state["message"] = "Hello," + state["message"]
    return state

#Way to define the graph
graph = StateGraph(AgentState)

#Way to add the node to the graph
graph.add_node("greeting", greeting_node)

graph.set_entry_point("greeting")
graph.set_finish_point("greeting")

app = graph.compile()

result = app.invoke({"message": "Varuuu!!"})
print(result["message"])













