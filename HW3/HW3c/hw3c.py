##########################################################
# Sofware Req Doc: HW3c
# Release Date: September 19, 2023
# Code Author: A. Lynn
# Description: This program shows the basic useage of
# functions. We also show in this program how to call
# functions as well as how to pass arguments to the function
# this program also shows the basic usage of the return value
##########################################################

# Requirement 1: greet function that does no take paramaters or return value
def greet():
    """Displays the hello world message"""
    # Requirement 2: greet function prints "Hello World!" message
    print("Hello World!")

# Requirement 3: defining the add function 
def add(num1, num2):
    """Adds two numbers together"""
    result = num1 + num2
    return result
# Requirement 4: calling the add function with 4 and 5 as the parameters
print(add(4,5))

# Requirement 5: defining the city_country function
def city_country(city, country):
    """Return the names of a city and country"""
    # Requirement 6: neatly formatted string
    return f"{city.title()}, {country.title()}"

# Requirement 7: calling the city_country function and passing parameters
print(city_country('prague', 'czechia'))
print(city_country('lake bled', 'slovenia'))
print(city_country('munich', 'germany'))
