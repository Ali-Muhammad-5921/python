from functools import reduce

cube = lambda x : x*x*x

num = [1,2,3,4,5]

newNum = list(map(cube, num)) # map function map vlaue type return krta hy islo list ma convert kr skty hain

print(newNum)

x = lambda a : a>=3
newNo = list(filter(x , num))
print(newNo)

# map , filter and reduce are higher order functions i.e. they take functions as arguments

s = lambda x, y : x+y

ab = reduce(s , num)
print(ab)
