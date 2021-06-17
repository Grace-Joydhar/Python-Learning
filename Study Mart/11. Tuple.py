
import sys
a = "Tuple is a collection which is odered but unchangeable.\nThat means there is no option to add or remove data directly from the array. But we can put duplicate values"
print(a)

tuple = (1, (2,3,4),5, 6,7)
print('tuple', sys.getsizeof(tuple)) #Memory requirement low
print(tuple)

'''del tuple #For Delete the array.
print(tuple)'''

list = [1, [2,3,4],5, 6,7]
print('list', sys.getsizeof(list)) #Memory requirement high
print(list)