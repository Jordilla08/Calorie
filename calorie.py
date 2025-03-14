# This program tracks daily calorie intake by summing user-provided food calorie values.

# Initialize the total calorie count
total_calories = 0

# Prompt the user for the number of foods they ate
num_foods = int(input("How many foods did you eat today? "))

# If there are foods to log, loop through and collect their calorie counts
for i in range(num_foods):
    # Ask the user for the name of the food
    food_name = input(f"Enter the name of food item #{i + 1}: ")
    
    # Ask for the calorie count of that food
    calories = int(input(f"Enter the calories for {food_name}: "))
    
    # Add the calories to the total
    total_calories += calories

# Display the total calorie intake
print(f"Total calorie intake: {total_calories} calories")
