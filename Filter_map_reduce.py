from functools import reduce
# def even(n):
#     return n%2==0 #without using lamda


# def update(n):
#     return n * 2

# def add_all(a,b):
#     return a+b
num = [2, 3, 4, 5, 6, 7, 8, 9, 1]
even = list(filter(lambda n: n % 2 == 0, num))
odd = list(filter(lambda n: n % 2 != 0, num))
print(even)
print(odd)
double=list(map(lambda n:n*2,even))
double1=list(map(lambda n:n*2,odd))
print("Double even values :", double)
print("Double odd values:", double1)

sum=reduce(lambda a,b:a+b,double1)
sum2=reduce(lambda a,b:a-b,double1)
print("New sum is : ",sum2)
print("sum is :",sum)
