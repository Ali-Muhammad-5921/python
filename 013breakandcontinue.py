for i in range(12):
    if( i==5 ):
        print("i : 5 , going to skip this iteration")
        continue
    if(i == 10):
        print("i : 10 , going to break")
        break
    print("5 x ", i+1 , "=", 5 *( i+1))
print("loop broken")

        # do while in python

i = 0
while True:
    i += 1 
    print(i)
    if(i % 10 == 0):
        break
    