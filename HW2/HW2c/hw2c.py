##########################################################
# Sofware Req Doc: HW2c
# Release Date: September 12, 2023
# Code Author: A. Lynn
# Description: This program shows how to work with lists
# it also demonstrates how to use for loops, if, elif, and
# else statements.  This program also uses tuples and shows
# how to work with tuples
##########################################################

# Requirement 1
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Requirement 2
truth = cars[1] == 'bmw'
print(truth)
# Requiremment 3
fallacy = cars[1] != 'bmw'
print(fallacy)

# Requirement 4
if 'subaru' in cars:
    print('The Subi is Home!')
# Requirement 5
if 'ford' not in cars:
    print('We left the Ford at Grandpa\'s house')
# Requirement 6
if cars[3] != 'toyota':
    print('The Yoda is Gone')
elif cars[3] == 'offroad':
    print('Yoda is fighting for the darkside!')
else:
    print('Yoda is safe')

# Requirement 7
aTuple = 'fare', 12, 1, [1, 4, 7]
print(aTuple)
