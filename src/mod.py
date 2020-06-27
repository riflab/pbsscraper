# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:28:26 2020

@author: Arif Darmawan
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

def print_bukalapak(f_bukalapak, judul, stok, berat, beli, tag, penerbit, url_gambar, desc_text):
    
    domain = 'https://alhaf.com/'
    beli = markup_beli(beli)
    stok = stok_checker(stok)
    
    desc = 'Silahkan chat terlebih dahulu untuk menanyakan ketersediaan stok barang' 
    
    f_bukalapak.write(judul + ',' + 
                      stok + ',' + 
                      berat + ',' + 
                      beli + ',' +
                      'Baru' + ',' +
                      desc + ',' + 
                      'Tidak' + ',' + 
                      'j&tr | jner | tikir | wahana' + ',' + 
                      domain + url_gambar + ',' +
                      penerbit + ',' +
                      tag + '\n')
