'''
result: https://imgur.com/Nh7nkjF

Condition1: 리스트에 국가 이름과 "국가 부호 코드(Alpha-3 code)"를 저장하세요. !
Condition2: 몇몇의 나라들은 통화 코드를 가지고 있지 않습니다. ( No universal currency 라고 표기되어 있음) 이러한 경우에는 리스트에 추가하지 마세요. !
Condition3: 사용자의 입력을 확인하여 그 입력 값이 국가 목록에 해당하는 숫자 범위면 프로그램이 동작하고 그 외의 값들은 동작하지 않습니다.
Condition4: 국가를 선택하면 국가 이름과 통화 코드를 표시해줍니다.
'''

'''
Separating td:
데이터가 총 1072개가 잡힐거에요. 그걸 4로 나누면 268개 일겁니다. nameOfCountry = country_list[a*4].text.replace(" ","")
  numOfCountry = country_list[3+a*4].text 이런식으로 저는 나눴습니다.
'''

import os
import requests
from bs4 import BeautifulSoup

os.system("cls") #clear?
URL = "https://www.iban.com/currency-codes"

count_country = 0
country_name_list = []
country_code_list = []

def extract_iban_pages():
    result = requests.get(URL)
    
    soup = BeautifulSoup(result.text,"html.parser")
    
    trs = soup.find_all('tr')

    global count_country, country_code_list, country_name_list
    
    for idx, tr in enumerate(trs):
        if idx > 0:
            tds = tr.find_all('td')
            country_name = tds[0].text.capitalize()
            country_currency = tds[1].text
            country_code = tds[2].text
            
            if country_currency != "No universal currency":
                count_country += 1
                country_name_list.append(country_name)
                country_code_list.append(country_code)
            else:
                pass
    
    return country_name_list, country_code_list
    

def user_input():

    global count_country
    global country_dictionary
    global currency_code_dictionary

    try:
        selected_num = int(input("#:"))

        if 0 <= selected_num <= count_country:
            print(f'You choose {country_dictionary[selected_num]}')
            print(f'The currency code is {currency_code_dictionary[selected_num]}')
        else:
            print("Choose a number from the list.")
            user_input()

    except:
        print("That wasn't a number.")
        user_input()


extract_iban_pages()
print("Hello! Please choose select a country by number: ")

enu_country_code_list = enumerate(country_code_list)
enu_country_name_list = enumerate(country_name_list)
country_dictionary = {}
currency_code_dictionary = {}

for idx, country_currency_code in enu_country_code_list:
    currency_code_dictionary[idx] = country_currency_code

for idx, country_name in enu_country_name_list:
    print(f'#{idx} {country_name}')
    country_dictionary[idx] = country_name

user_input()