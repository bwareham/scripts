#!/usr/local/bin/python

#THIS IS THE ORIGINAL MASTER COPY OF A SCRAPE FOR THE COLLEGE NAVIGATOR SITE
#MAKE A COPY TO REWORK TO SCRAPE OTHER DATA FROM THE SITE

import sys
import re
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://nces.ed.gov/collegenavigator/'
#State=MN returns 161 schools or 11 pages at 15 per page;
#if I were ambitious I would automate range determination
PAGES = range(1,12)
for page in PAGES:
    PAGE_URL = BASE_URL + '?s=MN&pg=' + "%s" % (page)
    path_start = '?s=MN&pg=%s&id=' % (page)
    response = requests.get(PAGE_URL)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text)
        links = soup.findAll('a')

        download_links = soup.findAll('a', href=lambda path: path and path.startswith(path_start))
        file = open('/home/bwareham/output/netprices.csv', 'a')
        for link in download_links:
            school_name = link.text.encode('utf-8') #encode necessary because initial runs returned UnicodeEncondingError
            relative_link = link.get('href')
            SCHOOL_URL = BASE_URL + relative_link
            find_ipeds = re.search("[0-9]+\Z", relative_link)
            ipeds = find_ipeds.group(0)
            response = requests.get(SCHOOL_URL)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.text) 
                    netprice_section = soup.find('div', id="divctl00_cphCollegeNavBody_ucInstitutionMain_ctl02")
                    table = netprice_section("table")[0]
                    row = table('tr')[1]
                    netprice = row('td')[3].text

                except (IndexError,TypeError):
                    netprice = "N/A"
            else:
                print "Problem with subroutine. Response: "#subroutine goes here
            file_row = ipeds + ", " + school_name + "," + netprice + '\n'
            print file_row
            file.write(file_row)

    else:
        sys.exit("Response code not OK: %s" % response.status_code)
else:
    
    #file = open('/home/bwareham/output/netprices.csv', 'r+')
    #file.write(file_rows)
    file.close()
    print "Job complete"

