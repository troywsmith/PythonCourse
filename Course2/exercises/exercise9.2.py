# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

name = 'mbox-short.txt'
handle = open(name)

counts = dict()

for line in handle:
  if line.startswith('From '):
    month = line.split()[3]
    counts[month] = counts.get(month, 0) + 1

print(counts)
