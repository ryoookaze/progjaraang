import socket
import sys
import threading
import os
from thread import *

TCP_IP = "127.0.0.1"
TCP_PORT = 5000
client_path = "D:\Ryan\Kuliah\Progjar\tcp-multi\clientfolder"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)