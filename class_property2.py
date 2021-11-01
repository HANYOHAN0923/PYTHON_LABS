class Date:
    def __init__(this, month):
        this.innerMonth = month
    
    @property
    def month(this):
        return this.innerMonth
    @month.setter
    def month(this, month):
        if 1 <= month <= 12:
            this.innerMonth = month

today = Date(8)
today.month = 15
print(today.month)