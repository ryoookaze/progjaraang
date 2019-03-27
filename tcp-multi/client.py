import socket
import sys
import threading
import os
from thread import *

TCP_IP = "127.0.0.1"
TCP_PORT = 8502
client_path = "./clientfolder/"
image_name = ["lambo1.jpg", "lambo2.jpg"]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def Main():
    s = socket.socket()
    s.connect((TCP_IP, TCP_PORT))
    if not os.path.exists(client_path):
        os.mkdir(client_path)
        filename = raw_input("Filename? -> ")
        if filename != 'q':
            s.send(filename)
            data = s.recv(4096)
            if data[:6] == 'EXISTS':
                filesize = long(data[6:])
                message = raw_input("File exists, " + str(filesize)+"Bytes, download? (Y/N)? -> ")
                if message == 'Y':
                    s.send("OK")
                    f = open('new_'+filename, 'wb')
                    data = s.recv(4096)
                    totalRecv = len(data)
                    f.write(data)
                    while totalRecv < filesize:
                        data = s.recv(4096)
                        totalRecv += len(data)
                        f.write(data)
                        print "{0:.2f}".format((totalRecv/float(filesize))*100)+"% Done"
                    print "Download Complete!"
            else:
                print "File Does Not Exist!"

    s.close()
    

if __name__ == '__main__':
    Main()

