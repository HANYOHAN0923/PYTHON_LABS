import datetime


#sep(separation)
print("S","A","P", sep=" ")


#end(1)
print("Kim", end="")
print("chaewon")


#end(2)
print("Kimchae", end="chae")
print("won")

#format(1) - {num}
year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day

str_year = str(datetime.date.today().year)
str_month = str(datetime.date.today().month)
str_day = str(datetime.date.today().day)

print("오늘은 "+str_year+"년 "+str_month+"월 "+str_day+"일 "+"입니다.")
print("오늘은 {0}년 {1}월 {2}일 입니다.".format(year, month, day))
print("오늘은 %d년 %d월 %d일 입니다."%(year, month, day))

#format(2) - %symbol
# %s : string
# %d : integer
# %f : float
print("%s의 정답은 %d번입니다."%("이번 문제", 3))



#escape
# \n 줄바꿈
print ("줄바꿈\n꿈바줄")
# \t TAB
print("TAB\t탭")
# \\ '\'
print("C:\\user\\desktop\\PYTHON_LABS")
# \' 작은따옴표
print("\'그만큼 작은따옴표가 나오고 싶다는 소리지\'")
# \" 큰따옴표
print("\"그만큼 큰따옴표가 나오고 싶다는 소리지\"")
# \b 백스페이스(delete)
print("안녕 \b하세요")