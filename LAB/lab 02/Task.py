# Lab Task 1
list1 = list(map(int, input("Enter first list of numbers: ").split()))
list2 = list(map(int, input("Enter second list of numbers: ").split()))

merged = list1 + list2
merged.sort()

print("Merged and Sorted List:", merged)


# Lab Task 2
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Smallest element:", min(numbers))
print("Largest element:", max(numbers))


# Lab Task 3: Numerical derivative of sin(x)
from math import sin, cos, pi

def derivative_sin(h):
    x_values = [i * h for i in range(int(-pi / h), int(pi / h) + 1)]
    for x in x_values:
        approx = (sin(x + h) - sin(x)) / h
        print(f"x={x:.3f}, derivative≈{approx:.6f}, cos(x)={cos(x):.6f}")

# Try with different h values
print("Using h = 0.001")
derivative_sin(0.001)

print("\nUsing h = 0.01")
derivative_sin(0.01)

print("\nUsing h = 0.1")
derivative_sin(0.1)



# Lab Task 4
birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
    print(name)

person = input("Who's birthday do you want to look up? ")

if person in birthdays:
    print(f"{person}'s birthday is {birthdays[person]}.")
else:
    print("Sorry, birthday not found.")


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
