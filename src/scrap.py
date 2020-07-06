# -*- coding: utf-8 -*-
"""
https://github.com/riflab/pbsscraper.git

@author: Arif Darmawan
email: arif.darmawan@riflab.com
"""

from bs4 import BeautifulSoup as soup
from headers import hd
from mod import judul_checker, print_BL, print_TP, print_SP, image_rename, deskripsi_checker
from datetime import datetime
import requests
import xlsxwriter

def scrap(index, index_BL, index_TP, index_SP, response, BL, BLws, TP, TPws, SP, SPws, penerbit='-'):
    page_soup = soup(response.text, "html.parser")
    
    product_items = page_soup.find_all("div",{"class":"product-item"})
    desc = page_soup.find_all("div",{"class":"description"})
    images = page_soup.find_all("div",{"class":"product-main-image"})

    for i in range(0, len(product_items)):
        judul = product_items[i].h3.a.text.replace(',', '.')
        judul = judul_checker(judul, penerbit)

        if index % 90 == 0:
            # BLws = open('../dokumen/BL_' + str(int(index/90)) + '_' + str(d) + '_.csv', "w")
            # BL = xlsxwriter.Workbook('../dokumen/BL_' + str(int(index/90)).zfill(2) + '_' + str(d) + '_.xlsx')
            BLws = BL.add_worksheet()
            index_BL = 1

        if index % 150 == 0:
            TPws = TP.add_worksheet()
            index_TP = 1

        if index % 3000 == 0:
            SPws = SP.add_worksheet()
            index_SP = 1

        try:
            atemp = product_items[i].find_all('p')
            stok = atemp[0].text.split()[2]
            berat = atemp[1].text.split()[2]
            tag = atemp[2].text.replace(';', ' ')
            tag = ' '.join(tag.split())

            if tag == 'Buku Sunnah' or tag == 'Buku Anak' or tag == 'Mushaf Al Quran':
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
                
                print_BL(index_BL, BLws, judul, stok, berat, beli, tag, penerbit, url_gambar[3:], desc_text)
                print_TP(index_TP, TPws, judul, stok, berat, beli, tag, penerbit, url_gambar[3:], desc_text)
                print_SP(index_SP, SPws, judul, stok, berat, beli, tag, penerbit, url_gambar[3:], desc_text)
                
                link_img = images[i].img.get("src")
                with open(url_gambar, "wb") as img:
                    img.write(requests.get(link_img).content)
                
                index += 1
                index_BL += 1
                index_TP += 1
                index_SP += 1

        except: 
            stok = berat = tag = jual = beli = '-'
            
            pass
        
    return index, index_BL, index_TP, index_SP, BLws, TPws, SPws
    

if __name__ == '__main__':
    headers = hd()
    url = 'https://weborder.id/pbs/Store/StoreMainController/suppub/1/10/0'
    response = requests.get(url, headers=headers)
    
    index = index_BL = index_TP = index_SP = 0
    BLws = TPws = SPws = ''

    d = datetime.now().date()
    BL = xlsxwriter.Workbook('../dokumen/BL_' + str(d) + '_.xlsx')
    TP = xlsxwriter.Workbook('../dokumen/TP_' + str(d) + '_.xlsx')
    SP = xlsxwriter.Workbook('../dokumen/SP_' + str(d) + '_.xlsx')
    index, index_BL, index_TP, index_SP, BLws, TPws, SPws = scrap(index, index_BL, index_TP, index_SP, response, BL, BLws, TP, TPws, SP, SPws, 'ADZ DHAHABI')
    BL.close()
    TP.close()
    SP.close()