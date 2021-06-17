#Same Memory Location
x=12
y=x
print(id(x))
print(id(y))

#Different Memory Location
x=5
y=10
z=15
print(id(x))
print(id(y))
print(id(z))