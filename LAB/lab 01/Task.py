# Lab Task 1: Reverse digits of an integer
num = int(input("Enter an integer: "))
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

print("Reversed number:", reverse_num)


# Lab Task 2: Sum of even and odd numbers
numbers = list(map(int, input("Enter integers separated by space: ").split()))
even_sum = 0
odd_sum = 0

for n in numbers:
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)


# Lab Task 3: Fibonacci series
terms = int(input("Enter number of terms: "))
a, b = 0, 1

print("Fibonacci series:")
for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b


# Lab Task 4: Student grades
marks = int(input("Enter marks (1-100): "))

if marks < 50:
    grade = "F"
elif marks <= 60:
    grade = "E"
elif marks <= 70:
    grade = "D"
elif marks <= 80:
    grade = "C"
elif marks <= 90:
    grade = "B"
elif marks <= 100:
    grade = "A"
else:
    grade = "Invalid input!"

print("Grade:", grade)



# Lab Task 5: Factorial of a number
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)
