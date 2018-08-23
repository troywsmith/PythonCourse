# Exercise 3: Write a program to read through a mail log, build a histogram
# using a dictionary to count how many messages have come from
# each email address, and print the dictionary.

name = 'mbox-short.txt'
handle = open(name)

counts = dict()

for line in handle:
  if line.startswith('From '):
    email = line.split()[1]
    counts[email] = counts.get(email, 0) + 1

print(counts)