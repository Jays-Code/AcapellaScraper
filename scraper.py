from bs4 import BeautifulSoup as bs
import requests
from flask import Flask

app = Flask(__name__)


base = "https://www.youtube.com/results?search_query="

qstring = "isolated+vocals+acapella"

r = requests.get(base+qstring)

page = r.text
soup = bs(page, 'html.parser')






vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)
    

@app.route('/')
def listResults():
    return(page)

'''
should return soup but that gives error: return(soup)
'''
