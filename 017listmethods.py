l = [0,1,2,45,94,0,10,25,0,45]

print(l)
l.append(15) # end pr add krna
l.sort() # accessinding order
l.sort(reverse=True) # descending order
l.reverse() # list to ulta kr dy ga
print(l.index[6]) # returns first  index of accurence  
print(l.count(1)) # no of occurences
#m = l # dono lists change hongi
# m = l.copy()
# m[0] = 5 
# print(l)

# l.insert(1,4) # insert 4 at index 1 

m = [10 , 25 , 100]
a = l+m

l.extend(m)


