#local variable
#kim(), han()의 info는 이름만 같은 두개의 다른 지역변수이다.

def kim():
    info = "chaewon Kim"
    return info

def han():
    info_name = "yohan Han"
    return info_name


#global variable
price = 1000

def sale():
    global price
    price = 500


sale() #이 부분을 주석처리하면 1000이 출력됨

print(price)