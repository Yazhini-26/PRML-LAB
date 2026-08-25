from transpose import read_matrix, display_matrix, transpose_matrix

m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

A = read_matrix(m, n)

T = transpose_matrix(A)

print("\nOriginal Matrix:")
display_matrix(A)

print("\nTranspose Matrix:")
display_matrix(T)