'''
class ClassName:
    def __init__(this, initial value):
        member(variable initialization)
    define method
'''
class PersonalInfo:
    def __init__(this, name, age, nationality):
        this.name = name
        this.age = age
        this.nationality = nationality


        #첫번째 메서드 __init__ 생성자는 객체를 초기화 한다. 앞뒤로 밑줄 대 가가 있는 메서드를 특수 메서드라고 하는데 용도와 이름이 미리 정해져있다
        #첫번째 인수는 자기 자신을 의미하는 this, 참조시 this.멤버 구문을 사용한다.
        #this 나머지 인수로 멤버의 초기 값을 전달받아 대입한다. 파이썬은 변수를 선언하는 문법이 없어서 따로 멤버 변수를 선언하지 않고 대신 __init__에서 초기값을 받아 대입하는 형식으로 멤버를 생성한다.
        #따라서 생자에서 this.멤버 = 초기값 형식으로 대입하면 클래스의 멤버변수ㅠ가 된다.


    def info(this):
        print(this.name + "은 " + str(this.age) +"살 " + this.nationality+"인입니다.")




#객체 생성 방법: 객체 = ClassName(Arguments...)
'''
객체를 먼저 생성 후 이 객체를 생성자인 __init__의 첫 번째 인수 self로 전달하고 생성문에서 전달한 인수는 두 번째 이후의 인수로 전달되어 새로 생성되는 객체의 맴버에 대입된다.
즉
kim = PersonalInfo(22,"김채원")
__init__(this,age,name):
kim = this
22 = age
name = 김채원
__init__생성자는 객체 생성 직후에 호출되어 멤버를 초기화하는 역할을 담당한다
따라서 kim.info()와 PeronsonInfo.info(kim)은 같은 문장이다
'''
kim = PersonalInfo("김채원",22,"한국")
kim.info()
PersonalInfo.info(kim)
jo = PersonalInfo("조유리",21,"한국")
jo.info()

#class를 구성하는 변수와 함수를 합쳐 멤버라고 통칭한다
#class에 소속된 함수를 특별히 메서드라고 부른다

