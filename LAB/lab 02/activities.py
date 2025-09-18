# Activity 1
list1 = input("Enter elements of first list separated by space: ").split()
list2 = input("Enter elements of second list separated by space: ").split()

joined_list = list1 + list2
print("Joined List:", joined_list)


# Activity 2
def is_palindrome(s):
    s = s.lower()  # ignore case
    return s == s[::-1]

word = input("Enter a string: ")
if is_palindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


# Activity 3
a = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Result matrix (3x3)
c = [[0 for _ in range(3)] for _ in range(3)]

# Multiply
for i in range(3):
    for j in range(3):
        for k in range(3):
            c[i][j] += a[i][k] * b[k][j]

print("Matrix C (a * b):")
for row in c:
    print(row)


# Lab Task 5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

new_dict = {k: sample_dict[k] for k in keys}
print("Extracted Dictionary:", new_dict)

# Activity 4: Polygon Perimeter
import math

def polygon_perimeter(points):
    perimeter = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # wrap around to first point
        perimeter += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return perimeter

# Example (6-sided polygon)
polygon = [(0,0), (2,0), (2,2), (4,2), (4,0), (0,0)]
print("Perimeter:", polygon_perimeter(polygon))


# Activity 5
def symmetric_diff(A, B):
    C = []
    for x in A:
        if x not in B and x not in C:
            C.append(x)
    for y in B:
        if y not in A and y not in C:
            C.append(y)
    return C

A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

C = symmetric_diff(A, B)
print("Symmetric Difference (custom function):", C)

# Built-in checks
setA = set(A)
setB = set(B)
print("A ^ B:", setA ^ setB)
print("B ^ A:", setB ^ setA)
print("A.symmetric_difference(B):", setA.symmetric_difference(setB))


# Activity 6
phonebook = {
    ("Albert", "Einstein"): "123-456-789",
    ("Isaac", "Newton"): "987-654-321",
    ("Marie", "Curie"): "555-123-456"
}

first = input("Enter first name: ")
last = input("Enter last name: ")

key = (first, last)
if key in phonebook:
    print(f"Phone number of {first} {last} is {phonebook[key]}")
else:
    print("Sorry, name not found.")


