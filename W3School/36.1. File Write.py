# # Python File Write
# # To write to an existing file, you must add a parameter to the open() function:
# # 1. "a" - Append - will append to the end of the file
# # 2. "w" - Write - will overwrite any existing content (That means will delete the previous content and add new lines.

a = "Open the file Hello.txt and append content to the file\n"
print(a)
#
# open and write to the file.
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Hello1.txt", "a")
f.write("\nNew line added\n")
f.close()

# #open and read the file
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Hello1.txt")
print(f.read())

b = "\nOpen the file Hello.txt and overwrite the content:\n"
print(b)

# Open and write
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Hello1.txt", "w")
f.write("Oops, deleted all previous content mistakenly.")
f.close()
#
# open and read
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Hello1.txt")
print(f.read())
