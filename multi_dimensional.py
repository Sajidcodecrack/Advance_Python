def printed_array(rows, cols, arr):
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j],end=" ")
        print()


rows = (int)(input("Enter the value of row:"))
cols = (int)(input("Enter the value of coloumn:"))
my_arr = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = (int)(input("Enter the value of the elements:"))
        row.append(val)
    my_arr.append(row)

print("\nMy 2D array :")
printed_array(rows,cols,my_arr)
