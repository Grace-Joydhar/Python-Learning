a= "Different types of error occurs in Programming"
print(a)

b = "\n1. Compile Time Error: It is also called syntax error. When we forget to write any complete word (prin instead of print) or miss any collon, coma or anythibng else, then it occurs."
print(b)

c ="\Logical Error: For example - a= 5, b= 10. then a+b will be 15. But result shows 12."
print(c)

d = "\nRun Time Error: 5/0, there will be no result. cause we can not divide any number by 0. So the code will be stopped\n"
print(d)

e = "\nIf we write except Exception, Then it will work for all kind of exception. Otherwise we can define every exception seperately.\n"
print(e)

x = 5
y = 0

try:
    print("Resource Open: ")
    print(x/y)
    z = int(input("Enter a number: "))
except ZeroDivisionError:
    print("You can not divide a number by zero")
except ValueError:
    print("Wrong input")
finally:
    print("Resource Close")
print("Done")