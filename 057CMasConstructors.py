class Abc:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet
    
    def info(self):
        print(f'{self.name}\'s pet is {self.pet}')

    @classmethod 
    def fromStr(clas , string):
        return clas(string.split('-')[0],string.split('-')[1])

hp = Abc.fromStr('Harry Potter-Hedwig')
hp.info()