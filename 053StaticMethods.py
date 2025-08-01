class Math:
    def __init__(self):
        self.num = 5

    @staticmethod
    def add(a,b): # jb static method banaty hain to self nhi likhty q k static method kisi class sy asociated nhi hoty
        print(a+b)

a = Math()

print(a.add(10 , 25))# as add method does'nt return anything so none is printed
