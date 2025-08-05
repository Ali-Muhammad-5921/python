class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def show(self):
        print(f'{self.name}\'s age is {self.age}')

class Player:
    def __init__(self,name, sports):
        self.name = name
        self.sports = sports

    def show(self):
        print(f'{self.name} plays {self.sports}')

#class PP(Player,Person):
class PP(Person,Player):
    def __init__(self, name, age,sports):
        self.name = name
        self.age = age
        self.sports = sports

a = Person('Dumbledor','89')
b = Player('Wood', 'Quidich')
c = PP('Harry ', 14 , 'Quidich')
c.show()
print(PP.mro())