print("************* Age detection ***************")
age=int(input("Enter your age : "))
print(age)
print("Taking decession of the given age ")
if age<0:
    print("Unborn human being ")
elif age==0 or age<= 5:
    print("He /she is a baby ")
else:
    print("He / she is a adult ")