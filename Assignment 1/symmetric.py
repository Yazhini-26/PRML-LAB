def read_matrix(rows, cols):
    matrix = []

    print(f"Enter {rows * cols} elements:")

    for i in range(rows):
        row = list(map(int, input().split()))

        while len(row) != cols:
            print(f"Enter {cols} elements:")
            row = list(map(int, input().split()))

        matrix.append(row)

    return matrix


def display_matrix(matrix):
    for row in matrix:
        print(*row)


def issymmetric(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True