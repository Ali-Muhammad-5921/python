# list change ho skti hy lekin tuples change nhi hoti

tup = (10,25)
print(type(tup),tup)

# tup = (10)  iski type int hy agr tuple banani hy to tup = (10,) comma lagana hoga

print(tup[0])
print(tup[-1])
if 10 in tup:
    print("yes")

tup1 = ("Harry Potter" , "Ron Weasley", "Hermoine Granger" , "Sirius Black" ,"Remus Lupin")
tup2 = tup1[1:4]
print(tup2)