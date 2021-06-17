a = "List is a collection which is changeable and ordered. It allows duplicate values."
print(a)

b= "\nList with nested list:"
print(b)
list = [1,["Grace", 5, 54, 60], 10,4.5,6, 6,20,22, "Grace"]
print(list)
print(list[1][3])

list.extend([3,4,5,6,7]) #To add new values in the array

list.remove(10) #Direct a value. But if there are same value more than 1 time, then it will only delete the first value. So we need to delete with index property.
list.remove(list[1]) #From the index.

print(list.count(6)) #To find a number's existance.
print(list)
