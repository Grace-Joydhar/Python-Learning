'''Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.'''

x= 5
y = "Jhon"
print(x)
print(y)

'''Casting
If you want to specify the data type of a variable, this can be done with casting.'''
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

'''Get the Type
You can get the data type of a variable with the type() function.'''
x = 5
y = "Jhon"
z = 3.45
print(type(x))
print(type(y))
print(type(z))

'''Variables name can only be (A-z, 0-9, and _ )'''
myvar = "My "
my_var = "name "
myvar1 = "is "
_my_var = "Grace "
MYVAR = "Joydhar."
print(myvar + my_var + myvar1 + _my_var + MYVAR)


'''Multiple Values: Must use comma(,) in between values'''
x,y,z = "Banana", "Orange", "Apple"

print(x)
print(y)
print(z)

#One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack Collections
fruits = ["apple", "orange", "banana"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables: We need to add + before the varriable
x= "awesome"
print("python is " +x)

#Also we can add two variables using +
x = "Python is "
y = "Awesome."
z = x+y
print(z)

#Local and Global Variables: Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. But if we write global with a variable, that will be used in anywhere in your code and it will remain same.
#Local Variable outside a function
x = "Lovely"

def myfunction():
    print("python is " +x)

myfunction()

#Local Variable inside a function

def myfunc():
    x = "Beauty"
    print("Python is " +x)

myfunc()

#Local variable inside and outside a function

y= "do work"

def myfunc1():
    y = "think"
    print("People love to " + y)
myfunc1()

print("People love to " + y)

#Global Variable

def myfunc2():
    global x
    x= "Love"
    print("Bangladesh is a place of " + x)
myfunc2()

print("Bangladesh is a place of " + x)

'''Also, use the global keyword if you want to change a global variable inside a function.'''

x = "Awesome"

def myfunc3():
    global x
    x = "beautiful"
myfunc3()

print("Bangladesh is " + x)
