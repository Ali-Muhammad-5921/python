class Person:
    def __init__(self , name ,residence , pet  , petName):
        self.name = name 
        self.residence = residence
        self.petName = petName
        self.pet = pet

    def info(self):
        print(f'{self.name} lives at {self.residence} , has a pet {self.pet} called {self.petName}')

h = Person('Harry Potter', '4 - Privet Drive' , 'Owl' , 'Hedwig')
r = Person('Ron Weasley', 'The Burrow' , 'Fat Rat' , 'Scabbers')
her = Person('Hermoine Granger', 'Somewhere in the UK' , 'Cat' , 'Crookshanks')

h.info()
r.info()
her.info()