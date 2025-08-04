# super keyword is used to refer parent class from  a child class

class Pc :
    def pm (self):
        print('This is a method of parent class.')

class Cc(Pc):
    def p(self):
        print('This is a method of child class.')
        super().pm()

a = Cc()
a.p()