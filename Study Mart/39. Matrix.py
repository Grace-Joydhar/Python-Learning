import numpy as np

m1=([1,2,3],
    [4,5,6],
    [7,8,9]
)

m2=([7,8,9],
    [1,2,3],
    [4,5,6]
)

result1 = np.add(m1,m2)
print("The addition of matrix is: ", result1)

result2 = np.subtract(m1,m2)
print("\nThe sub of matrix is: ", result2)

result3 = np.dot(m1,m2)
print("\nThe mul of matrix is: ", result3)

result4 = np.divide(m1,m2)
print("\nThe division of matrix is: ", result4)