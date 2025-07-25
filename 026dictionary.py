dic = {
    'name' : 'Harry Potter',
    'loc' : 'Privet Drive',
    'school' : 'Hogwarts',
    "pet" : 'Hedwig'
}
print(dic['name'])
#print(dic.get('name')) yeh bilkul uper wali line ka kaam krti hy lekin agr koi esi key dhoond rhy ho jo k nhi hy to phr uper wali error de gi or nechy wali none print kry gi
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

for key,value in dic.items() :
    print(f'The value of {key} is {value}' )


