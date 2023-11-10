##########################################################
# Sofware Req Doc: HW4c
# Release Date: October 10, 2023
# Code Author: A. Lynn
# Description: This program shows ways to work with files.
# It first shows three methods for reading from a file.
# Finally the program shows how to write to a file with 
# user input. 
##########################################################

print("---Reading Entire File---")
# Requirement 4
with open('./hw4c.txt') as file_object:
	contents = file_object.read()
print(contents)

print("\n---Looping Lines in Entire File")
# Requirement 5
filename = 'hw4c.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

print("\n---Storing Lines in a List---")
# Requirement 6
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

print()
# Requirement 7
filename = 'hw4c_guest.txt'
name = input("What is your name: ")

# Requirement 8
with open(filename, 'w') as file_object:
	file_object.write(f"{name}\n")
