# a=(int)(input("Enter the array size : "))
# n=[]
# i=0
# while i<a:
#     x=(int)(input(f"Enter the elements in array {i+1} :"))
#     n.append(x)
#     i=i+1
# print(f"Printing the array :\n",n)

# a = int(input("Enter the array size: "))
n = []
a = int(input("Enter the size:"))

for i in range(a):
    x = int(input(f"Enter the value {i+1}: "))
    if i % 2 == 0:
        n.append(x)

print("Array with elements at odd indices:", n)

print("Odd numbers in the array:")
for num in n:
    if num % 2 != 0:
        print(num)
        print(n.reverse)
