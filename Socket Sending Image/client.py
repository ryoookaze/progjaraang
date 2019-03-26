import os
import time
import sys
import socket

HOST = "127.0.0.1"
PORT = 9000

server_address("127.0.0.1",9000)
buf_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_connect(server_address)

while true:
    