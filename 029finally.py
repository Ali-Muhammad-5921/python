
try:
    i = [21,54,87,98,65]
    i1 = int(input("Enter a number"))
except :
    print('some error')

finally:
    print("I'm always executed .")
# this is same as :
print("I'm always executed .")

# but difference is in function 

def someFun () :
    try:
        i1 = int(input("Enter a number"))
        return i1
    except :
        print('some error')
        return 0

    finally: # this will be printed regaredles of the return statement in both try and except
        print("I'm always executed .")
    # this is same as :             this will not be
    print("I'm always executed .")

a = someFun()