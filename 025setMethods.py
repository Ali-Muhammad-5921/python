s1 = {15,24,26,35,95,57,13}
s2 = {51,24,26,7,5,85,57,46,64}

s1.add(25)
s2.remove(24)
item = s1.pop()

print(item)

print(s1.union(s2))
print(s1.intersection(s2))

# s1.intersection_update(s2)
#s1.update(s2) # updates s1 with the values of s2 
print(s1,s2)

# symmetric difference includes the non common values 
print(s1.symmetric_difference(s2))

# difference means A - B
print(s1.difference(s2))

#disjoint sets have nothing in common
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))

# to delete entire sets
del s1 
# to clear a set
s2.clear()
print(s2)

 