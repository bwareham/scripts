#!/usr/local/bin/python

import sys
import re
import requests
from bs4 import BeautifulSoup

#Rewriting Target store scrape to get legislator educational info

START_URL = 'http://www.house.leg.state.mn.us/members/hmem.asp'
BASE_URL = '###'

get_members = requests.get(START_URL)


if get_members.status_code == 200:
    members_soup = BeautifulSoup(get_members.text)
    member_pics = members_soup.findAll('td', style_="vertical-align:middle;text-align:center;width:90px;float:left;")
    file = open('/home/bwareham/output/xgrmembers.txt', 'a')
""" 
 for link in state_links:
            relative_link = link.get('href')
            STATE_URL = BASE_URL + relative_link
            get_stores = requests.get(STATE_URL)
            if get_stores.status_code == 200:
                store_soup = BeautifulSoup(get_stores.text)
                store_links = store_soup.findAll('tr', class_="data-row")
                for link in store_links:
                    info = link.findAll('td', limit=4)
                    for field in info:
                        #print field.text + "|"
                        file.write(field.text + '|')
                    file.write('\n')
            else:
                print "Problem with get_stores"			
"""
    print "SUCCESS"
else:
    sys.exit("Response code not OK: %s" % response.status_code)

