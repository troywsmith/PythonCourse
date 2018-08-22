# fruit = 'banana'
# print(fruit[1:4])
# print(len(fruit))
# print(fruit.count('a'))

# index = 0
# while index < len(fruit):
#   letter = fruit[index]
#   print(index, letter)
#   index += 1

# for letter in fruit:
#   print(letter)

# a = 'Hello '
# b = a + 'There'

# print(b)

# if 'a' in b:
#   print('Found it!')
# else:
#   print('Cant find it')


# print(b.split(' '))
# print(b)

# greet = ' Hello Bob '
# newStr = greet.replace('Bob', 'Jane')
# print(newStr)

# print(greet.strip())

# line = 'Please have a nice day'
# print(line.startswith('Please'))
# print(line.startswith('sdga'))

# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# atPos = data.find('@')
# print(atPos)

# sppos = data.find(' ', atPos)
# print(sppos)

# host = data[atPos+1 : sppos]
# print(host)

# x = 'From marquard@uct.ac.za'
# print(x[14:17])

# fname = input('Enter a file name: ')

# try:
#   fhand = open(fname)
# except:
#   print('Cannot open file', fname)
#   quit()

# count = 0
# for line in fhand:
#   if line.startswith('Subject:'):
#     count += 1

# print('There were', count, 'subject lines in', fname)

# friends = ['Joe', 'Glenn', 'Sally']

# for friend in friends:
#   print(friend)

# for i in range(len(friends)):
#   friend = friends[i]
#   print(friend, i)

# t = [9, 41, 12, 3, 74, 15]
# print(t[:3])
# print(t[3:])

# stuff = list()

# stuff.append('book')
# stuff.append(99)
# print(stuff)

# while True:
#   inp = input('Enter a #: ')
#   if inp == 'done':
#     break
#   stuff.append(float(inp))

# average = sum(stuff) / len(stuff)
# print('Average:', average)

# abc = 'With three words'
# stuff = abc.split()
# print(stuff)

# for word in stuff:
#   print(word)

# Use the file name mbox-short.txt as the file name
fh = open('mbox.txt')

for line in fh:
    if line.startswith("From") :
      emailLines = line.split()
      email = emailLines[1]
      domain = email[email.find('@') + 1 : ]
      print(domain) 
