'''
Documentation:https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''
from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

extract_indeed_jobs(last_indeed_page)

print(last_indeed_page)