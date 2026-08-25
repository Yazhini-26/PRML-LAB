def read_matrix(rows, cols):
    matrix = []

    print("Enter the matrix:")

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


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for j in range(cols):
        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        transpose.append(new_row)

    return transpose