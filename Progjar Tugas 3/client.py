import socket
import os
import sys
import glob
from os import listdir
from os.path import isfile, join

client_path = "./client/"
host = '127.0.0.1'
port = 5000
image_list = []
mypath = "./"

s = socket.socket()
s.connect((host, port))
#completePath = os.path.join(client_path, f)
print("DO for Download, UP for Upload, OUT for Exit")
input_req = raw_input(">")


def Main():
    if(input_req == 'DO'):
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        print(onlyfiles)
        filename = raw_input("Filename? -> ")
        if filename != 'q':
            s.send(filename)
            data = s.recv(1024)
            if data[:6] == 'EXISTS':
                filesize = long(data[6:])
                message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
                if message == 'Y':
                    client_path = "./client/"
                    completePath = os.path.join(client_path, filename)
                    s.send("OK")
                    f = open(completePath, 'wb')
                    data = s.recv(1024)
                    totalRecv = len(data)
                    f.write(data)
                    while totalRecv < filesize:
                        data = s.recv(1024)
                        totalRecv += len(data)
                        f.write(data)
                        print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
                    print "Download Complete!"

            else:
                print "File Does Not Exist!"
    
    if(input_req == 'UP'):
        return uploadToServer()
    
    if(input_req == 'OUT'):
        s.close()
        sys.exit()

def uploadToServer():
        filename = raw_input("Filename? -> ")
        if filename != 'q':
            s.send(filename)
            data = s.recv(1024)
            if data[:6] == 'EXISTS':
                filesize = long(data[6:])
                message = raw_input("File exists, " + str(filesize) +"Bytes, upload? (Y/N)? -> ")
                if message == 'Y':
                    s.send("OK")
                    f = open('new_'+filename, 'wb')
                    data = s.recv(1024)
                    totalRecv = len(data)
                    f.write(data)
                    while totalRecv < filesize:
                        data = s.recv(1024)
                        totalRecv += len(data)
                        f.write(data)
                        print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
                    print "Upload Complete!"
                    
            else:
                print "File Does Not Exist!"

    

if __name__ == '__main__':
    Main()