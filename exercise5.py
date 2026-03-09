from typing import TypedDict, List, Literal
from langgraph.graph import StateGraph, START, END
from random import randint, choice

class AgentState(TypedDict):
    name: str
    number: int
    upper: int
    lower: int
    hint: str
    attempts: int
    guesses: List[int]

def setup_node(state: AgentState) -> AgentState:
    state["name"] = state["name"] + ", Welcome to Guessing Game!!!"
    state["number"] = randint(0, 20)
    state["upper"] = 20
    state["lower"] = 0
    state["attempts"] = 0
    state["guesses"] = []
    state["hint"] = "Choose a number between 0 and 20"
    print(f"DEBUG: Number to guess: {state['number']}")  # For testing
    return state

def guess_node(state: AgentState) -> AgentState:
    possible_guesses = [i for i in range(state["lower"], state["upper"] + 1) 
                       if i not in state["guesses"]]
    guess = choice(possible_guesses) if possible_guesses else state["lower"]
    state["guesses"].append(guess)
    state["attempts"] += 1
    print(f"Guess #{state['attempts']}: {guess}")
    return state

def hint_node(state: AgentState) -> AgentState:
    latest_guess = state["guesses"][-1]
    if latest_guess == state["number"]:
        state["hint"] = "You guessed it!"
    elif latest_guess < state["number"]:
        state["hint"] = "Too low"
        state["lower"] = latest_guess + 1
    else:
        state["hint"] = "Too high"
        state["upper"] = latest_guess - 1
    print(f"Hint: {state['hint']} (Range: {state['lower']}-{state['upper']})")
    return state

def should_continue(state: AgentState) -> Literal["continue", "end"]:
    latest_guess = state["guesses"][-1]
    if latest_guess == state["number"]:
        return "end"
    elif state["attempts"] >= 7:
        return "end"
    else:
        remaining = 7 - state["attempts"]
        return "continue"

# Create and configure the graph
graph = StateGraph(AgentState)
graph.add_node("setup", setup_node)
graph.add_node("guess", guess_node)
graph.add_node("hint_node", hint_node)

# Define the flow
graph.add_edge("setup", "guess")
graph.add_edge("guess", "hint_node")

# Add conditional edges for the loop
graph.add_conditional_edges(
    "hint_node", 
    should_continue,
    {
        "continue": "guess",
        "end": END
    }
)

# Set entry point and compile
graph.set_entry_point("setup")
app = graph.compile()

# Start the game
initial_state = {
    "name": "Player",
    "number": 0,  # Will be set by setup_node
    "upper": 0,   # Will be set by setup_node
    "lower": 0,   # Will be set by setup_node
    "hint": "",
    "attempts": 0,
    "guesses": []
}

result = app.invoke(initial_state)
print(f"Final state: {result}")