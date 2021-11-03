class NatureNumber:
    def __init__(self, num):
        self.innerNum = num

    def getnum(self):
        return self.innerNum

    def setnum(self, num):
        if num >= 0 and type(num) == int:
            self.innerNum = num
        else:
            self.innerNum = "자연수가 아닙니다"
    
    num_prop = property(getnum, setnum)

currentNum = NatureNumber(4)
print(currentNum.num_prop)
currentNum.num_prop = -1
print(currentNum.num_prop)
currentNum.num_prop = 0x10
print(currentNum.num_prop)