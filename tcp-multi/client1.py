import socket
import sys
import threading
import os
from thread import *

TCP_IP = "127.0.0.1"
TCP_PORT = 8501
client_path = "./clientfolder1/"
image_name = ["lambo1.jpg", "lambo2.jpg"]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def changefolder():
    os.chdir(client_path)

def Main():
    s = socket.socket()
    s.connect((TCP_IP, TCP_PORT))

    print "1. List image 2. Request Image 3. Send Image"
    input_req = raw_input(">")
    if(input_req == '1'):
        msg = sock.recv(buffsize)
        print msg
    
    elif(input_req == '2'):
        if not os.path.exists(client_path):
            os.mkdir(client_path)
            changefolder()
            filename = raw_input("Filename? -> ")
            if filename != 'q':
                s.send(filename)
                data = s.recv(buffsize)
                if data[:6] == 'EXISTS':
                    filesize = long(data[6:])
                    message = raw_input("File exists, " + str(filesize)+"Bytes, download? (Y/N)? -> ")
                    if message == 'Y':
                        s.send("OK")
                        f = open('new_'+filename, 'wb')
                        data = s.recv(buffsize)
                        totalRecv = len(data)
                        f.write(data)
                        while totalRecv < filesize:
                            data = s.recv(buffsize)
                            totalRecv += len(data)
                            f.write(data)
                            print "{0:.2f}".format((totalRecv/float(filesize))*100)+"% Done"
                        print "Download Complete!"
                        f.close()
                else:
                    print "File Does Not Exist!"
            s.close()
    elif(input_req=='3'):
        name = raw_input("Masukkan nama file -> ")
        sock.send("START {}" . format(name))
        size = os.stat(nama).st_size
        fp = open(name,'rb')
        i = fp.read()
        sent = 0
        for x in i:
            sock.send(x)
            sent += 1
        fp.close()
    
if __name__ == '__main__':
    Main()

