# import re

# hand = open('mbox-short.txt')

# emails = []

# for line in hand:
#   line = line.rstrip()
#   emailLines = re.findall('From .*@([^ ]*)', line)
#   if emailLines :
#     emails.append(emailLines[0])
  
# print(emails)

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect( ('data.pr4e.org', 80) )

# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)

# while True:
#   data = mysock.recv(512)
#   if (len(data) < 1):
#     break
#   print(data.decode())
# mysock.close()

# print(ord('a'))
# print(ord('A'))
# print(ord('\n'))


# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('https://www.linkedin.com/in/troy-w-smith/')

# # prints lines 
# for line in fhand:
#   print(line)

# making dict of word counts in txt page
# counts = dict()
# for line in fhand:
#   words = line.decode().split()
#   for word in words:
#     counts[word] = counts.get(word, 0) + 1

# print(counts)


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

print(html)
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))