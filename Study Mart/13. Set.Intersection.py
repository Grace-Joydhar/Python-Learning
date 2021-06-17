a = "Intersection means find the same data in different list"
print(a)

s1 = {1,2,3}
s2 = (2,3,4)
s3 = {3,4,5}

s4 = s1.intersection(s2)
print(s4)

s4 = s1.intersection(s2,s3)
print(s4)

b= "\nDifference:"
print(b)
s4 = s1.difference(s2) #Work will only for s1.
print(s4)

s4 = s1.symmetric_difference(s2) #will work for s1 and s2 both.
print(s4)

c = "\nRemove duplicate values from the list by converting to set."
print(c)

s5 =[1,2,3,4,5,1,2,3]
result = list(set([1,2,3,4,5,1,2,3])) #At first it will be converted to set. thn it will change to list
print(result) 