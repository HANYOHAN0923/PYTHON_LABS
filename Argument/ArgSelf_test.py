class SirenOrder:
    def __init__(self, nickname, menu):
        self.userNickname = nickname
        self.chooseMenu = menu

    def notice(self):
        print("%s님 주문하신 %s 나왔습니다"%(self.userNickname, self.chooseMenu))

    def thx(self):
        print("감사합니다, 다음에 또 방문해주세요!")

johnHan = SirenOrder("짱구는목말러", "자몽허니블랙티")
johnHan.notice()
johnHan.thx()