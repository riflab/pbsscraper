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
    'cookie': 'ci_session=tt33nc0b2kkr7a1u12s0sth2ngnspi7t; csrf_cookie_name=e3994ae85295f94811850ee8d2a9e7fa',
}

    return headers