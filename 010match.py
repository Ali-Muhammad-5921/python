x = int(input("Enter a number : "))

match x :
    case 0 : 
        print("x is zero.")
    case _ if(x > 0 and x <= 50) :
        print("x is between 1 and 50")
    case _ if(x > 50 and x <= 100 ):
        print("x is between 51 and 100")
    case _ :
        print("x is greater than 100")