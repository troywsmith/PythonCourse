# Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.

values = []

while True:
  value = input('Enter a number: ')
  try:
    values.append(int(value))
  except: 
    print('Invalid input')
  if value == 'done':
    print('Maximum is', max(values))
    print('Minimum is', min(values))
    break

  