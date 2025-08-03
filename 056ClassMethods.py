class Students:
    school = 'Hogwarts School of Witchcraft and Wizardry' # This is class variable
    def __init__(self,name):
        self.name = name # This is instance variable

    def info(self):
        print(f'{self.name} studies in {self.school}')

    @classmethod
    def changeSchool(self, newSchool):
        self.school = newSchool

hp = Students('Harry Potter')
rw = Students('Ronald Weasley')
hg = Students('Hermoine Granger')

hp.info()
rw.info()
hg.info()

dm = Students('Drace Malfoy')
dm.changeSchool("Dumstrang")
print(Students.school)        
