# Activity 1
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")


# Activity 2
total = 0

while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    total += num

print("Sum of values:", total)


# Activity 3
num = int(input("Enter an integer: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is NOT a prime number")


# Activity 4
total = 0

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    total += num

print("Sum of 5 numbers:", total)


# Activity 6
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name, "! You are", age, "years old.")


# Activity 7
import random

secret = random.randint(1, 9)
guesses = 0

while True:
    guess = input("Guess a number between 1 and 9 (or type 'exit' to quit): ")
    
    if guess.lower() == "exit":
        print("Game ended! You made", guesses, "guesses.")
        break

    guess = int(guess)
    guesses += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Exactly right! You guessed it in", guesses, "tries.")
        break
