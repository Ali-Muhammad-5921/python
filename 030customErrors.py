# a = int(input("Enter a number between 5 and 10 :"))



# # if a > 5 and a < 10 :
# #     print(f"The number is : {a}")

# if a < 5 and a > 10 :
#     raise ValueError("Value should be between 5 and 10")
# # python error classes sy error class dekh kr error raise kr lena 
# elif a == "quit" :
#     print("Program Ended .")
# else :
#     print(f"The number is : {a}")

user_input = input("Enter a number between 5 and 10 (or type 'quit' to exit): ")

if user_input.lower() == "quit":
    print("Program Ended.")
else:
    try:
        a = int(user_input)
        if 5 <= a <= 10:
            print(f"The number is: {a}")
        else:
            raise ValueError("Value should be between 5 and 10.")
    except ValueError as ve:
        print(f"Error: {ve}")
