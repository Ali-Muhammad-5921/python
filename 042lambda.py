def double (x):
    return x*2

cube = lambda x : x*x*x
avg = lambda x,y,z : (x+y+z)/3

def abx (fn , value):
    return 50 + fn(value)

print(double(2))
print(cube(2))
print(avg(10,25,0))
print(abx(cube , 2)) # this is same as the line below 
print(abx(lambda x : x*x*x,2))