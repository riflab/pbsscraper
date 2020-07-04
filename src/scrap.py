# -*- coding: utf-8 -*-
"""
https://github.com/riflab/pbsscraper.git

@author: Arif Darmawan
email: arif.darmawan@riflab.com
"""

from bs4 import BeautifulSoup as soup
from headers import hd
from mod import judul_checker, print_bukalapak, print_tokopedia, image_rename, deskripsi_checker
import requests
import re
import xlsxwriter

def scrap(index, index_BL, index_TP, response, BL, f_bukalapak, TP, f_tokopedia, penerbit='-'):
    page_soup = soup(response.text, "html.parser")
    
    product_items = page_soup.find_all("div",{"class":"product-item"})
    desc = page_soup.find_all("div",{"class":"description"})
    images = page_soup.find_all("div",{"class":"product-main-image"})

    for i in range(0, len(product_items)):
        judul = product_items[i].h3.a.text.replace(',', '.')
        judul = judul_checker(judul)

        if index % 90 == 0:
            # d = datetime.now().date()
            # BL.close()
            # f_bukalapak = open('../dokumen/BL_' + str(int(index/90)) + '_' + str(d) + '_.csv', "w")
            # BL = xlsxwriter.Workbook('../dokumen/BL_' + str(int(index/90)).zfill(2) + '_' + str(d) + '_.xlsx')
            f_bukalapak = BL.add_worksheet()
            index_BL = 1

        if index % 150 == 0:
            # d = datetime.now().date()
            # TP.close()
            # f_tokopedia = open('../dokumen/TP_' + str(int(index/150)) + '_' + str(d) + '_.csv', "w")
            # TP = xlsxwriter.Workbook('../dokumen/TP_' + str(int(index/150)).zfill(2) + '_' + str(d) + '_.xlsx')
            f_tokopedia = TP.add_worksheet()
            index_TP = 1

        try:
            atemp = product_items[i].find_all('p')
            stok = atemp[0].text.split()[2]
            berat = atemp[1].text.split()[2]
            tag = atemp[2].text.replace(';', ' ')
            tag = re.sub(' +', ' ', tag)

            if tag == ' Buku Sunnah' or tag == ' Buku Anak' or tag == ' Mushaf Al Quran':
                b = product_items[i].find_all("div",{"class":"pi-price"})
                jual = b[0].text.split()[2].split('.')[1].replace(',', '')
                beli = b[0].text.split()[6].replace(',', '')
                deskripsi = desc[i].text.strip()
                
                temp1 = image_rename(penerbit)
                temp2 = image_rename(judul)
                
                d = open('../deskripsi/' + temp1 + '___' + temp2 + '.txt','w')
                
                desc_text = deskripsi_checker(str(deskripsi))
                
                d.write(desc_text)
                d.close()       
                print(index, judul, penerbit)
                
                url_gambar = '../gambar/' + temp1 + '___' + temp2 + '.jpg'
                
                print_bukalapak(index_BL, f_bukalapak, judul, stok, berat, beli, tag, penerbit, url_gambar[3:], desc_text)
                print_tokopedia(index_TP, f_tokopedia, judul, stok, berat, beli, tag, penerbit, url_gambar[3:], desc_text)
                
                link_img = images[i].img.get("src")
                with open(url_gambar, "wb") as img:
                    img.write(requests.get(link_img).content)
                
                index += 1
                index_BL += 1
                index_TP += 1

        except: 
            stok = berat = tag = jual = beli = '-'
            
            pass
        
    return index, index_BL, index_TP, f_bukalapak, f_tokopedia
    

if __name__ == '__main__':
    headers = hd()
    url = 'https://weborder.id/pbs/Store/StoreMainController/suppub/1/10/0'
    response = requests.get(url, headers=headers)
    
    index = index_BL = index_TP = 0
    f_bukalapak = f_tokopedia = ''

    d = datetime.now().date()
    BL = xlsxwriter.Workbook('../dokumen/BL_' + str(d) + '_.xlsx')
    TP = xlsxwriter.Workbook('../dokumen/TP_' + str(d) + '_.xlsx')
    # index, f_bukalapak, TP = scrap(index, response, f_bukalapak, TP,'Pustaka Alhaf')
    index, index_BL, index_TP, f_bukalapak, f_tokopedia = scrap(index, index_BL, index_TP, response, BL, f_bukalapak, TP, f_tokopedia, 'Pustaka Alhaf')
    BL.close()
    TP.close()