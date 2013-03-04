#!/usr/local/bin/python


import sys
import re
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://nces.ed.gov/collegenavigator/?s=MN&pg=10'

response = requests.get(BASE_URL)
    
if response.status_code == 200:
    soup = BeautifulSoup(response.text)
    links = soup.findAll('a')

    download_links = soup.findAll('a', href=lambda path: path and path.startswith(path_start))
    file = open('/home/bwareham/output/southcentral.txt', 'a')
    for link in download_links:
        school_name = link.text.encode('utf-8') #encode necessary because initial runs returned UnicodeEncondingError
        """
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
        """
        file_row = school_name + '\n'
        print file_row
        file.write(file_row)

    else:
        sys.exit("Response code not OK: %s" % response.status_code)
else:
    
    file.close()
    print "Job complete"

