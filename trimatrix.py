from triangular import read_matrix, display_matrix
from triangular import is_uppertriangular, is_lowertriangular

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

if m != n:
    print("\nMatrix is neither Upper Triangular nor Lower Triangular because it is not a square matrix.")
else:
    print("\nEnter the matrix:")
    A = read_matrix(m, n)

    print("\nMatrix:")
    display_matrix(A)

    upper = is_uppertriangular(A)
    lower = is_lowertriangular(A)

    if upper:
        print("\nThe matrix is Upper Triangular.")

    if lower:
        print("The matrix is Lower Triangular.")