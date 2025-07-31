def greet(fx):
    #def mfx(*args , **kwargs): *args sub arguments ko lene ka tareeka hy as a tuple and **kwargs tareeka hy dictionary ko leny ka 
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this Function")
    return mfx

@greet
def hw():
    print("Hello World")

def add (a , b):
    print(a+b)

hw()
greet(add)(1,2)
