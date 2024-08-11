def print_2d_array(arr, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
        print()

# Get the number of rows and columns from user input
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty 2D array
my_2d_array = []

# Get values for each element from user input
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter value for element at position ({i+1}, {j+1}): "))
        row.append(value)
    my_2d_array.append(row)

# Print the 2D array
print("\nYour 2D array:")
print_2d_array(my_2d_array, rows, cols)
