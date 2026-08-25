from vector import read_vector, display_vector, dot_product

n = int(input("Enter the dimension of the vectors: "))

print("\nEnter Vector 1:")
v1 = read_vector(n)

print("\nEnter Vector 2:")
v2 = read_vector(n)

result = dot_product(v1, v2)

print("\nVector 1:")
display_vector(v1)

print("Vector 2:")
display_vector(v2)

print("\nDot Product =", result)