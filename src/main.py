# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:47:29 2020

@author: Arif Darmawan
"""
from bs4 import BeautifulSoup as soup
from headers import hd
from scrap import scrap
import requests
import re

# headers = hd()

# url = 'https://weborder.id/pbs/Store/StoreMainController'
def main(url, headers, f_bukalapak):
    response = requests.get(url, headers=headers)
    page_soup = soup(response.text, "html.parser")
    list_pub = page_soup.find_all("ul",{"class":"dropdown-menu"})[3]

    temp = list_pub.find_all('a')

    for i in range(0, len(temp)):
        penerbit = temp[i].text
        penerbit = re.sub(' +', ' ', penerbit)
        url = temp[i].get('href')
        print(penerbit)
        
        while True:
            response = requests.get(url, headers=headers)
               
            scrap(response, f_bukalapak, penerbit)
            
            page_soup = soup(response.text, "html.parser")
            next_page = page_soup.findAll("li",{"class":"next page"})
            if next_page: 
                link = next_page[0].find_all('a')[0].get('href')
                url = link
            else:
                break


if __name__ == '__main__':
    headers = hd()
    url = 'https://weborder.id/pbs/Store/StoreMainController'
    
    f_bukalapak = open('../dokumen/bukalapak20200627.csv', "w")

    main(url, headers, f_bukalapak)

    f_bukalapak.close()