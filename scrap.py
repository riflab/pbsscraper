# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:28:26 2020

@author: Arif Darmawan
"""

from bs4 import BeautifulSoup as soup
from headers import hd
from mod import judul_checker, print_bukalapak, image_rename, deskripsi_checker
import requests
import re

def main(response, f_bukalapak, penerbit='-'):
    page_soup = soup(response.text, "html.parser")
    
    product_items = page_soup.find_all("div",{"class":"product-item"})
    desc = page_soup.find_all("div",{"class":"description"})
    images = page_soup.find_all("div",{"class":"product-main-image"})
    
    for i in range(0, len(product_items)):
        judul = product_items[i].h3.a.text.replace(',', '.')
        judul = judul_checker(judul)
        
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
                
                d = open('deskripsi/' + temp1 + '___' + temp2 + '.txt','w')
                
                desc_text = deskripsi_checker(str(deskripsi))
                
                d.write(desc_text)
                d.close()       
                print(judul)
                # f.write(judul + ',' + penerbit + ',' + stok + ',' + berat + ',' + tag + ',' + jual + ',' + beli + ',' + penerbit + '___' + judul +'.jpg' + '\n')
                
                url_gambar = 'gambar/' + temp1 + '___' + temp2 + '.jpg'
                
                print_bukalapak(f_bukalapak, judul, stok, berat, beli, tag, penerbit, url_gambar, desc_text)
                
                # link_img = images[i].img.get("src")
                # with open(url_gambar, "wb") as img:
                #     img.write(requests.get(link_img).content)

        except: 
            stok = berat = tag = jual = beli = '-'
            
            pass
    

if __name__ == '__main__':
    headers = hd()
    url = 'https://weborder.id/pbs/Store/StoreMainController/suppub/1/10/0'
    response = requests.get(url, headers=headers)
    
    f_bukalapak = open("bukalapak.csv", "w")

    main(response, f_bukalapak,'Pustaka Alhaf')
    f_bukalapak.close()