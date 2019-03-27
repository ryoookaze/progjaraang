import socket
import sys
import threading
import os
from thread import *


TCP_IP = "127.0.0.1"
TCP_PORT = 9000
server_path = "D:\Ryan\Kuliah\Progjar\tcp-multi\serverfolder"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def Clientcon():
    sock.listen(5)
    print"Waiting for connection"
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(5)
    print "Server Started"
    while True:
        conn, addr = sock.accept()
        print "Terhubung ke" + str(addr)
        t = threading.Thread(target=RetrievingFile, args=("retrThread", conn))
        t.start()
    sock.close()

def RetrievingFile(name, sock):
    if not os.path.exists(server_path):
        os.mkdir(server_path)
        filename = sock.recv(4096)
        if os.path.isfile(filename):
                userResponse = sock.recv(4096)
                if userResponse[:2] == 'OK':
                    with open(filename,'rb') as file:
                        bytesToSend = file.read(4096)
                        sock.send(bytesToSend)
                        print "File name :", filename
                        print "File size", bytesToSend
        sock.close()

if __name__ == "__clientcon__":
    Clientcon()



