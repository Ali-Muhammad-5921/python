class Person:
    name = 'Harry Potter'
    age = 13
    book = 'Prisoner of Azkaban'
    school = 'Hogwarts school of witchcraft and wizardry'
    def info(self): # self ka mtlb woh object jis k liye method call kiya ja rha hy
        print(f'{self.name} is a studendt of {self.school}')

a = Person()

a.info()

a.name = 'Ron Weasley'
a.info()

a.name = 'Hermoine Granger'
a.info()