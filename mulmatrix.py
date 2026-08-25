def read_matrix(rows, cols):
    matrix = []
    print(f"Enter {rows * cols} elements:")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix
def display_matrix(matrix):
    for row in matrix:
        print(*row)
def multiply_matrix(A, B, m, n, k):
    C = [[0 for _ in range(k)] for _ in range(m)]
    for i in range(m):
        for j in range(k):
            for l in range(n):
                C[i][j] += A[i][l] * B[l][j]

    return C