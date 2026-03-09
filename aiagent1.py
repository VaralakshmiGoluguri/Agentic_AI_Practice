# from typing import TypedDict, List
# from langchain_core.messages import HumanMessage
# from langchain_openai import ChatOpenAI
# from langgraph.graph import StateGraph, START, END
# # from dotenv import load_dotenv

# # load_dotenv()

# class AgentState(TypedDict):
#     messages: List[HumanMessage]

# llm=ChatOpenAI(model="gpt-4o", api_key="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")

# def process(state:AgentState)->AgentState:
#     response = llm.invoke(state["messages"])
#     return state

# graph = StateGraph(AgentState)
# graph.add_node("process",process)
# graph.add_edge(START, "process")
# graph.add_edge("process", END)
# agent = graph.compile()


# user_input = input("Enter: ")
# while user_input != "exit":
#     agent.invoke({"messages": [HumanMessage(content=user_input)]})
#     user_input = input("Enter: ")


from typing import TypedDict, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage
 

GOOGLE_API_KEY = ""

class AgentState(TypedDict):
    messages: List[HumanMessage | AIMessage]

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, google_api_key=GOOGLE_API_KEY)
 

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print("\nAI:", response.content)
    state["messages"].append(response)
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

print("Chat with Gemini (type 'exit' to quit)")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break
    agent.invoke({"messages": [HumanMessage(content=user_input)]})