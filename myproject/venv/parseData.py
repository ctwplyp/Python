import bs4 #importing soup
from urllib.request import urlopen as url #importing urllib for url request
from bs4 import BeautifulSoup as soup
import pandas as pd
import json

class Review:
    def __init__(self, descr, rating, review_dt):
        self.descr = descr
        self.rating = rating
        self.review_dt = review_dt
def getAllPages():
    pizza_url ="https://www.yelp.com/search?find_desc=pizza&find_loc=New+York+NY&ns=1"
    request=url(pizza_url)
    htmlscrap=request.read()
    request.close
    page_soup=soup(htmlscrap,"html.parser")#parsing as html
    #review_counter=i.findAll("li",{"class":"review-count responsive-small-display-inline-block"})
 
    body = page_soup.findAll("h3",{"class":"search-result-title"})
    pageRef={}
    for i in range(1, len(body)): #Skipping the first record
        body1 = body[i].findAll("a", {"class":"biz-name js-analytics-click"})
        name=body1[0].find("span")
        href=body1[0]["href"]
      #  print(body1)
        name_val = name.string
      #  name = name.text.replace("</span>","")
      #  print(href)
      #  print(name_val)
        pageRef[href] =name_val
        for p in pageRef:
            print(p)


def parseReviews(review_count):
    x=0
    filename="datasets.csv" #saving data as csv
    f=open(filename,"w")
    headers="Name,Friend Count,Photo Count,Review Count,Elite Member,Funny Count,Cool Count,Useful Count,Review Length,Checkin Count\n" #these are the features that are scraped 
    f.write(headers)
    total_rev_rating = 0
    for count in range(review_count): #regex could have been used here but this is to increment the url page(keeping it simple.)
        my_url="https://www.yelp.com/biz/julianas-pizza-brooklyn-5?o?sort_by=date_desc"
        request=url(my_url)#taking url as a paramter
        htmlscrap=request.read()
        request.close()
        page_soup=soup(htmlscrap,"html.parser")#parsing as html
        body_t = page_soup.findAll("script",{"type":"application/ld+json"})
        body_text =body_t[0].text
        json1_data =json.loads(body_text)
        json_reviews1 = json1_data['review'][count]
        rating = json_reviews1['reviewRating']
        rating_value = rating['ratingValue']
        description = json_reviews1['description']
        date = json_reviews1['datePublished']
        reviewTemp = Review(description, rating_value, date)
        total_rev_rating=total_rev_rating + rating_value
        #print(rating_value)
    average = total_rev_rating / review_count
    print(average)
       # print(ratingValue)
       # print(description)
       # print(reviewTemp.descr)
        #urls = [el['url'] for el in json.loads(body_t.text)['itemListElement']]

        #cprint(urls)
           
        #print(type(body_t))
    f.close()
#parseReviews(3)
getAllPages()