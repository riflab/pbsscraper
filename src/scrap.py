# -*- coding: utf-8 -*-
"""
https://github.com/riflab/pbsscraper.git

@author: Arif Darmawan
email: arif.darmawan@riflab.com
"""

from bs4 import BeautifulSoup as soup
from headers import hd
from mod import judul_checker, print_BL, print_TP, print_SP, print_TA, image_rename, deskripsi_checker
from datetime import datetime
from test import test
import requests
import xlsxwriter

def scrap(index, index_BL, index_TP, index_SP, index_TA, response, BL, BLws, TP, TPws, SP, SPws, TA, TAws, penerbit='-'):
    page_soup = soup(response.text, "html.parser")
    
    # test(index, index_BL, index_TP, index_SP, index_TA, response, BL, BLws, TP, TPws, SP, SPws, TA, TAws, '-')
    product_items = page_soup.find_all("div",{"class":"product-item"})
    desc = page_soup.find_all("div",{"class":"description"})
    images = page_soup.find_all("div",{"class":"product-main-image"})

    for i in range(0, len(product_items)):
        judul = product_items[i].h3.a.text.replace(',', '.')
        judul = judul_checker(judul, penerbit)
        
        if index % 150 == 0:
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
            TAws = TA.add_worksheet()
            index_TA = 1

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
                desc_text = deskripsi_checker(str(deskripsi))

                temp1 = image_rename(penerbit)
                temp2 = image_rename(judul)

                d = open('../deskripsi/' + temp1 + '___' + temp2 + '.txt','w')
                d.write(desc_text)
                d.close()

                print(index, judul, penerbit)
                
                url_gambar = '../gambar/' + temp1 + '___' + temp2 + '.jpg'
                
                print_BL(index_BL, BLws, judul, stok, berat, beli, tag, penerbit, url_gambar[3:], desc_text)
                print_TP(index_TP, TPws, judul, stok, berat, beli, tag, penerbit, url_gambar[3:], desc_text)
                print_SP(index_SP, SPws, judul, stok, berat, beli, tag, penerbit, url_gambar[3:], desc_text)
                print_TA(index_TA, TAws, judul, stok, berat, beli, tag, penerbit, url_gambar[3:], desc_text, jual)
                
                link_img = images[i].img.get("src")
                with open(url_gambar, "wb") as img:
                    img.write(requests.get(link_img).content)
                
                index += 1
                index_BL += 1
                index_TP += 1
                index_SP += 1
                index_TA += 1

        except: 
            stok = berat = tag = jual = beli = '-'
            
            pass
        
    return index, index_BL, index_TP, index_SP, index_TA, BLws, TPws, SPws, TAws
    

if __name__ == '__main__':
    headers, cookies = hd()
    url = 'https://weborder.id/pbs/Store/StoreMainController/suppub/1/10/0'
    response = requests.get(url, headers=headers, cookies=cookies)
    
    index = index_BL = index_TP = index_SP = index_TA = 0
    BLws = TPws = SPws = TAws = ''

    d = datetime.now().date()
    BL = xlsxwriter.Workbook('../dokumen/' + str(d) + '_BL_.xlsx')
    TP = xlsxwriter.Workbook('../dokumen/' + str(d) + '_TP_.xlsx')
    SP = xlsxwriter.Workbook('../dokumen/' + str(d) + '_SP_.xlsx')
    TA = xlsxwriter.Workbook('../dokumen/' + str(d) + '_TA_.xlsx')
    index, index_BL, index_TP, index_SP, index_TA, BLws, TPws, SPws, TAws = scrap(index, index_BL, index_TP, index_SP, index_TA, response, BL, BLws, TP, TPws, SP, SPws, TA, TAws, 'ADZ DHAHABI')
    BL.close()
    TP.close()
    SP.close()
    TA.close()