# # Create a New File
# # To create a new file in Python, use the open() method, with one of the following parameters:
# # "x" - Create - will create a file, returns an error if the file exist
# # "a" - Append - will create a file if the specified file does not exist
# # "w" - Write - will create a file if the specified file does not exist

a = "Create New File\n"
print(a)

# #Create new file and write some text.
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Newfile.txt", "w")
f.write("This is a new file.\nYou can add whatever contents you want\n")

# open new file and read
f = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Newfile.txt")
print(f.read())

g= open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Del_file.txt", "w")
g.write("This is another new file.\nYou can delete the file")

g = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Del_file.txt")
print(g.read())

h = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Delete/Full_file_Del.txt", "w")
h.write("\nDelete the entire file You can delete the file")

h = open("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Delete/Full_file_Del.txt")
print(h.read())
