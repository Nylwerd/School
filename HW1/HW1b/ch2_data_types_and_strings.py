# Modified Program
hi = 'Hello {}'.format("World")
print (hi)

big = 123123123123123123123123123123123123123123123123 + 1
print(big)

base_ten = 10
print(base_ten)

octal = 0o10
print(octal)

hex_code = 0x10
print(hex_code)

binary_code = 0b10
print(binary_code)

single_quote = 'This string contains a single quote (\') character.'
print(single_quote)
double_quote = "This string contains a double quote (\") character."
print(double_quote)

period = 'a\
... b\
... c'
print(period)

slash = 'foo\\bar'
print(slash)
space = 'foo\tbar'
print(space)

table = "a\141\x61"
print(table)

case = 'HAPPY BIRTHDAY'
print(case.lower())

caps = 'I\'m not trying to shout!'
print(caps.upper())

name = "john green the magician"
print(name.title())

a, b = 4, 3
a = b

+a
-b
print("The result of the modulus = " + str(a % b))
print("Four to the third power = " + str(a ** b))