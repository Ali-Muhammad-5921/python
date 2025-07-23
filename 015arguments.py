# def average(a = 10 , b = 5):
#     print("The average of ",a ,"and", b , "ïs : ", (a+b)/2)

# average() # agr average nhi daingy to default arguments use hongy
# average(4)
# average(4 ,5)
# average(b = 10 , a = 8) # keywords arguments

def average(*numbers): # *means the arguments are in form of tuple
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    #print("The average of all numbers is : ", sum/len(numbers))
    return sum/len(numbers)

avg = average(5,6)
print(avg)