# msg = "I am {} and Im from {}"
# name = 'Ali Muhammad'
# country = 'Pakistan'

# print(msg.format(name , country))

msg = "I am {1} and I'm from {0}"
name = 'Ali Muhammad'
country = 'Pakistan'

# print(msg.format(country , name))
print(f"I am {name} and I'm fron {country}")
print(f"I am {{name}} and I'm fron {{country}}")

price = 49.099999
txt = f"for only {price : .3f}"
print(txt)
print(f'{2*30}')
print(type(f'{2*30}'))
