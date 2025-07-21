a = int(input("Enter your age : "))
print("Your age is : ",a)

if(a >= 18):
    print("Your can drive")
else:
    print("Your can not drive")

num = int(input("Enter a number : "))
if(num < 0):
    print("The Number is Negative .")
elif(num == 0):
    print("The Number is Zero .")
else : 
    print("The Number is Positive .")

if(num < 0):
    print("The Number is Negative .")
elif(num == 0):
    print("The Number is Zero .")
else : 
    if(num > 0 and num < 20):
        print("The Number is between 1 and 20 .")
    elif(num > 20 and num < 50):
        print("The Number is between 21 and 50 .")
    else : 
        print("The Number is greater than 50 .")