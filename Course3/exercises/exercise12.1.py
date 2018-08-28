import socket

url = input('Please enter a URL:')
host  = url.split('/')[2]

print(url, host)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( (host, 80) )

cmd = 'GET ${url} HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
  data = mysock.recv(3000)
  if (len(data) < 1):
    break
  print(data.decode())
mysock.close()