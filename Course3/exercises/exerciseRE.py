import re

handle = open('sample2.txt')

total = 0

for line in handle:
  nums = re.findall('[0-9]+', line)
  for num in nums:
    total += int(num)

print(total)