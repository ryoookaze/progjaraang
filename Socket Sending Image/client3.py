import random, os
import socket, select
from time import gmtime, strftime
from random import randint


HOST = '127.0.0.1'
PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)

try:
    answer = sock.recvfrom(4096)
    images = answer[:5] + "1.jpg"
    print ('answer = %s') % answer
    if images:
        print("File:"), images
        file_name = images

    myfile = open(file_name, 'wb')

    if answer == 'GOT SIZE':
        sock.sendall(bytes)

        answer = sock.recv(4096)
        print ('answer = %s') % answer

        if answer == 'GOT IMAGE' :
            sock.sendall("BYE BYE ")
            print ("Image successfully send to server") % file_name

    myfile.close()

finally:
    sock.close()