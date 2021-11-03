class NatureNum:
    def __init__(self, num):
        self.innnerNum = num

    @property
    def num_value(self):
        return self.innnerNum
    
    @num_value.setter
    def num_value(self, num):
        if type(num) == int and num >= 0:
            self.innnerNum = num


num1 = NatureNum(8)
print(num1.num_value)
num1.num_value = 16
print(num1.num_value)