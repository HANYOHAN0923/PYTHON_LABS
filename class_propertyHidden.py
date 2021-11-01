class Date:
    def __init__(this, month):
        this.__month = month
    
    def getmonth(this):
        return this.__month
    def setmonth(this, month):
        if 1 <= month <= 12:
            this.__month = month
    month = property(getmonth, setmonth)

today = Date(8)
today.__month = 15
print(today.month)

'''
___가 붙으면 내부적인 실제 이름을 _className__MemberName으로 복잡하게 만든다.
즉 __month는 _Date__month가 된다.
'''