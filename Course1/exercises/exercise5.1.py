# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

total = 0
count = 0

while True:
  value = input('Enter a number: ')
  if value == 'done':
    break
  try:
    fval = float(value)
  except: 
    print('Invalid input')
    continue
  
  count += 1
  total += fval

print(total, count, total / count)



