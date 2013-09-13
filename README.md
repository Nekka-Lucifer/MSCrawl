README

All testing done on a clean install of Ubuntu Desktop 12.04 64bit

1. 
Run install.sh via "sh install.sh" in the terminal
You will need to enter the sudo password

Python should now be fully updated with Scrapy
Tor and Privoxy should also be installed, fully configured, and reloaded.

2.
Test the installation has been succesful by running test.sh via "sh test.sh"
If succesful, you should get two different IPs

####INFO####
The Web-scraping works in 2 parts.
The first part retrieves the links to the company pages.
The second part extracts the addresses from those links.
####INFO####

3.
You need to fill in the Get.txt file provided with links to the area pages
E.g. "
http://www.masterseek.com/companies/United-Kingdom/Bolton/1
http://www.masterseek.com/companies/United-Kingdom/Bolton/2
http://www.masterseek.com/companies/United-Kingdom/Bolton/3
"
Be sure to not give any invalid URLs and that you fill the file with each page of locations.
E.g. Bolton has 84 pages, so there will be 84 lines.
To find how many pages, there is a "Last" button at the bottom of the Location pages.

4.
Run Get.sh via "sh Get.sh"
This will clear the file "Links.txt".
It will then populate it with links from pages you provided in Get.txt
This is done using the Tor network.

5.
Run Extract.sh via "sh Extract.sh"
This will extract the company names, addresses, phone numbers, etc. from the links in Links.txt
Make sure Links.txt has at least 1 line
The addresses will be stored in Addresses.csv
WARNING: This will overwrite the file.

6.
Wait... 

7.
Enjoy your list of company addresses.

TROUBLESHOOTING:
Running install.sh:
The installation has been tested on Ubuntu 12.04 64Bit (Desktop)
It's not recommended to install on other packages (Such as Debian) as the configuration files are stored in different locations
Make sure you have an internet connection.

Running Get.sh / Extract.sh
Ensure Privoxy and Tor are fully installed and running (Using test.sh)
Ensure Get.txt has at least 1 line and the URL(s) are valid when running EITHER script