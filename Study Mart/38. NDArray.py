from numpy import *

a= "2D array:"
print(a)

arr1 = array([
    [1, 2, 3, 4, 9, 2],
    [5, 6, 7, 8, 4, 1]
])

print("Array 1 is: ", arr1)
print("Datatype of Array1: ", arr1.dtype)
print("Dimension of Array1 :", arr1.ndim)
print("Shape of Array1 : ", arr1.shape)

b = "\n2D to 1D Array"
print(b)

arr2 = arr1.flatten()
print(arr2)
print("Datatype of Array2: ", arr2.dtype)
print("Dimension of Array2 :", arr2.ndim)
print("Shape of Array2 : ", arr2.shape)

c = "\n1D to 2D Array"
print(c)

arr3 = arr2.reshape(3, 4)
print(arr3)
print("Datatype of Array3: ", arr3.dtype)
print("Dimension of Array3 :", arr3.ndim)
print("Shape of Array3 : ", arr3.shape)

d = "\n2D to 3D Array"
print(d)

arr4 = arr1.reshape(3, 2, 2)
print(arr4)
print("Datatype of Array4: ", arr4.dtype)
print("Dimension of Array4 :", arr4.ndim)
print("Shape of Array4 : ", arr4.shape)


e = "\n2D to 3D Array - Practice"
print(e)
arr5 = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr6 = arr5.reshape(3, 2, 3)
print(arr6)