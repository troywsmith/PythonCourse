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


# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()

# print(html)
# # soup = BeautifulSoup(html, 'html.parser')

# # # Retrieve all of the anchor tags
# # tags = soup('a')
# # for tag in tags:
# #     print(tag.get('href', None))

# import json
# data = '''
# {
#   "name" : {
#     "type" : "intl",
#     "number" : "+1 516 603 0853"
#   },
#   "email" : {
#     "hide" : "yes"
#   }
# }'''

# info = json.loads(data)

# print('Name: ', info["name"])




import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)