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
    print(videolist)
    
    return str(videolist)
    

''' FOR PRINTING LIST TO DOWNLOAD MANUALLY
now that your results are being printed using the 'vids' variable, include some lines of code 
that will make a list of the hrefs and vid titles and save it under queryResults variable
(issue still persists with page/hits not fully loading; why?)
'''


''' FOR DOWNLOADING AUTOMATICALLY
options for mp3 encoding: 
https://stackoverflow.com/questions/47420304/download-video-in-mp3-format-using-pytube
'''