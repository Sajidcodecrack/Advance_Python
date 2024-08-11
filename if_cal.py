print("************ Please select a option **************")
a = (int)(input("Enter the first value : "))
b = (int)(input("Enter the second value :"))
op = input(("Choose a option : (+) (-) (*) (/) (%))"))
if op == "+":
    c = a + b
    print("Summation of the two values : ", c)
elif op == "-":
    if a > b:
        d = a - b
        print("Subtraction of the two values: ", d)
    else:
        d = b - a
        print("Subtraction of the two values: ", d)
elif op == "*":
    e = a * b
    print("Product of this two values are : ", e)
elif op == "/":
    if a > b:
        f = float(a / b)
        print("Divisonal value of this two values : ", f)
    else:
        f = float(a / b)
        print("Division of the two values : ", f)
else:
    if a < b:
        per = float(a / b) * 100
        print("Percentage of the two values : ", per)
    elif a > b:
        per = float(a / b) * 100
        print("Percentage can't be over 100 : ", per)
