import re
inp = input('Enter a regular expression:')

name = 'mbox-short.txt'
handle = open(name)

count = 0
emailLines = []
for line in handle:
  matches = re.findall(inp, line)
  if matches:
    count += 1
    print(line.rstrip())
  
print(name, 'had', count, 'lines that matched', inp)