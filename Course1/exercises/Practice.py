# x = 11
# if x < 2: 
#   print('Small')
# elif x < 10:
#   print('Medium')
# else: 
#   print('Large')
# print('All done.')

# str = 'Hello Troy'
# # using a try to elinate a possibility of a traceback
# try:      
#   istr = int(str)
# except:
#   istr = -1

# print('Done', istr)

# rawstr = input('Enter a number: ')
# try:
#   ival = int(rawstr)
# except:
#   ival = -1

# if ival > 0:
#   print('Number: ', ival)
# else:
#   print('Not a number')

def thing(str):
  print(str)
thing('Hello World')

big = max('hello world')
print(big)

def greet():
  return "Hello"
print(greet())

def addTwo(a, b):
  return a + b

print(addTwo(2, 3))