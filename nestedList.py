# Nested lists in Python
# A list can contain other lists, creating a matrix-like or nested structure.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Matrix:")
for row in matrix:
    print(row)

print("\nAccessing an element:")
print(matrix[1][2])  # 6

print("\nNested loop to print each element:")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Flatten a nested list into a single list
flattened = []
for row in matrix:
    for value in row:
        flattened.append(value)

print("\nFlattened list:", flattened)

# Example of list of lists with strings
students = [
    ["Alice", 90],
    ["Bob", 85],
    ["Charlie", 92],
]

print("\nStudents:")
for student in students:
    print(student[0], "->", student[1])
