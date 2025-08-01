# Access Modifiers mean public , private and protected variables by default the variables are public.
# Public variables mean class k bahir sy access kiye ja skty hain.
# self.variable_name means a public variable.
# self.__variable_name means a private variable.
# self._variable_name means a protected variable.
#Protected class or sub classes ma access kiye ja skty hain.

# Python does'nt provide any protection to any variable this is all just an convention and it can change depending on where we work.
# The only thing is we can not directly access the varialbe with __.

class Abx:

    def __init__(self,name,pet):
        self.__name = name
        self._pet = pet

class Abc:
    pass

a = Abx('Harry Potter',"Hedwig")
b = Abc()
#print(a.__name) This gives error 
# print(a._Abx__name)# This is indirect access of private varible called Name Mangling
# print(a.__dir__)
# print(a.__dir__())

