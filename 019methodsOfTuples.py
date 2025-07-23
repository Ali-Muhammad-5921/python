# tuples can not be changed directly

hpCharacters = ("Harry Potter","Ron Weasley","Hermoine Garanger","Sirius Black","Remus Lupin","Dusley")
temp = list(hpCharacters)
temp.append("Snape")
temp.pop(5)
hpCharacters = tuple(temp)
print(hpCharacters)

tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = tup1 + tup2

print(tup3)
tup3.count(1)
tup3.index(5 ,2 , 4) # yeh btaye ga k 2nd sy 4th tk phla 5 kis index pr hy 
print(len(hpCharacters))