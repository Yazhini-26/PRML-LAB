from mulmatrix import read_matrix, display_matrix, multiply_matrix

m = int(input("Enter number of rows of Matrix A (m): "))
n = int(input("Enter number of columns of Matrix A (n): "))
k = int(input("Enter number of columns of Matrix B (k): "))

print("\nEnter Matrix A:")
A = read_matrix(m, n)

print("\nEnter Matrix B:")
B = read_matrix(n, k)

C = multiply_matrix(A, B, m, n, k)

print("\nMatrix A:")
display_matrix(A)

print("\nMatrix B:")
display_matrix(B)

print("\nResultant Matrix (A × B):")
display_matrix(C)