import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_124866.json'
print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
print(data)
js = json.loads(data)
sum = 0
count = 0
for comment in js['comments']:
  sum += int(comment['count'])
  count += 1

print('Count: ', count)
print('Sum: ', sum)

