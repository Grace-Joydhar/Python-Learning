x = "File Open and Read\n"
print(x)

f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Hello.txt")
print(f.read())

a = "\nReturn the 5 first characters of the file:"
print(a)
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Hello.txt", "rt")
print(f.read(5))

# #Read Lines
b = "\nYou can return one line by using the readline() method. By calling readline() two times, you can read the two first lines"
print(b)
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Hello.txt", "rt")
print(f.readline())

c = "\nBy looping through the lines of the file, you can read the whole file, line by line:"
print(c)
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Hello.txt", "rt")
for lines in f:
    print(lines)

d = "\nClose Files. It is a good practice to always close the file when you are done with it."
print(d)
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Hello.txt")
print(f.readline())
f.close()
