# from dataclasses import dataclass
# from typing import List, Dict, Tuple

# @dataclass
# class UserProfile:
#     age: int
#     weight_kg: float
#     height_cm: float
#     gender: str
#     activity_level: str
#     goal: str
    
#     @property
#     def bmi(self) -> float:
#         return self.weight_kg / ((self.height_cm / 100) ** 2)
    
#     @property
#     def ideal_weight(self) -> float:
#         if self.gender.lower() == 'male':
#             return 48.0 + 2.7 * ((self.height_cm * 0.393701) - 60)
#         else:
#             return 45.5 + 2.2 * ((self.height_cm * 0.393701) - 60)
    
#     def calculate_bmr(self) -> float:
#         if self.gender.lower() == 'male':
#             bmr = 88.362 + (13.397 * self.weight_kg) + (4.799 * self.height_cm) - (5.677 * self.age)
#         else:
#             bmr = 447.593 + (9.247 * self.weight_kg) + (3.098 * self.height_cm) - (4.330 * self.age)
#         return bmr
    
#     def calculate_tdee(self) -> float:
#         activity_multipliers = {
#             'sedentary': 1.2,
#             'light': 1.375,
#             'moderate': 1.55,
#             'active': 1.725,
#             'very active': 1.9
#         }
#         return self.calculate_bmr() * activity_multipliers.get(self.activity_level.lower(), 1.2)
    
#     def calculate_goal_calories(self) -> Tuple[float, str]:
#         tdee = self.calculate_tdee()
#         if self.goal.lower() == 'lose':
#             return tdee - 500, "Weight Loss (500 cal deficit)"
#         elif self.goal.lower() == 'gain':
#             return tdee + 500, "Weight Gain (500 cal surplus)"
#         return tdee, "Maintenance"

# def get_user_input() -> UserProfile:
#     print("\n=== AI Diet Planner ===\n")
    
#     while True:
#         try:
#             age = int(input("Enter your age: "))
#             if age <= 0 or age > 120:
#                 print("Please enter a valid age between 1-120")
#                 continue
#             break
#         except ValueError:
#             print("Please enter a valid number for age.")
    
#     while True:
#         try:
#             weight_kg = float(input("Enter your weight in kg: "))
#             if weight_kg <= 0 or weight_kg > 300:
#                 print("Please enter a valid weight between 1-300 kg")
#                 continue
#             break
#         except ValueError:
#             print("Please enter a valid number for weight.")
    
#     while True:
#         try:
#             height_cm = float(input("Enter your height in cm: "))
#             if height_cm <= 0 or height_cm > 300:
#                 print("Please enter a valid height between 1-300 cm")
#                 continue
#             break
#         except ValueError:
#             print("Please enter a valid number for height.")
    
#     while True:
#         gender = input("Enter your gender (male/female): ").lower()
#         if gender in ['male', 'female']:
#             break
#         print("Please enter 'male' or 'female'.")
    
#     while True:
#         activity_level = input("\nSelect your activity level:\n"
#                              "1. Sedentary (little to no exercise)\n"
#                              "2. Light (light exercise 1-3 days/week)\n"
#                              "3. Moderate (moderate exercise 3-5 days/week)\n"
#                              "4. Active (hard exercise 6-7 days/week)\n"
#                              "5. Very active (very hard exercise & physical job)\n"
#                              "Enter choice (1-5): ")
        
#         activity_map = {
#             '1': 'sedentary',
#             '2': 'light',
#             '3': 'moderate',
#             '4': 'active',
#             '5': 'very active'
#         }
        
#         if activity_level in activity_map:
#             activity_level = activity_map[activity_level]
#             break
#         print("Please enter a number between 1-5.")
    
#     while True:
#         goal = input("\nSelect your goal:\n"
#                     "1. Lose weight\n"
#                     "2. Maintain weight\n"
#                     "3. Gain weight\n"
#                     "Enter choice (1-3): ")
        
#         goal_map = {
#             '1': 'lose',
#             '2': 'maintain',
#             '3': 'gain'
#         }
        
#         if goal in goal_map:
#             goal = goal_map[goal]
#             break
#         print("Please enter a number between 1-3.")
    
#     return UserProfile(age, weight_kg, height_cm, gender, activity_level, goal)

# def generate_meal_plan(calories: float) -> Dict[str, List[Dict[str, str]]]:
#     """Generate a sample meal plan based on calorie target."""
#     # This is a simplified example. In a real app, you'd want a more comprehensive database of foods.
    
#     # Macronutrient distribution (40% carbs, 30% protein, 30% fat)
#     protein_cal = calories * 0.3
#     carbs_cal = calories * 0.4
#     fat_cal = calories * 0.3
    
#     # Convert to grams (4 cal/g for protein and carbs, 9 cal/g for fat)
#     protein_g = round(protein_cal / 4)
#     carbs_g = round(carbs_cal / 4)
#     fat_g = round(fat_cal / 9)
    
#     # Sample meal plan (simplified)
#     meals = {
#         'Breakfast': [
#             {"name": "Oatmeal with banana and almonds", "calories": round(calories * 0.25)},
#             {"name": "Scrambled eggs with whole wheat toast", "calories": round(calories * 0.25)}
#         ],
#         'Lunch': [
#             {"name": "Grilled chicken salad with olive oil dressing", "calories": round(calories * 0.35)},
#             {"name": "Quinoa bowl with vegetables and tofu", "calories": round(calories * 0.35)}
#         ],
#         'Dinner': [
#             {"name": "Baked salmon with sweet potato and broccoli", "calories": round(calories * 0.3)},
#             {"name": "Stir-fried tofu with brown rice and vegetables", "calories": round(calories * 0.3)}
#         ],
#         'Snacks': [
#             {"name": "Greek yogurt with berries", "calories": round(calories * 0.1)},
#             {"name": "Handful of mixed nuts", "calories": round(calories * 0.1)}
#         ]
#     }
    
#     return {
#         'macros': {
#             'protein_g': protein_g,
#             'carbs_g': carbs_g,
#             'fat_g': fat_g
#         },
#         'meals': meals
#     }

# def display_results(profile: UserProfile):
#     print("\n=== Your Diet Plan ===\n")
    
#     # Basic info
#     print(f"Age: {profile.age} years")
#     print(f"Weight: {profile.weight_kg} kg")
#     print(f"Height: {profile.height_cm} cm")
#     print(f"BMI: {profile.bmi:.1f}")
#     print(f"Ideal Weight: {profile.ideal_weight:.1f} kg")
    
#     # Calculations
#     bmr = profile.calculate_bmr()
#     tdee = profile.calculate_tdee()
#     goal_calories, goal_desc = profile.calculate_goal_calories()
    
#     print(f"\nBMR: {bmr:.0f} calories/day (calories burned at rest)")
#     print(f"TDEE: {tdee:.0f} calories/day (based on activity level)")
#     print(f"Goal: {goal_desc}")
#     print(f"Daily Calorie Target: {goal_calories:.0f} calories")
    
#     # Generate and display meal plan
#     meal_plan = generate_meal_plan(goal_calories)
    
#     print("\n=== Recommended Daily Macros ===")
#     print(f"Protein: {meal_plan['macros']['protein_g']}g")
#     print(f"Carbs: {meal_plan['macros']['carbs_g']}g")
#     print(f"Fats: {meal_plan['macros']['fat_g']}g")
    
#     print("\n=== Sample Meal Plan ===")
#     for meal_name, options in meal_plan['meals'].items():
#         print(f"\n{meal_name} (Choose one):")
#         for option in options:
#             print(f"- {option['name']} ({option['calories']} cal)")
    
#     print("\n=== Additional Recommendations ===")
#     print("- Drink at least 2-3 liters of water daily")
#     print("- Get 7-9 hours of quality sleep")
#     print("- Combine diet with regular exercise for best results")
#     print("- Consult a healthcare professional before starting any diet plan")

# def main():
#     try:
#         user_profile = get_user_input()
#         display_results(user_profile)
#     except KeyboardInterrupt:
#         print("\n\nOperation cancelled by user.")
#     except Exception as e:
#         print(f"\nAn error occurred: {str(e)}")

# if __name__ == "__main__":
#     main()






from typing import List, Dict, TypedDict, Optional
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    age: Optional[int]
    weight_kg: Optional[float]
    height_cm: Optional[float]
    gender: Optional[str]
    activity_level: Optional[str]
    goal: Optional[str]
    bmi: Optional[float] = None
    ideal_weight: Optional[float] = None
    bmr: Optional[float] = None
    tdee: Optional[float] = None
    goal_calories: Optional[float] = None
    goal_description: Optional[str] = None
    macros: Optional[Dict[str, float]] = None
    meal_plan: Optional[Dict[str, List[Dict[str, str]]]] = None


def collect_user_info(state: AgentState) -> AgentState:
    """Collect basic user information."""
    print("\n=== AI Diet Planner ===\n")
    
    while True:
        try:
            state['age'] = int(input("Enter your age: "))
            if state['age'] <= 0 or state['age'] > 120:
                print("Please enter a valid age between 1-120")
                continue
            break
        except ValueError:
            print("Please enter a valid number for age.")
    
    while True:
        try:
            state['weight_kg'] = float(input("Enter your weight in kg: "))
            if state['weight_kg'] <= 0 or state['weight_kg'] > 300:
                print("Please enter a valid weight between 1-300 kg")
                continue
            break
        except ValueError:
            print("Please enter a valid number for weight.")
    
    while True:
        try:
            state['height_cm'] = float(input("Enter your height in cm: "))
            if state['height_cm'] <= 0 or state['height_cm'] > 300:
                print("Please enter a valid height between 1-300 cm")
                continue
            break
        except ValueError:
            print("Please enter a valid number for height.")
    
    while True:
        gender = input("Enter your gender (male/female): ").lower()
        if gender in ['male', 'female']:
            state['gender'] = gender
            break
        print("Please enter 'male' or 'female'.")
    
    return state

def collect_activity_level(state: AgentState) -> AgentState:
    """Collect activity level information."""
    while True:
        activity_level = input("\nSelect your activity level:\n"
                             "1. Sedentary (little to no exercise)\n"
                             "2. Light (light exercise 1-3 days/week)\n"
                             "3. Moderate (moderate exercise 3-5 days/week)\n"
                             "4. Active (hard exercise 6-7 days/week)\n"
                             "5. Very active (very hard exercise & physical job)\n"
                             "Enter choice (1-5): ")
        
        activity_map = {
            '1': 'sedentary',
            '2': 'light',
            '3': 'moderate',
            '4': 'active',
            '5': 'very active'
        }
        
        if activity_level in activity_map:
            state['activity_level'] = activity_map[activity_level]
            break
        print("Please enter a number between 1-5.")
    
    return state

def collect_goal(state: AgentState) -> AgentState:
    """Collect user's goal."""
    while True:
        goal = input("\nSelect your goal:\n"
                    "1. Lose weight\n"
                    "2. Maintain weight\n"
                    "3. Gain weight\n"
                    "Enter choice (1-3): ")
        
        goal_map = {
            '1': 'lose',
            '2': 'maintain',
            '3': 'gain'
        }
        
        if goal in goal_map:
            state['goal'] = goal_map[goal]
            break
        print("Please enter a number between 1-3.")
    
    return state

def calculate_health_metrics(state: AgentState) -> AgentState:
    """Calculate BMI, ideal weight, BMR, and TDEE."""
    state['bmi'] = state['weight_kg'] / ((state['height_cm'] / 100) ** 2)
    if state['gender'] == 'male':
        state['ideal_weight'] = 48.0 + 2.7 * ((state['height_cm'] * 0.393701) - 60)
    else:
        state['ideal_weight'] = 45.5 + 2.2 * ((state['height_cm'] * 0.393701) - 60)
    
    if state['gender'] == 'male':
        state['bmr'] = 88.362 + (13.397 * state['weight_kg']) + (4.799 * state['height_cm']) - (5.677 * state['age'])
    else:
        state['bmr'] = 447.593 + (9.247 * state['weight_kg']) + (3.098 * state['height_cm']) - (4.330 * state['age'])
    
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    state['tdee'] = state['bmr'] * activity_multipliers.get(state['activity_level'], 1.2)
    
    return state

def calculate_goal_calories(state: AgentState) -> AgentState:
    """Calculate goal calories based on user's goal."""
    if state['goal'] == 'lose':
        state['goal_calories'] = state['tdee'] - 500
        state['goal_description'] = "Weight Loss (500 cal deficit)"
    elif state['goal'] == 'gain':
        state['goal_calories'] = state['tdee'] + 500
        state['goal_description'] = "Weight Gain (500 cal surplus)"
    else:
        state['goal_calories'] = state['tdee']
        state['goal_description'] = "Maintenance"
    return state

def generate_meal_plan(state: AgentState) -> AgentState:
    """Generate a meal plan based on the calculated calories."""
    calories = state['goal_calories']

    protein_cal = calories * 0.3
    carbs_cal = calories * 0.4
    fat_cal = calories * 0.3

    state['macros'] = {
        'protein_g': round(protein_cal / 4),
        'carbs_g': round(carbs_cal / 4),
        'fat_g': round(fat_cal / 9)
    }
    
    state['meal_plan'] = {
        'Breakfast': [
            {"name": "Oatmeal with banana and almonds", "calories": round(calories * 0.25)},
            {"name": "Scrambled eggs with whole wheat toast", "calories": round(calories * 0.25)}
        ],
        'Lunch': [
            {"name": "Grilled chicken salad with olive oil dressing", "calories": round(calories * 0.35)},
            {"name": "Quinoa bowl with vegetables and tofu", "calories": round(calories * 0.35)}
        ],
        'Dinner': [
            {"name": "Baked salmon with sweet potato and broccoli", "calories": round(calories * 0.3)},
            {"name": "Stir-fried tofu with brown rice and vegetables", "calories": round(calories * 0.3)}
        ],
        'Snacks': [
            {"name": "Greek yogurt with berries", "calories": round(calories * 0.1)},
            {"name": "Handful of mixed nuts", "calories": round(calories * 0.1)}
        ]
    }
    
    return state

def display_results(state: AgentState) -> AgentState:
    """Display the final results to the user."""
    print("\n=== Your Diet Plan ===\n")
    

    print(f"Age: {state['age']} years")
    print(f"Weight: {state['weight_kg']} kg")
    print(f"Height: {state['height_cm']} cm")
    print(f"BMI: {state['bmi']:.1f}")
    print(f"Ideal Weight: {state['ideal_weight']:.1f} kg")
    

    print(f"\nBMR: {state['bmr']:.0f} calories/day (calories burned at rest)")
    print(f"TDEE: {state['tdee']:.0f} calories/day (based on activity level)")
    print(f"Goal: {state['goal_description']}")
    print(f"Daily Calorie Target: {state['goal_calories']:.0f} calories")
    

    print("\n=== Recommended Daily Macros ===")
    print(f"Protein: {state['macros']['protein_g']}g")
    print(f"Carbs: {state['macros']['carbs_g']}g")
    print(f"Fats: {state['macros']['fat_g']}g")
    

    print("\n=== Sample Meal Plan ===")
    for meal_name, options in state['meal_plan'].items():
        print(f"\n{meal_name} (Choose one):")
        for option in options:
            print(f"- {option['name']} ({option['calories']} cal)")
    

    print("\n=== Additional Recommendations ===")
    print("- Drink at least 2-3 liters of water daily")
    print("- Get 7-9 hours of quality sleep")
    print("- Combine diet with regular exercise for best results")
    print("- Consult a healthcare professional before starting any diet plan")
    
    return state

def main():
    workflow = StateGraph(AgentState)
    workflow.add_node("collect_user_info", collect_user_info)
    workflow.add_node("collect_activity_level", collect_activity_level)
    workflow.add_node("collect_goal", collect_goal)
    workflow.add_node("calculate_health_metrics", calculate_health_metrics)
    workflow.add_node("calculate_goal_calories", calculate_goal_calories)
    workflow.add_node("generate_meal_plan", generate_meal_plan)
    workflow.add_node("display_results", display_results)
    

    workflow.add_edge("collect_user_info", "collect_activity_level")
    workflow.add_edge("collect_activity_level", "collect_goal")
    workflow.add_edge("collect_goal", "calculate_health_metrics")
    workflow.add_edge("calculate_health_metrics", "calculate_goal_calories")
    workflow.add_edge("calculate_goal_calories", "generate_meal_plan")
    workflow.add_edge("generate_meal_plan", "display_results")
    workflow.add_edge("display_results", END)

    workflow.set_entry_point("collect_user_info")
    
    # Compile the workflow
    app = workflow.compile()
    
    try:
        # Initialize the state
        initial_state = {
            'age': None,
            'weight_kg': None,
            'height_cm': None,
            'gender': None,
            'activity_level': None,
            'goal': None
        }
        
        # Run the workflow
        for output in app.stream(initial_state):
            # The workflow will handle all the steps
            pass
            
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()