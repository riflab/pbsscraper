# -*- coding: utf-8 -*-
"""
https://github.com/riflab/pbsscraper.git

@author: Arif Darmawan
email: arif.darmawan@riflab.com
"""

def hd():

    cookies = {
    'csrf_cookie_name': 'fb3a9934b396b7afa9beecf5f43b6e1b',
    'ci_session': 'i5rqrh9t3k1ear1tp2pitpa6ipoohfv6',
    }

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://weborder.id/pbs/Store/StoreMainController/suppub/289/10/0',
    'Upgrade-Insecure-Requests': '1',
}


    return headers, cookies