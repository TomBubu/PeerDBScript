# Source: https://www.youtube.com/watch?v=XQgXKtPSzUI, Data Science Dojo, Published on Jan 6, 2017

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#SJC
sjc_url = "https://peeringdb.com/ix/5"
#AER
aer_url = "https://peeringdb.com/ix/26"
#HKIDC
hkidc_url = "https://peeringdb.com/ix/125"
#SNGIDC
sngidc_url = "https://peeringdb.com/ix/158"
#STLD
stld_url = "https://peeringdb.com/ix/94"
#TYOIDC
tyoidc_url = "https://peeringdb.com/ix/167"


# For SJC:
uClient = uReq(sjc_url)                                         # Grab the webpage and download it
page_html = uClient.read()                                      # Store the content to the varialbe page_html
uClient.close()                                                 # Close the client once the webpage is saved
page_soup = soup(page_html, "html.parser")                      # Pass the page through the BeautifulSoup, use HTML parser

peer_names = page_soup.findAll("div",{"class":"peer"})          # Looking for all divs that have class peer (object class)
peer_ipv4s = page_soup.findAll("div",{"class":"ip4"})           # Looking for IPv4 addresses of peers
peer_ipv6s = page_soup.findAll("div",{"class":"ip6"})           # Looking for IPv6 addresses of peers

for k in range(0,len(peer_names)):
    str_names = peer_names[k].get_text()
    str_ipv4s = peer_ipv4s[k].get_text()
    str_ipv6s = peer_ipv6s[k].get_text()
    str_to_remove = "\n"
    print(str_names.strip(str_to_remove))
    print(str_ipv4s)
    print(str_ipv6s)
    print("\n")
    k+=1

