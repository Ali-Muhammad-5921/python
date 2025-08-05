class Person:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def show(Self):
        return f'{Self.name}\'s age is {Self.age}'

class Student(Person):
    def __init__(self, name, age,sports):
        super().__init__(name, age)
        self.sports = sports

    def show(self):
        return f"{super().show()} and play's {self.sports}"

class Pet(Student):
    def __init__(self, name, age, sports,pet):
        super().__init__(name, age, sports)
        self.pet = pet

    def show(self):
        return f"{super().show()} and has a pet called {self.pet}"

hp = Pet('Harry Potter' , 14 , 'Quidich', 'Hedwig')
print(hp.show())