dic = {
    'name' : 'Harry Potter',
    'loc' : 'Privet Drive',
    'school' : 'Hogwarts',
    "pet" : 'Hedwig'
}
dic2 = {
    'name' : 'Ron Weasley',
    'loc' : 'The Burrow',
    "pet" : 'Scabbers'
}
dic2.pop('pet') # pop item last item ko remove krta hy we can also use del dic2['pet']
dic.update(dic2)
print(dic)
dic.clear()
print(dic)
print(dic2)
# we can delete entire dictionary by del keyword