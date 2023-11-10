##########################################################
# Sofware Req Doc: HW2a
# Release Date: August 28, 2023
# Code Author: A. Lynn
# Description: This code shows the basics of creating a
# list.  It also will show the use of the insert, append
# del, and pop methods. This program will also show how
# to sort a list in ascending and descending order.
##########################################################
print('\tRequirement 1') # create a list of 8 items 
my_family = ['andrew', 'jessica', 'william', 'noah', 'adela', 'oreo', 'atticus', 'puffer']
print(my_family)

print('\tRequirement 2') # print the list in a single column
for a in my_family: print(a.title())

print('\tRequirement 3') # Print a paragraph if text and access all list items
print(f'There are a lot of people in my family. {my_family[0].title()} is me\
and i am awesome! {my_family[1].title()} is my wife and she is a woman superstar! \
{my_family[2].title()} is my oldest son and he is 12 and starting the 8th grade. \
{my_family[3].title()} is 7 and he is going into 2nd grade! {my_family[4].title()} \
is our youngest and only girl and she is 5 starting kindergarten this year! Our \
lovable dog {my_family[5].title()} is a piebald dachshund and he loves cuddles! \
Our old grumpy poodle {my_family[6].title()} is friendly to the family, but does \
not like strangers. We have a silly fish named {my_family[7].title()}.')

print('\tRequirement 4') # Modify two items from the list
my_family[6] = 'panda'
my_family[7] = 'flip'
print(f'We recently lost Atticus and {my_family[6].title()} replaced him and she is \
so cute and cuddly.  Someone also forgot to feed Puffer so we bought a beta fish named \
{my_family[7].title()}.')

print('\tRequirement 5') # Use insert, append, and del methods
my_family.insert(5, 'natalie')
my_family.append('fawkes')
del my_family[0]
print(my_family)
popped_family = my_family.pop()
print('The best person in the family is ' + popped_family.title() + ', because he knows \
the greatest professor to ever live.')


print('\tRequirement 6') # Remove an item by name
my_family.remove('flip')
print(my_family)

print('\tRequirement 7') # Sort the list in ascending order
my_family.sort()
print(my_family)

print('\tRequirement 8') # Temporarily sor the list in reverse order
print(sorted(my_family, reverse=True))

#Requirement 9
#my_family[8]