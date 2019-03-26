import socket, select
import os
import sys

server_address("127.0.0.1",9000)
buf_size = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(10)

file_name=["car1.jpg", "car2.jpg"]

for x in file_name:
while true:
    
    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

    server_socket.sendto(server_address)
    print "Sending %s ..." % x

    for socket in read_sockets:
        if socket == server_socket:
            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)
        
        else 
            try:
                data = sokcet.recv(4096)

                if data:
                    txt = data.strip()

                    if txt == 'GET_IMG' :
                        with open(x,'rb') as fileopen:
                            image_data = fileopen.read()

        except:
            sock.close()
            connected_clients_sockets.remove(sock)
            continue
    server_socket.close()