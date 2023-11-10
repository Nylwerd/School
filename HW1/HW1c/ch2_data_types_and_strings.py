##########################################################
# Sofware Req Doc: HW1c
# Release Date: August 28, 2023
# Code Author: A. Lynn
# Description: This code shows simple file header, basics 
#   of Python variables, data types, operators (Req b) and 
#   strings (Req a). In addition, the use of basic software 
#   requirement development and comments. 
#########################################################
#req a.vii
hi = 'Hello {}'.format("World")
print (hi)
#req a.i
new_line = "Hello World!\n"
print(new_line)
#req b.i
big = 123123123123123123123123123123123123123123123123 + 1
print(big)
#req b.ii.1
base_ten = 10
print(base_ten)
#req b.ii.2
octal = 0o10
print(octal)
#req b.ii.3
hex_code = 0x10
print(hex_code)
#req b.ii.4
binary_code = 0b10
print(binary_code)
#req a.iii
single_quote = 'This string contains a single quote (\') character.'
print(single_quote)
#req a.iv
double_quote = "This string contains a double quote (\") character."
print(double_quote)
#req a.vi
period = 'a\
... b\
... c'
print(period)
#req a.v
slash = 'foo\\bar'
print(slash)
#req a.ii
tab = 'foo\tbar'
print(tab)
#req b.iii
table = "a\141\x61"
print(table)
#req a.x
case = 'HAPPY BIRTHDAY'
print(case.lower())
#req a.ix
caps = 'I\'m not trying to shout!'
print(caps.upper())
#req a.viii
name = "john green the magician"
print(name.title())
#req b.iv
a, b = 4, 3
#req b.iv.1
a = b
#req b.v.1
+a
#req b.v.2
-b
#req b.vi.1
print("The result of the modulus = " + str(a % b))
#req b.vi.2
print("Four to the third power = " + str(a ** b))