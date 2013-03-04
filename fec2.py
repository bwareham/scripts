#!/usr/bin/env python

import csv
import sys

import requests
from BeautifulSoup import BeautifulSoup

form_data = {
    'name':'Romney', # committee name field
    'type':'P',      # committee type is P for Presidential
    'frmtype':'F3P', # form type
}
response = requests.post('http://query.nictusa.com/cgi-bin/dcdev/forms/', data=form_data)

if response.status_code == 200:
    soup = BeautifulSoup(response.text)
    links = soup.findAll('a')

    download_links = soup.findAll('a', href=lambda path: path and path.startswith('/cgi-bin/dcdev/forms/DL/'))

    print download_links

else:
    sys.exit("Response code not OK: %s" % response.status_code)