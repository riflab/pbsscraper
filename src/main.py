# -*- coding: utf-8 -*-
"""
https://github.com/riflab/pbsscraper.git

@author: Arif Darmawan
email: arif.darmawan@riflab.com
"""

from bs4 import BeautifulSoup as soup
from headers import hd
from scrap import scrap
from datetime import datetime
import requests
import re
import xlsxwriter

def main(url, headers, BL, TP, SP, TA):
    response = requests.get(url, headers=headers)
    page_soup = soup(response.text, "html.parser")
    list_pub = page_soup.find_all("ul",{"class":"dropdown-menu"})[3]

    temp = list_pub.find_all('a')
    
    index = index_BL = index_TP = index_SP = index_TA = 0
    BLws = TPws = SPws = TAws = ''

    for i in range(0, len(temp)):
        penerbit = temp[i].text
        penerbit = ' '.join(penerbit.split())
        url = temp[i].get('href')
        print(penerbit)

        while True:

            response = requests.get(url, headers=headers)
               
            index, index_BL, index_TP, index_SP, index_TA, BLws, TPws, SPws, TAws = scrap(index, index_BL, index_TP, index_SP, index_TA, response, BL, BLws, TP, TPws, SP, SPws, TA, TAws, penerbit)
            
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
    TP = xlsxwriter.Workbook('../dokumen/TP_' + str(d) + '_.xlsx')
    SP = xlsxwriter.Workbook('../dokumen/SP_' + str(d) + '_.xlsx')
    TA = xlsxwriter.Workbook('../dokumen/TA_' + str(d) + '_.xlsx')
    main(url, headers, BL, TP, SP, TA)
    BL.close()
    TP.close()
    SP.close()
    TA.close()
