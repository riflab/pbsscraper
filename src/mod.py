# -*- coding: utf-8 -*-
"""
https://github.com/riflab/pbsscraper.git

@author: Arif Darmawan
email: arif.darmawan@riflab.com
"""

import re
import math

def deskripsi_checker(text):
    
    text = text.replace("b'", '').replace("'", '').replace('"', '')
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    text = re.sub(' +', ' ', text)
    
    return text

def image_rename(image_name):
    
    image_name = image_name.replace(' ', '-')    
    
    return image_name

def roundup(x):
    
    return int(math.ceil(x / 100.0)) * 100

def stok_checker(stok):
    
    stok = int(stok)
    if stok < 0:
        stok = 0
        
    return str(stok)
    
def markup_beli(beli):

    beli = int(beli)
    beli = (beli*110/100)+2000
    beli = roundup(beli)

    return str(beli)

def judul_checker(judul):
    
    judul = re.sub(' +', ' ', judul)
    temp = judul
    temp = judul.split()
    
    try:
        temp = int(temp[0])
        judul = 'Buku ' + judul
    except ValueError:

        if temp[0] == 'Buku' or temp[0] == 'Mushaf':
            pass
        else:
            judul = 'Buku ' + judul
    
    return judul.title()

def print_bukalapak(index_BL, f_bukalapak, judul, stok, berat, beli, tag, penerbit, url_gambar, desc_text):
    
    domain = 'https://alhaf.com/'
    beli = markup_beli(beli)
    stok = stok_checker(stok)
    
    desc = 'Silahkan chat terlebih dahulu untuk menanyakan ketersediaan stok barang.'  

    f_bukalapak.write(index_BL, 1, judul)
    f_bukalapak.write(index_BL, 2, stok)
    f_bukalapak.write(index_BL, 3, berat)
    f_bukalapak.write(index_BL, 4, beli)
    f_bukalapak.write(index_BL, 5, 'Baru')
    f_bukalapak.write(index_BL, 6, desc)
    f_bukalapak.write(index_BL, 7, 'Tidak')
    f_bukalapak.write(index_BL, 8, 'j&tr | jner | tikir | wahana')
    f_bukalapak.write(index_BL, 9, domain + url_gambar)

def print_tokopedia(index_TP, f_tokopedia, judul, stok, berat, beli, tag, penerbit, url_gambar, desc_text):
    
    SKU = 1

    if tag == ' Buku Sunnah':
        tagN = 3324
        etalase = 24393635
    elif tag == ' Buku Anak':
        tagN = 3373
        etalase = 24393641
    elif tag == ' Mushaf Al Quran':
        tagN = 826
        etalase = 24393638
    
    domain = 'https://alhaf.com/'
    beli = markup_beli(beli)
    stok = stok_checker(stok)

    desc = 'Silahkan chat terlebih dahulu untuk menanyakan ketersediaan stok barang.' 

    f_tokopedia.write(index_TP, 1, judul)
    f_tokopedia.write(index_TP, 2, SKU)
    f_tokopedia.write(index_TP, 3, tagN)
    f_tokopedia.write(index_TP, 4, desc)
    f_tokopedia.write(index_TP, 5, beli)
    f_tokopedia.write(index_TP, 6, berat)
    f_tokopedia.write(index_TP, 7, 1)
    f_tokopedia.write(index_TP, 8, 'Aktif')
    f_tokopedia.write(index_TP, 9, stok)
    f_tokopedia.write(index_TP, 10, etalase)
    f_tokopedia.write(index_TP, 11, '')
    f_tokopedia.write(index_TP, 12, '')
    f_tokopedia.write(index_TP, 13, 'Baru')
    f_tokopedia.write(index_TP, 14, domain + url_gambar)
