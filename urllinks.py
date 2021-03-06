import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certification errors // Info stackoverflow
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = input("Enter-")
html = urllib.request.urlopen(urls, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
