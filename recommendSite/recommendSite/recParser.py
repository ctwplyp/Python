import urllib
import urllib2
from bs4 import BeautifulSoup
import re
from threading import Thread

def parse(n):
    url='https://www.yelp.com/search?find_loc=New+York,+NY&start=0&cflt=pizza'
    url2='https://www.yelp.com/search?find_desc=pizza&find_loc=New+York%2C+NY&ns=1'

    page = urllib2.urlopen(url2)
    soup =  BeautifulSoup(page.text, 'html.parser')


    desc = soup.findAll(attrs={"name": re.compile(r"description", re.I)})
    names = desc[0]['content'].encode('utf-8').decode().split("-")[1].split(",")
parse(60)
