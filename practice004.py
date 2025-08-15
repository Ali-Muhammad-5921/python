import csv

                    # CSV Handling Practice Questions
        
        # Easy

# Q1: Read a CSV file containing student names and marks, and print all the rows.

with open('marks.txt', 'r') as f :
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Q2: Write a CSV file with three columns: Product, Price, and Quantity. Add 5 sample products.

data = [
    ["Product", "Price", "Quantity"],
    ["Pen", 20, 50],
    ["Notebook", 50, 30],
    ["Pencil", 10, 100],
    ["Eraser", 5, 80],
    ["Marker", 25, 40]
]
with open('products.txt','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Q3: Read a CSV file and print only the first column values.

with open('file.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])

        # Medium

# Q1: Read a CSV file of employees and filter only those with a salary greater than 50,000.

with open('file.txt','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Salary'] > 50000):
            print(row)


# Q2: Write a program to add a new row to an existing CSV file without overwriting the data.

new = ['name',20,'grade']
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new)

# Q3: Read a CSV file and convert its data into a list of dictionaries.

with open('file.txt', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(data)

        # Slightly Challenging

# Q1: Read a CSV file and sort the rows based on a given column (e.g., Age).

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    sort = sorted(reader, key=lambda x: int(x['Age']))

with open('sorted.csv','w',newline='') as f:
    writer = csv.DictWriter(f,fieldNames=['Name','Age','Grade'])
    writer.writeheader()
    writer.writerows(sort)

# Q2: Merge two CSV files that have the same column headers into a single file.

with open("file1.csv", "r") as f1, open("file2.csv", "r") as f2:
    reader1 = list(csv.reader(f1))
    reader2 = list(csv.reader(f2))

merged = reader1 + reader2[1:]

with open('merged.csv','w') as f :
    writer = csv.writer(f)
    writer.writerows(merged)

# Q3: Read a CSV file and calculate the average of a numeric column (e.g., marks).

total = 0 
count = 0
with open('file.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader :
        total += int(row['Marks'])
        count += 1 

print('Average Marks :',total/count) 