import socket
import sys
import threading
import os
from thread import *

TCP_IP = "127.0.0.1"
TCP_PORT = 9000
client_path = "D:\Ryan\Kuliah\Progjar\tcp-multi\clientfolder"
image_name = ["lambo1.jpg", "lambo2.jpg"]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def Main():
    sock.connect((TCP_IP, TCP_PORT))
    if os.path.exists(client_path):
        os.mkdir(client_path)
        os.chdir(client_path)

    filename = raw_input("Filename? -> ")
    if filename != 'q':
            sock.send(filename)
            data = sock.recv(4096)
            if data[:6] == 'EXIST':
                filesize = long(data[6:])
                pesan = raw_input("File sudah ada, " + str(filesize)+\
                "Bytes, unggah? (Y/N)? -> ")
            
                if pesan == 'Y':
                    sock.send('OK')
                    data = os.join.path(client_path, filename)
                    f = open(data, 'wb')
                    data = sock.recv(4096)
                    jumlahTerima = len(data)
                    f.write(data)
                    while jumlahTerima < filesize:
                        data = sock.recv(4096)
                        jumlahTerima += len(data)
                        f.write(data)
            
            else:
                    print"File tidak ada"
    sock.close()
if __name__ == "__main__":
    Main()

