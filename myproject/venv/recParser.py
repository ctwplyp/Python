from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
from threading import Thread

def parse(n):
    url='https://www.yelp.com/search?find_loc=New+York,+NY&start=0&cflt=pizza'
    url2='https://www.yelp.com/search?find_desc=pizza&find_loc=New+York%2C+NY&ns=1'
    url3 ='https://www.yelp.com/biz/julianas-pizza-brooklyn-5'

    page = requests.get(url3)
    soup =  BeautifulSoup(page.text, 'html.parser')

    filename="datasets.csv" #saving data as csv
    f=open(filename,"w")
    headers="Name,Friend Count,Photo Count,Review Count,Elite Member,Funny Count,Cool Count,Useful Count,Review Length,Checkin Count\n" #these are the features that are scraped 
    f.write(headers)

    container=soup.findAll("div",{"class":"review review--with-sidebar"})#the class name where all the features are contained
    #print(len(container))
    
    for i in container:

        #print(containers)
      #  friend_counter=i.findAll("li",{"class":"friend-count responsive-small-display-inline-block"})
     #  friend_count=friend_counter[0].b.text
     #   review_counter=i.findAll("li",{"class":"review-count responsive-small-display-inline-block"})
      #  review_count=review_counter[0].b.text
    #    photo_counter=i.findAll("li",{"class":"photo-count responsive-small-display-inline-block"})
        
      #  if photo_counter:
      #      photo_count=photo_counter[0].b.text
      #  else:
      #      photo_count=0
     #   elite_counter=i.findAll("li",{"class":"is-elite responsive-small-display-inline-block"})
     #   if elite_counter:
     #       elite_count=1
     #   else:
      #      elite_count=0
     #  funny_counter=i.findAll("a",{"class":"ybtn ybtn--small funny js-analytics-click"})
     #   funny_count1=funny_counter[0].findAll("span",{"class":"count"})
     #   funny_count=funny_count1[0].text
     #   if funny_count:
    #        funny_count=funny_count
     #   else:
      #      funny_count=0
     #  cool_counter=i.findAll("a",{"class":"ybtn ybtn--small cool js-analytics-click"})
      #  cool_count1=cool_counter[0].findAll("span",{"class":"count"})
     #   cool_count=cool_count1[0].text
     #   if cool_count:
     #       cool_count=cool_count
      #  else:
     #       cool_count=0
      #  useful_counter=i.findAll("a",{"class":"ybtn ybtn--small useful js-analytics-click"})
     #  useful_count1=useful_counter[0].findAll("span",{"class":"count"})
      #  useful_count=useful_count1[0].text
      #  if useful_count:
     #       useful_count=useful_count
     #  else:
      #      useful_count=0
     #  user_counter=i.findAll("a",{"class":"user-display-name js-analytics-click"})
      #  user_count=user_counter[0].text
      #  rating_counter=i.findAll("div",{"class":"biz-rating biz-rating-large clearfix"})
      #  rating_count=rating_counter[0].div.div["title"]
      #  rating_count=(int(rating_count[0]))

      #  length_counter=i.findAll("p",{"lang":"en"})
      #  xx=str(length_counter[0])
     #   length_count=len(xx)
        #print(length_count)

      #  checkin_counter=i.findAll("li",{"class":"review-tags_item"})
      #  if checkin_counter:
      #      var1=checkin_counter[0].text.strip()
      #      checkin_count=(int(var1[0]))
      #  else:
      #      checkin_count=0

        rating =i.findAll("div",{"class":"review-content"})
        print(rating)
      #  f.write(str(user_count) + "," + str(friend_count) + "," + str(photo_count) + "," + str(review_count)+","+str(elite_count)+","+str(funny_count)+","+str(cool_count)+","+str(useful_count)+","+str(length_count)+","+str(checkin_count) +"\n")

   # x=x+20
    f.close()

    #3150
    #3264
 #  desc = soup.findAll(attrs={"name": re.compile(r"description", re.I)})
#    names = desc[0]['content'].encode('utf-8').decode().split("-")[1].split(",")
#    print(names)

parse(1)
