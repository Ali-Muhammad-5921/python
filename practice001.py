for i in range(5):
    print('Ali Muhammad')

fruits = []
for i in range(5):
    fruit_name = input(f'Enter the fruit number {i+1} : ')
    fruits.append(fruit_name)

for i in range(5):
    print(f'Fruit number {i+1} is : {fruits[i]}')

def add():
    a = int(input('Enter the First Number :'))
    b = int(input('Enter the Second Number :'))
    print(f'The sum of {a} and {b} is {a+b}')

student1 = {
    'marks': 78
}
student2 = {
    'marks': 87
}
student3 = {
    'marks': 90
}
print(student1['marks'])
print(student2['marks'])
print(student3['marks'])
