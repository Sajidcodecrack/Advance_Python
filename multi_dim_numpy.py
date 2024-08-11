from numpy import *

arr1 = array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [11, 10, 5],
        [3, - 4, 1],
        [2, 1, 0],
        [4, 6, 7],
        [3, 1, 5],
        [1,1,7]
    ]
)
# print(arr1.shape)
# arr2=arr1.flatten()
# print(arr2)
arr3 = arr1.reshape(3, 3, 3,1)
print(arr3)
