import math
n= int(input("Enter any value: "))
f = math.factorial(n)
print(f)

#By Using Function:
'''def fact(n):
    initial = 1
    for i in range (1, n+1):
        initial = initial*i
    return initial
result = fact(5)
print(result)
'''

#In a normal way:
'''n = int(input("Enter any value: "))
f = 1
for i in range (1,n+1):
    f=f*i
print(f)
'''