import sys
a = "Set can not contain duplicate values:"
print(a)

s1 = set([1,2,3,4,5])
print(s1)

s2 = {1,2,3,4,5}
print(s2)

s3 = {1,2,3,4,5,1,2,3} #Set never works with duplicate values
print(s3)

b= "\nAdd a new value: To add many numbers we need to use update"
print(b)

s3.add(6) #Add will add only one value
print(s3)

s3.update([7,8,9]) #Update option can add many values
print(s3)

s4 = {10,11,12}
s3.update([13,14,15], s4)
print(s3)

d = "For removing a number from the list, we can write remove. But if the number is missed from the list, in that case the result will show error. So for a smooth result, we can write discard instead of remove. It will work properly"
print(d)
s3.remove(15)
s3.discard(17)
print(s3)

