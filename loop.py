# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:47:29 2020

@author: Arif Darmawan
"""
from bs4 import BeautifulSoup as soup
from headers import hd
from scrap import main
import requests
import re

headers = hd()

url = 'https://weborder.id/pbs/Store/StoreMainController'

response = requests.get(url, headers=headers)
page_soup = soup(response.text, "html.parser")
list_pub = page_soup.find_all("ul",{"class":"dropdown-menu"})[3]

temp = list_pub.find_all('a')

f_bukalapak = open("bukalapak20200524.csv", "w")

for i in range(0, len(temp)):
    penerbit = temp[i].text
    penerbit = re.sub(' +', ' ', penerbit)
    url = temp[i].get('href')
    print(penerbit)
    
    while True:
        response = requests.get(url, headers=headers)
           
        main(response, f_bukalapak, penerbit)
        
        page_soup = soup(response.text, "html.parser")
        next_page = page_soup.findAll("li",{"class":"next page"})
        if next_page: 
            link = next_page[0].find_all('a')[0].get('href')
            url = link
        else:
            break
        
f_bukalapak.close()