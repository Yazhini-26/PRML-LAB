def read_vector(n):
    print(f"Enter {n} elements:")
    vector = list(map(int, input().split()))

    while len(vector) != n:
        print(f"Enter {n} elements:")
        vector = list(map(int, input().split()))

    return vector


def display_vector(vector):
    print(*vector)


def dot_product(v1, v2):
    result = 0

    for i in range(len(v1)):
        result += v1[i] * v2[i]

    return result