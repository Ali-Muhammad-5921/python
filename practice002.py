
                            # Difficulty Level : Easy 

# Q 1 : print all numbers from 1 to 20
for i in range(20):
    print(f'{i+1}')

# Q2 : print all even numbers from 1 to 50 

for i in range (1,51):
    if i % 2 == 0:
        print(i)

# Q3 : print all numbers from 10 to 1 
for i in range(10):
    print(f'{10 - i}')

# Q4 : take a number from user and print its table
num = int(input('Enter a number whose table you want to print :'))
for i in range(10):
    print(f'{num} x {i+1} = {num* (i+1)}')

# Q 5 : find sum of numbers from 1 till 100 using loop
total = 0
for i in range(1,101):
    total += i

print(total) 


                            # Difficulty Level : Medium

# Q 1 : make a list of 10 integers and take a number from user and see if that exists or not 
li = [10,465,78,94,53,48,12,47,66,35]
user = int(input('Enter the number you want to check in the list:'))
flag = 0
for i in range(len(li)):
    if user == li[i]:
        print('Yes the number exists.')
        flag = 1
if flag == 0:
    print('No the number doesnt exists.')

# Q2 : make 3 list of 5 numbers and check which one is the largest
list1 = [1,2,3,4,5]
list2 = [11,12,13,14,15]
list3 = [21,22,23,24,25]

li1t = 0
li2t = 0
li3t = 0

for i in range(len(list1)):
    li1t += list1[i] 
    li2t += list2[i] 
    li3t += list3[i] 
if li1t > li2t and li1t > li3t :
    print('List one is the largest')
    print(list1)
elif li2t > li1t and li2t > li3t :
    print('List 2 is the largest.')
    print(list2)
else:
    print('List 3 is the largest.')
    print(list3)

# Q 3 : take your name and reverse it 

name = input('Enter Your name :')
print(name[::-1])

# Q4 : store 3 marks in dic and print total and avg marks

dic = {
    'bio' : 69 ,
    'phy' : 81 ,
    'chem' : 65
}
total_marks = dic['bio'] + dic['phy'] + dic['chem']
avg = total_marks/3
print(f'Total Marks : {total_marks} \n Average : {avg}')

# Q5 : create a list of fruits and replace the second fruit with mango
fruits = ['Apple' , 'Banana' , 'Banana' , 'Pineapple' ,"Pear"]
fruits[1] = 'Mango'

print(fruits)


                    # Difficulty Level : Slighlty Cahllenging

# Q1 : take a sentence and count how many times each word appears
sentence = input('Enter a sentence :')
words = sentence.split()
words_count = {}

for word in words:
    words_count[word] = words_count.get(word,0)+1

print(words_count)

# Q 2 : remove duplicate without sets

list_with_dup = input('Enter a list of elements that contains duplicates and are seperated by spaces : ').split()
unique_list = []

for item in list_with_dup:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)

# Q3 : Take a number as input and Check if it's prime or not

def checkPrime(num) :
    flag = 0
    for i in range(num):
        if num % (i+1) == 0:
            flag += 1
    if flag == 2:
        print(f'{num} is a Prime Number')
    else:
        print(f'{num} is NOT a Prime Number')

prime = int(input('Enter a number :'))
checkPrime(prime) 


# Q4 : take marks of 5 subject and assign grade
total_m = 0
obtain_m = 0
for i in range(5):
    total_maarks = int(input(f'Enter the total marks of subejct {i+1} :'))
    obtained_marks = int(input(f'Enter the obtained marks of subejct {i+1} :'))
    total_m += total_maarks
    obtain_m += obtained_marks

percentage = (obtain_m/total_m) *100

if percentage >= 90 :
    print('A Grade')
elif percentage >= 80:
    print('B Grade')
elif percentage >= 70  :
    print('C Grade')
else :
    print('Fail')

# Q5 : take 2 numbers and ooeration from the user and print result

num1 = int(input('Enter num1 :'))
num2 = int(input('Enter num2 :'))
op = input('Enter The operation you want to perform (Enter +,-,*,/,//,%)')
if(op == '+'):
    print(f'{num1} + {num2} = {num1 + num2}')
elif(op == '-'):
    print(f'{num1} - {num2} = {num1 - num2}')
elif(op == '*'):
    print(f'{num1} * {num2} = {num1 * num2}')
elif(op == '/'):
    print(f'{num1} / {num2} = {num1 / num2}')
elif(op == '//'):
    print(f'{num1} // {num2} = {num1 // num2}')
elif(op == '%'):
    print(f'{num1} % {num2} = {num1 % num2}')






