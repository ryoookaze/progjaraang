import socket
import sys
import threading
import os
from thread import *

TCP_IP = "127.0.0.1"
TCP_PORT = 8502
BUFFERSIZE = 4096
server_path = "./serverfolder/"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if os.path.exists(server_path):
    os.mkdir(server_path)

def Main():
    print"Waiting for connection"
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(5)
    print "Server Started"
    conn, addr = sock.accept()
    while True:
        print "Terhubung ke" + str(addr)
        t = threading.Thread(target=RetrievingFile, args=("retrThread", conn))
        t.start()
    sock.close()

def RetrievingFile(name, sock):
    if not os.path.exists(server_path):
        os.mkdir(server_path)
        filename = sock.recv(BUFFERSIZE)
        if os.path.isfile(filename):
                userResponse = sock.recv(BUFFERSIZE)
                if userResponse[:2] == 'OK':
                    with open(filename,'rb') as file:
                        bytesToSend = file.read(BUFFERSIZE)
                        sock.send(bytesToSend)
                        print "File name :", filename
                        print "File size", bytesToSend
        sock.close()

if __name__ == "__main__":
    Main()




