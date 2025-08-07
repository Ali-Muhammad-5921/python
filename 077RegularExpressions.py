import re # package for regular expressions

# pattern = r'[A-Z]ogwarts'  plus tells us more than one occurence
pattern = r'[A-Z]+ogwarts' 
text = '''
Harry Potter studies at hogwarts
Ron Weasley studies at hogwarts
Hermoine Granger studies at hogwarts
Dumbledore teaches at Hogwarts
Dog in Dogwarts
'''

# match = re.search(pattern, text) it gives only 1st occurence
match = re.finditer(pattern,text)
for m in match:
    print(m)
    print(m.span())
    print(type(m.span()))
    print(text[m.span()[0]:m.span()[1]])

# docs.python.org here is the documentation for regular expression
# regexr.com see the cheatsheet here 