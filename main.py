from googlesearch import search
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime


class Class:

    def __init__(self):
        pass

    def clean_url(self,url):
        url = url.lower()
        # preprocess the url
        counter = 0
        count_q = 0
        count_id = 0
        # Get the Unique URL AKA Package Name
        for word in url:
            if word == '/':
                self.x = counter
            counter += 1
        url = url[self.x+1:len(url)]
        # if ? and id both exist
        if '?' in url:
            if 'id' in url:
                for count,word in enumerate(url):
                    if word == '?':
                        if count_q == 0:
                            count_q = count
                    if word == 'id':
                        if count_id == 0:
                            count_id = count
                print(count_q,count_id)
                if count_q > count_id:
                    url = url[0:count_q]
                if count_id > count_q:
                    url = url[0:count_id]
            if 'id' not in url:
                for count,word in enumerate(url):
                    if word == '?':
                        if count_q == 0:
                            count_q = count
                url = url[0:count_q]
        # if only id exists
        if 'id' in url and '?' not in url:
            for count,word in enumerate(url):
                if word == 'i':
                    if url[count:count+2] == 'id':
                        if count_id == 0:
                            count_id = count
            print(count_id)
            url = url[0:count_id-1]

        # Clearing the data
        self.x = 0
        return url

    def get_body(self,url,agency): ## Travel Agency Name + Full Web URl
        web_page = requests.get(url)
        self.web_page = web_page.text
        print(self.web_page)
        url = self.clean_url(url)
        # Saving the data to file
        with open('./web_pages.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow([agency,url])


    def get_links(url,city_name):
        # Get links from the webpage
        web_page = requests.get(url)    



    def google_search(city_name,travel_agency_site_url):
        results = search(f"site:{travel_agency_site_url} {city_name} travel package")
        for count, result in enumerate(results):
            print(f"Indexing {result} -- Travel Agency :- {travel_agency_site_url}...")
        
    def clean(self):
        pass





if __name__ == '__main__':
    url = 'https://www.thomascook.in/holidays/international-tour-packages/dubai-tour-packages/dubai-september-special-buy-1-get-1-freepkgId=PKG006186&packageClassId=1&destination=PKG006186_dubai_CITY_1&destTag=United%20Arab%20Emirates'
    Class().get_body(url,'Thomas Cook')
