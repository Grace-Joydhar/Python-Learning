import mymodule

mymodule.greeting("Jhon")

#Variables in Module
#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)

a = mymodule.person1["age"]
print(a)

#Built-in Modules
#There are several built-in modules in Python, which you can import whenever you like.


import platform

x = platform.system()
print("\n",x)

#Using the dir() Function
#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

y = dir(platform)
print(y)