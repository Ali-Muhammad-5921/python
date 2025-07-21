hp = "Harry Potter" # Strings are immutable
a = "!!! abc !!!!"


print(len(hp))
print(hp.upper())
print(hp.lower())
print(a.rstrip("!"))
print(a.replace("abc" , "Luffy"))
print(a.split(" ")) # this will make a list from string on the basis of space


blogHeading = "introduction tO pytHOn"

print(blogHeading.capitalize())
wel = "Welcome to Hogwarts :)"
print(wel.center(50))


print(wel.count("o"))
print(wel.endswith(":)"))
print(wel.endswith("e",0,7))
print(wel.find("to")) # returns 1st occurence -1 if isn't present

print(wel.isalnum()) # returns true if string consists of A-Z a-z 0-9 else false
print(wel.isalpha()) # returns true if string consists of A-Z a-z else false
print(wel.islower()) #returns true if all characters are lower case else false
print(wel.isprintable()) # returns true if all characters are printable  else false

