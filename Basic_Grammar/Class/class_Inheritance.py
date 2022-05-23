#상속은 기존 클래스를 확장하여 멤버를 추가하거나 동작을 변경하기 위해 사용하는 방법이다.
#따라서 빗긋한 클래스가 있다면 처으부터 다시 만들 필요 없이 상속받아 수정해서 사용이 가능하다.
#새로 정의되는 자식 클래스는 부모 클래스의 모든 멤버를 물려받는다.

'''
class ClassName(ClassParents):
    ```
'''

class PersonalInfo:
    def __init__(this, name, age, nationality):
        this.name = name
        this.age = age
        this.nationality = nationality

    def info(this):
        print(this.name + "은 " + str(this.age) +"살 " + this.nationality+"인입니다.")

    def test():
        print("test")

class ExtensionPersonalInfo(PersonalInfo):
    def __init__(this, name, age, nationality, groupName):
        super().__init__(name,age,nationality)
        this.groupName = groupName

    def info(this):
        super().info()
        print("소속된 그룹이름은 " + this.groupName + "입니다.")

    '''
    def info(this):
        print("%d살 %s입니다."%(this.age, this.name))
    '''

    def songList(this):
        print("라면과 공구탄, 비눗방울, 얼음별 대모험 ...")



kim = PersonalInfo("김채원",22,"한국")
kim.info()
jo = ExtensionPersonalInfo("조유리",21,"한국","IZ*ONE")
jo.info()
jo.songList()

#자식 클래스에서 부모의 메서드를 호출할 때는 super() 메서드로 부모를 구해 호출한다
#Extension~의 __init__는 인수로 전달 받은 나이와 이름을 초기화하기 위해 부모의 생성자인 super().init__를 호출한다
#그치만 이렇게 하면 부모가 변경될 때 자식 또한 같이 수정되는 불편함이 있다
#Extension~의 info()메서드처럼 부모의 동작을 Override하여 사용할 수도 있으며 부모의 메서드를 사용하지 않고 완전히 다르게 작성할 수도 있다.
#자식 class가 또다른 class를 파생시킬 수도 있음