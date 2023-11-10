##########################################################
# Sofware Req Doc: HW3a
# Release Date: September 12, 2023
# Code Author: A. Lynn
# Description: This program shows how to work with dictionaries
# it also demonstrates how to use for loops and how to use them
# to work with dictionaries.
##########################################################

# Requirement 1-3
glossary = {
    'tuple': 'a list that cannot be changed, immuntable',
    'loop': 'a way to repeat the same action on multiple items',
    'range': 'a function to generate a series of numbers',
    'nesting': 'placing a function inside of another function',
    'pep': 'a styling guide to help programmers style their code',
}

# Requirement 4
for key, value in glossary.items():
    print(f"{key.upper()}: {value.capitalize()}.\n")

# Requirement 6
person_1 = {
    'first_name': 'michael', 
    'last_name': 'felix', 
    'age': 22, 
    'city': 'Jackson',
}
person_2 = {
    'first_name': 'taylor', 
    'last_name': 'snake', 
    'age': 29, 
    'city': 'fairchild',
}
person_3 = {
    'first_name': 'juliana', 
    'last_name': 'moore', 
    'age': 33, 
    'city': 'zane',
}

# Requirement 7
people = []
people.append(person_1)
people.append(person_2)
people.append(person_3)

# Requirement 8 & 9
for person in people:
    print (f"{person['first_name'].title()} {person['last_name'].title()} of \
{person['city'].title()} is {person['age']} years young.")