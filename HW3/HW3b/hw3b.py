##########################################################
# Sofware Req Doc: HW3b
# Release Date: September 19, 2023
# Code Author: A. Lynn
# Description: This program shows the basic functionality
# of using while loops and working with user input. This 
# program also shows how to take items from one list and 
# move them to another list using basic looping.
##########################################################

# Requirement 1: welcome message and dinner question
prompt = "Welcome to Zion's Pizza Restaurant"
prompt += "\nHow many people will be dining tonight? "
num_people = input(prompt)

# Requirement 2: if loop for table status
if int(num_people) > 8:
    print("Sorry, but you will need to wait for a table.")
else:
    print("Excellent, we have a table ready for you.\n")

    # Requirement 3: while loop for pizza toppings
    pizza_toppings = []
    active = True
    
    while active:
        topping = input("Enter a pizza topping or 'quit' to finish your order: ")
        if topping == 'quit':
            active = False
        else:
            # Requirement 4: print statement for adding pizza toppings
            print(f"I'll add {topping.capitalize()} to your pizza.")
            pizza_toppings.append(topping)

    # Added for loop to show appended list (for my own sanity check)
    print("\nHere is your pizza with the following toppings:")
    for topping in pizza_toppings:
        print(f" {topping.capitalize()}")

# Requirement 5: various sandwiches in a list
sandwich_orders = ["BMT with bacon", "tuna", "ham & cheese", "teriyaki"]
# Requirement 6: empty finsihed sandwiches
finished_sandwiches = []

# Requirement 7: while loop to move sandwhiches from orders to finished
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I am working on your {sandwich.capitalize()} sandwich.")
    # Requirement 8: move sandwhiches to finished sandwiches
    finished_sandwiches.append(sandwich)

# Requirement 9: for loop to list the sandwiches
print("\nHere are the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f" {sandwich.capitalize()} sandwich")