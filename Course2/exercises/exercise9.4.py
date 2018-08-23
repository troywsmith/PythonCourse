# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# name = input("Enter file:")
name = 'mbox-short.txt'
handle = open(name)

counts = dict()

for line in handle:
  if line.startswith('From '):
    email = line.split()[1]
    counts[email] = counts.get(email, 0) + 1

biggestK = None
biggestV = None
for k,v in counts.items():
  if biggestV is None or v > biggestV:
    biggestK = k
    biggestV = v

print(biggestK, biggestV)
