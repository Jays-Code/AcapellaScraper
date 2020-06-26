from bs4 import BeautifulSoup as bs
import requests


base = "https://www.youtube.com/results?search_query="

qstring = "isolated+vocals+acapella"

r = requests.get(base+qstring)

page = r.text
soup = bs(page, 'html.parser')

print(bs)

