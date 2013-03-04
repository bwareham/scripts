#!/usr/local/bin/python

#THIS IS A MODIFICATION OF THE ORIGINAL MASTER COPY OF A SCRAPE FOR THE COLLEGE NAVIGATOR SITE
#IT IS DESIGNED TO SCRAPE INFO ABOUT FINANCIAL AID
#IT ALSO WILL PULL OPE ID NUMBERS, WHICH THE ORIGINAL DIDN'T

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
        file = open('/home/bwareham/output/cnAid.csv', 'a')
        #error_file = open('/home/bwareham/output/cnAidERROR.txt', 'a')
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
                    find_ids = soup.find_all('span','ipeds')
                    ipeds_id = find_ids[2].next_element
                    ope_id = ipeds_id.next_sibling.next_sibling
                    aid_section = soup.find('div', id="divctl00_cphCollegeNavBody_ucInstitutionMain_ctl01")
                    table = aid_section("table")[1]
                    row_pell = table('tr')[2]
                    pell_percent = row_pell('td')[2].text
                    total_pell = row_pell('td')[3].text
                    row_loan = table('tr')[3]
                    loan_percent = row_loan('td')[2].text
                    total_loan = row_loan('td')[3].text
                    file_row = pell_percent + " | " + total_pell + " | " + loan_percent + " | " + total_loan
                except (IndexError,TypeError,AttributeError):
                    file_row = "ERROR" + ' | ' + "ERROR" + ' | ' + "ERROR" + ' | ' + "ERROR"
                    
            else:
                print "Problem with subroutine. Response: "#subroutine goes here
            file.write(school_name + " | ")
            file.write(ipeds_id + " | " + ope_id + " | ")
            file.write(file_row + '\n')
            print school_name
            

    else:
        sys.exit("Response code not OK: %s" % response.status_code)
else:
    
    
    file.close()
    #error_file.close()
    print "Job complete"

