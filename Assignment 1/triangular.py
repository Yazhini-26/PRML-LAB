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


def is_uppertriangular(matrix):
    n = len(matrix)

    for i in range(1, n):
        for j in range(i):
            if matrix[i][j] != 0:
                return False

    return True


def is_lowertriangular(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False

    return True