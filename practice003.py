from collections import Counter
import re

                # File Handling Pracitce

        # Easy Questions

# Q1: Read a text file and print its contents line by line.

with open('myfile.txt','r') as file :
    for line in file:
        print(line.strip())
    
# Q2 : Write a Python program to append a line to an existing text file without overwriting the previous content.

with open('myfile.txt','a') as file:
    file.write('\nI am currently reading the fifth book.')

# Q3 : Count total number of words in the text file.

with open('myfil.txt','r') as file :
    total_words  = file.read()
    total_words = total_words.split()
    print(f'The total number of words in the file are : {total_words}')


        # Medium Questions

# Q1 : Read a file and display only lines that contain a specific keyword (e.g., "Python").

keyword = 'Harry'
with open('myfile.txt','r') as f:
    for line in f:
        if keyword in line :
            print(line.strip())


# Q2 : Create a program that copies the content of one file to another.

with open('myfile.txt','r') as src , open('HarryPotter.txt' , 'w') as dest:
    for line in src:
        dest.write(line)


# Q3 : Read a file and replace every occurrence of a given word with another word, then save the result to a new file.

keyword = 'peach'
replacment = 'mango'

with open('myfile.txt','r') as f:
    content = f.read()

content = content.replace(keyword, replacment)

with open('myfile.txt','w') as f:
    f.write(content)

 
        # Slightly Challenging

# Q1: Create a program that reads a text file and counts how many times each word appears, then saves the results to another file.

with open('myfile.txt','r') as f :
    words = f.read().split()

words_count = Counter(words)

with open('wordcount.txt','w') as f:
    for word , count in words_count.items() :
        f.write(f'{word} : {count}\n')


# Q2: Implement a Python program that reads a file and removes all blank lines before saving the cleaned version to another file.

with open('myfile.txt','r') as f:
    lines = f.readlines()

with open('cleaned.txt','w') as f:
    for line in lines :
        if line.strip():
            f.write(line)

# Q3: Read a log file and extract all dates that match the format YYYY-MM-DD.
with open('file.txt', 'r') as f:
    content = f.read()

dates = re.findall(r"\d{4}-\d{2}-\d{2}",content)

print(dates)