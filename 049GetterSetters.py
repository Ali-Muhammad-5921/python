class MYclass:
    def __init__(self , value):
        self._value = value

    @property # @property makes a getter and a getter behaves as a property
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter # tis is used to set values 
    def ten_value(self, new_val):
        self._value = new_val

a = MYclass(10)

a.ten_value = 25

print(a.ten_value)
    
