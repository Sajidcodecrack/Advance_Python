def create_matrix(row, col):
    matrix = []
    for i in range(row):
        row = []
        for j in range(col):
            element= (int)(input("Enter the elements at position : "))
            row.append(element)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
            print()


def main():
    row = (int)(input("Enter the row size: "))
    col = (int)(input("Enter the coloumn size"))
    matrix = create_matrix(row, col)
    print("\n The printed matrix :")
    print_matrix(matrix)
    
if __name__=="__main__":
    main()
