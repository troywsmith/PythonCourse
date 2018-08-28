import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

sum = 0
num = 0

# address = input('Enter location: ')

url = 'http://py4e-data.dr-chuck.net/comments_124865.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print(counts)
for count in counts:
  print(count.text)
  num += 1
  sum += int(count.text)


print('Count: ', num)
print('Sum: ', sum)