# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function

import os

a = "Remove the file only: os.remove(File name)\n"
print(a)
# if os.path.exists("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Del_file.txt"):
#     os.remove("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Del_file.txt")
# else:
#     print("The file does not exist ")


b = "Remove the entire folder: os.rmdir(File name)\n"
print(b)
# if os.path.exists("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Delete"):
#     os.rmdir("C://Users/DOLPHIN-PC/PycharmProjects/Python_Learning/Sample/Delete")
# else:
#     print("Entire Delete")