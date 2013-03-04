#!/usr/local/bin/python

import sys
import re
import requests
from bs4 import BeautifulSoup

START_URL = 'http://www.target.com/store-locator/state-listing'
BASE_URL = 'http://www.target.com/store-locator/'

get_states = requests.get(START_URL)

if get_states.status_code == 200:
    states_soup = BeautifulSoup(get_states.text)
    state_links = states_soup.findAll('a', class_="statelink")
    file = open('/home/bwareham/output/stores.txt', 'a')
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
	    #print STATE_URL
else:
    sys.exit("Response code not OK: %s" % response.status_code)


