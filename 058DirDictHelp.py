# in python dir and dict and help are the methods that can help us to understand an unknown class and objects.

class ABC :
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = ABC('Harry Potter', 14)
print(p.__dict__) # it gives all the attributes of this class as a dictionary





# x = [1,2,3]
# print(dir(x)) # this gives a list of methods that can be performed on it.
# x = (1,2,3)
# print(dir(x)) 


# help function is used to get the help documentation of an object including it's attributes and methods.
print(help(ABC))
