from bs4 import BeautifulSoup as bs
import requests
from flask import Flask
import lxml


app = Flask(__name__)


base = "https://www.youtube.com/results?search_query="

qstring = "isolated+vocals+acapella"


'''
base = "https://www.t"
qstring = "witter.com"
'''

r = requests.get(base+qstring)

page = r.text
soup = bs(page, 'lxml')






vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)


    

@app.route('/')
def listResults():
    print(vids)
    return(page)


    

'''
should return soup but that gives error: return(soup)
'''
'''
example url for reference: https://www.youtube.com/watch?v=eB0nUzAI7M8
'''
