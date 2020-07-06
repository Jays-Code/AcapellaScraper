from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
from flask import Flask
import lxml


app = Flask(__name__)

chrome_path = r"C:\Users\Jay\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.get("https://www.youtube.com/results?search_query=isolated+vocals+acapella")
pageContent = driver.page_source
'''
driver.close()
'''


base = "https://www.youtube.com/results?search_query="

qstring = "isolated+vocals+acapella"


'''
base = "https://www.t"
qstring = "witter.com"
'''

r = requests.get(base+qstring)

page = r.text
soup = bs(pageContent, 'lxml')






vids = soup.findAll('a',attrs={'id':'video-title'})
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)


    

@app.route('/')
def listResults():
    print(vids)
    
    return(pageContent)
    


    

'''
should return soup but that gives error: return(soup)
'''
'''
example url for reference: https://www.youtube.com/watch?v=eB0nUzAI7M8
'''



'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
driver = webdriver.Firefox(executable_path="/home/rishabh/Documents/pythonProjects/webScarapping/geckodriver")
driver.get('https://www.youtube.com/feed/trending')
content = driver.page_source
driver.close()

soup = BeautifulSoup(content, 'html.parser')
#Do whatever you want with it
'''