# -*- coding: utf-8 -*-
"""
https://github.com/riflab/pbsscraper.git

@author: Arif Darmawan
email: arif.darmawan@riflab.com
"""

def hd():

    headers = {
    'authority': 'weborder.id',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://weborder.id/pbs/Store/StoreMainController',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ci_session=vpkm4p8l3em7kjn7euart5dn9kc240r7; csrf_cookie_name=3fa263f63b1b2cb92d574b5d1ba130fd',
}

    return headers