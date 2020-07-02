# -*- coding: utf-8 -*-
"""
https://github.com/riflab/pbsscraper.git

@author: Arif Darmawan
email: arif.darmawan@riflab.com
"""

from bs4 import BeautifulSoup as soup
from headers import hd
from scrap import scrap
import requests
import re
import xlsxwriter

def main(url, headers, BL, TP):
    response = requests.get(url, headers=headers)
    page_soup = soup(response.text, "html.parser")
    list_pub = page_soup.find_all("ul",{"class":"dropdown-menu"})[3]

    temp = list_pub.find_all('a')
    
    index = index_BL = index_TP = 0
    f_bukalapak = f_tokopedia = ''

    for i in range(0, len(temp)):
        penerbit = temp[i].text
        penerbit = re.sub(' +', ' ', penerbit)
        url = temp[i].get('href')
        print(penerbit)

        while True:

            response = requests.get(url, headers=headers)
               
            index, index_BL, index_TP, f_bukalapak, f_tokopedia = scrap(index, index_BL, index_TP, response, BL, f_bukalapak, TP, f_tokopedia, penerbit)
            
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
    
    d = datetime.now().date()
    BL = xlsxwriter.Workbook('../dokumen/BL_' + str(d) + '_.xlsx')
    TP = xlsxwriter.Workbook('../dokumen/BL_' + str(d) + '_.xlsx')
    main(url, headers, BL, TP)
    BL.close()
    TP.close()
