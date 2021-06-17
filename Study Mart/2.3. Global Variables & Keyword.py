a= "Global Variables: When you write a variable outside of a function, that will be global variable. And you can use the function anywhere in your code."
print(a)

x= "Grace"
def myFunc():
    print("My name is: " +x)
myFunc()



b = "\nYou can also change the values of a global variable inside a function"
print(b)

y = "Grace"

def myNewFunc():
    y = "Antora"
    print("My nick name is: " +y)

myNewFunc()


c = "\nWe can also create a global variable inside a function by using 'global' keyword"

def myFuncNew1():
    global m
    m = "Bangladesh"
    print(m+ " is a beautiful country")
myFuncNew1()

def myFuncNew2():
    print(m+ " has a big population, around 17 cores") #same variable can be used in different places by using global keyword
myFuncNew2()