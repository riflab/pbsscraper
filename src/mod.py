# -*- coding: utf-8 -*-
"""
https://github.com/riflab/pbsscraper.git

@author: Arif Darmawan
email: arif.darmawan@riflab.com
"""

import re
import math

def deskripsi_checker(text):
    
    # text = text.replace("b'", '').replace("'", '').replace('"', '')
    # text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    # text = re.sub(' +', ' ', text)
    text = ' '.join(text.split())
    
    return text

def image_rename(image_name):

    image_name = ' '.join(image_name.split())
    image_name = image_name.replace(' ', '-')    
    
    return image_name

def roundup(x):
    
    return int(math.ceil(x / 100.0)) * 100

def stok_checker(stok):
    
    stok = int(stok)
    if stok < 0:
        stok = 0

    stok +=1
        
    return str(stok)
    
def markup_beli(beli):

    beli = int(beli)
    beli = (beli*115/100)+2000
    beli = roundup(beli)

    return str(beli)

def judul_checker(judul, penerbit):
    
    judul = ' '.join(judul.split()).title()
    judul = judul.replace('(', ' ')
    judul = judul.replace(')', ' ')
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
    
    # judul = judul.title().replace(penerbit.title(), ' ') 
    # judul = ' '.join(judul.split())

    return judul

def print_BL(index_BL, BLws, judul, stok, berat, beli, tag, penerbit, url_gambar, desc_text):
    
    domain = 'https://alhaf.com/'
    beli = markup_beli(beli)
    stok = stok_checker(stok)
    
    desc = 'Silahkan chat terlebih dahulu untuk menanyakan ketersediaan stok barang.'  
    desc = desc + ' \n\n' + judul

    BLws.write(index_BL, 1, judul[:150])
    BLws.write(index_BL, 2, stok)
    BLws.write(index_BL, 3, berat)
    BLws.write(index_BL, 4, beli)
    BLws.write(index_BL, 5, 'Baru')
    BLws.write(index_BL, 6, desc)
    BLws.write(index_BL, 7, 'Tidak')
    BLws.write(index_BL, 8, 'j&tr | jner | tikir | wahana')
    BLws.write(index_BL, 9, domain + url_gambar)

def print_TP(index_TP, TPws, judul, stok, berat, beli, tag, penerbit, url_gambar, desc_text):
    
    SKU = 1

    if tag == 'Buku Sunnah':
        tagN = 3324
        etalase = 24393638
    elif tag == 'Buku Anak':
        tagN = 3373
        etalase = 24393635
    elif tag == 'Mushaf Al Quran':
        tagN = 826
        etalase = 24393641
    
    domain = 'https://alhaf.com/'
    beli = markup_beli(beli)
    stok = stok_checker(stok)

    desc = 'Silahkan chat terlebih dahulu untuk menanyakan ketersediaan stok barang.'  
    desc = desc + ' \n\n' + judul 

    TPws.write(index_TP, 1, judul[:70])
    TPws.write(index_TP, 2, SKU)
    TPws.write(index_TP, 3, tagN)
    TPws.write(index_TP, 4, desc)
    TPws.write(index_TP, 5, beli)
    TPws.write(index_TP, 6, berat)
    TPws.write(index_TP, 7, 1)
    TPws.write(index_TP, 8, 'Aktif')
    TPws.write(index_TP, 9, stok)
    TPws.write(index_TP, 10, etalase)
    TPws.write(index_TP, 11, '')
    TPws.write(index_TP, 12, '')
    TPws.write(index_TP, 13, 'Baru')
    TPws.write(index_TP, 14, domain + url_gambar)

def print_SP(index_SP, SPws, judul, stok, berat, beli, tag, penerbit, url_gambar, desc_text):
    
    domain = 'https://alhaf.com/'
    beli = markup_beli(beli)
    stok = stok_checker(stok)
    
    desc = 'Silahkan chat terlebih dahulu untuk menanyakan ketersediaan stok barang.'  
    desc = desc + ' \n\n' + judul

    kategori = 16984
    SKU = 1

    SPws.write(index_SP, 1, kategori)
    SPws.write(index_SP, 2, judul[:100])
    SPws.write(index_SP, 3, desc[:3000])
    SPws.write(index_SP, 4, SKU)
    SPws.write(index_SP, 5, '')
    SPws.write(index_SP, 6, '')
    SPws.write(index_SP, 7, '')
    SPws.write(index_SP, 8, '')
    SPws.write(index_SP, 9, '')
    SPws.write(index_SP, 10, '')
    SPws.write(index_SP, 11, beli)
    SPws.write(index_SP, 12, stok)
    SPws.write(index_SP, 13, '')
    SPws.write(index_SP, 14, domain + url_gambar)
    SPws.write(index_SP, 15, '')
    SPws.write(index_SP, 16, '')
    SPws.write(index_SP, 17, '')
    SPws.write(index_SP, 18, '')
    SPws.write(index_SP, 19, '')
    SPws.write(index_SP, 20, '')
    SPws.write(index_SP, 21, '')
    SPws.write(index_SP, 22, '')
    SPws.write(index_SP, 23, berat)
    SPws.write(index_SP, 24, '')
    SPws.write(index_SP, 25, '')
    SPws.write(index_SP, 26, '')
    SPws.write(index_SP, 27, 'Aktif')
    # SPws.write(index_SP, 28, '')
    # SPws.write(index_SP, 29, '')