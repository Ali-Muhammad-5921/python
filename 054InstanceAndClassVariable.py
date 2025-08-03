class Students:
    school = 'Hogwarts School of Witchcraft and Wizardry' # This is class variable
    def __init__(self,name):
        self.name = name # This is instance variable

    def info(self):
        print(f'{self.name} studies in {self.school}')

hp = Students('Harry Potter')
rw = Students('Ronald Weasley')
hg = Students('Hermoine Granger')

hp.info()
rw.info()
hg.info()
        
