#default argument
def sumCounter(begin, end, step = 1):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum

print("1 ~ 100 =", sumCounter(1, 100)) #step = 1 default***
print("1 ~ 10 =", sumCounter(1, 10, 2))


# 기변 인수 *args(임의 개수의 인수를 받을 수 있음.)

#default intsum(s, *ints)
#error   intsum(*ints, s)
#error   intsum(*s, *ints)

def intsum(*ints):
    sum = 0
    for num in ints:
        sum += num
    return sum

print(intsum(1,2,3,4,5,6,7,8,9,10))


#키워드 인수 **kwargs 
def lol_tier(**kwargs):
    for dict, value in kwargs.items():
        print(dict,':',value,sep=' ')

lol_tier(username="JohnHan",tier="iron4",lp="24lp")

#unpacking
x = {"username":"hide on bush","tier":"challenger"}
lol_tier(**x)


#키워드 가변 인수
def calcscore(name, *score, **option):
    print(name)

    sum = 0
    for s in score:
        sum += s
    print("Total :", sum)

    if (option['avg'] == True):
        print("average :", sum / len(score))

calcscore("테스트", 39, 19, 83, avg = False)
calcscore("한요한", 100, 100, 100, 100, avg = True)
calcscore("김채원", 50, 27, 53 , 64, avg = True)