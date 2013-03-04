#!/usr/local/bin/python

import csv
import sys
import re
import requests
import lxml
from bs4 import BeautifulSoup

BASE_URL = 'http://nces.ed.gov/collegenavigator/'
relative_link = '?s=MN&pg=11&id=17391101' #South Central College-Faribault link
SCHOOL_URL = BASE_URL + relative_link
find_ipeds = re.search("[0-9]+\Z", relative_link)
ipeds = find_ipeds.group(0) + '\n'
response = requests.get(SCHOOL_URL)
if response.status_code == 200:
    try:
        soup = BeautifulSoup(response.text)
        find_ids = soup.find_all('span','ipeds')
        ipeds_id = find_ids[2].next_element
        ope_id = ipeds_id.next_sibling.next_sibling
        #aid_section = soup.find('div', id="divctl00_cphCollegeNavBody_ucInstitutionMain_ctl01")
        #table = aid_section("table")[1]
        #row_pell = table('tr')[2]
        #pell_percent = row_pell('td')[2].text
        #total_pell = row_pell('td')[3].text
        #row_loan = table('tr')[3]
        #loan_percent = row_loan('td')[2].text
        #total_loan = row_loan('td')[3].text
        print total_loan
        
    except (IndexError,TypeError,AttributeError):
        
        print "ERROR"
else:
    print "Problem with subroutine. Response: "