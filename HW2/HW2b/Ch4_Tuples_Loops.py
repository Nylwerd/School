#tupples, https://docs.python.org/3/tutorial/datastructures.html

t = 12345, 54321, 'hello!'
print(t[0])

print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

t[0] = 88888

for t in t:
    print(t)

v = ([1, 2, 3], [3, 2, 1])
print(v)

for v in v:
    print(v)
