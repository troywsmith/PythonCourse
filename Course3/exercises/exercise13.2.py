import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
countIn = int(input('Enter count:' ))
positionIn = int(input('Enter position: '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

newURL = url
count = 1
while count <= countIn + 1:
  url = newURL
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')  

  print(newURL)

  new = tags[positionIn - 1].get('href', None)
  count += 1
  newURL = tags[positionIn - 1].get('href', None)
