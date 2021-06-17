

from array import* #Import all functions of array
a = "\nFor Integer Number use 'i'"
print(a)
salary = array('i', [3000, 4000, 5000, 6000])
print(salary)
print(salary[0])

print(salary.buffer_info())  # It will print the store position and length
print(salary.append(12000)) #Used to add a new value
print(salary)

print(salary.remove(4000)) #Used to remove a value from the array
print(salary)

print(salary.reverse())
print(salary)

for i in range(4):
    print(salary[i]) #To print all the values


b = "\nFor Float Number use 'f'"
print(b)

salary = array('f', [3000.5, 4000.0, 5000.0, 6000.0])
print(salary)
print(salary[0])

print(salary.buffer_info())  # It will print the store position and length
print(salary.append(12000.0)) #Used to add a new value
print(salary)

print(salary.remove(4000.0)) #Used to remove a value from the array
print(salary)

print(salary.reverse())
print(salary)

for f in range(4):
    print(salary[f]) #To print all the values

