import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

#사이트 페이지 개수 가져오기
def extract_indeed_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div",{"class":"pagination"})

    links = pagination.find_all('a')

    pages = []
    for link in links[:-1]: #pages list에 마지막 원소를 제외(마지막 원소가 next버튼이여서)
        #pages.append(link.find("span").string)
        pages.append(int(link.string)) #위에 구문과 같은 결과가 나오는 이유가 <a>테그 안에 텍스트가 하나만 존재해서

    last_page = pages[-1]
    return last_page

#위의 함수를 기초로 하여, 각 페이지마다 접근하여 정보 가져오기
def extract_indeed_jobs(last_page):
    for page in range(last_page):
        page_list = requests.get(f'{URL}&start={page*LIMIT}')
        print(page_list.status_code)