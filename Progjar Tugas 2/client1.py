import socket
import os
s = socket.socket()
host = "127.0.0.1" 
port = 9000

s.connect((host, port))
s.send("Hello server!")
mypath = "./client1/"

received_file = 'car.jpg'
completeName = os.path.join(mypath, received_file)

with open(completeName, 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')