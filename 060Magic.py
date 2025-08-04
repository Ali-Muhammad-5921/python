# the methods that start from __ and end with __ are called dunder or magic mehtods.

class A:
    def __init__(self):
        self.name = 'Harry Potter'
        self.age = 14

    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i
    def __call__(self, *args, **kwds):
        print(self.__dict__)
        print(dir(A))
    
a = A()
print(a.name)
print(len(a))
a()