class NatureNumber:
    def __init__(self, num):
        self.num = num

    def getnum(self):
        return self.num

    def setnum(self, num):
        if num >= 0 and type(num) == int:
            self.num = num
        else:
            self.num = "자연수가 아닙니다"

currentNum = NatureNumber(4)
print(currentNum.getnum())
currentNum.setnum(-1)
print(currentNum.getnum())
currentNum.setnum(0x10)
print(currentNum.getnum())