# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:28:26 2020

@author: Arif Darmawan
"""
import re



def deskripsi_checker(text):
    
    text = text.strip()
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    text = re.sub(' +', ' ', text)
    text = text.replace("b'", '').replace(",", '.').
    
    return text

if __name__ == '__main__':
    
    s = 'bBuku 76 Dosa Besar yang Dianggap Biasa ini adalah terjemah dari kitab Al-Kaba\xe2\x80\x99ir karya pakar hadits Imam Adz-Dzahabi. Beliau dikenal sangat hati-'
    s = deskripsi_checker(s)
    
    print(s)
