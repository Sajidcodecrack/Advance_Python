from numpy import *
m=matrix('1,2,3;4,5,6;7,11,9')
print(m)
print("Diagonal value of the matrix:")
print(diagonal(m))
n=max(diagonal(m))

print("Summation: ",n)