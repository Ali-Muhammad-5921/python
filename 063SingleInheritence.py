class Animal :
    def __init__(self, name , speak):
        self.name = name
        self.speak = speak

    def __str__(self):
        return f'The Animal {self.name} makes {self.speak} sound'

class Cat(Animal):
    def __init__(self, name, speak,cn, owner):
        super().__init__(name, speak)  
        self.cn = cn
        self.owner = owner      

    def __call__(self):
        print( f'{self.cn} is a cat owned by {self.owner}')
    
a = Animal('Snow Owl','Hooting')
print(a)
c = Cat('Çat', "Meow" , 'Crookshanks','Hermoine Granger')
print(c)
c()