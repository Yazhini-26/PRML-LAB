from symmetric import read_matrix, display_matrix, issymmetric

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

if m != n:
    print("\nThe matrix is not symmetric because it is not a square matrix.")
else:
    print("\nEnter the matrix:")
    A = read_matrix(m, n)

    print("\nMatrix:")
    display_matrix(A)

    if issymmetric(A):
        print("\nThe matrix is Symmetric.")
    else:
        print("\nThe matrix is Not Symmetric.")