# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

name = 'mbox-short.txt'
handle = open(name)

counts = dict()

for line in handle:
  if line.startswith('From '):
    email = line.split()[1]
    address = email[email.find('@') + 1:]
    counts[address] = counts.get(address, 0) + 1

print(counts)