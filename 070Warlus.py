a = True
print(a:= False)

nums = [1, 2, 3 ,4 ,5]
while (n := len(nums)) > 0:
    print(nums.pop())

# assigns value as a part of larger expression

foods = list()
while (food := input('Enter food you like:')) != 'quit':
    foods.append(food)