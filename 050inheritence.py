class Employee:
    def __init__(self, name , subject):
        self.name = name
        self.subject = subject

    def info(self):
        print(f'{self.name}\'s favorite subject is {self.subject}')

class WitchesAndWizards(Employee):
    
    def show(self):
        print(f"{self.name} studies at Hogwarts ")

rw = WitchesAndWizards('Ron Weasley','Divination')
hp = WitchesAndWizards('Harry Potter', 'Defence Against the Dark Arts')
hg = WitchesAndWizards('Hermoine Granger' ,"Charms")
hp.info()
rw.info()
hg.info()
hp.show()
rw.show()
hg.show()
