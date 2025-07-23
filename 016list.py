l = [3,4,5,"Harry Potter ", True]
print(l)
print(type(l))

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])


# All 4 of these mean the same thing
print(l[-2])
# print(l(len(l)-2)) 
# print(l[5-2])
# print(l[3])

#it can work for all elements of the string
if "Harry Potter " in l : #yeh harry potter k bad wali space bhi matter krti hy
    print("yes")
else:
    print("no")

print(l)
print(l[:])
print(l[1:-1])
print(l[1:-1:2])
