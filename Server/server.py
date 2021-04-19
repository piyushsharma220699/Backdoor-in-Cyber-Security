import socket
import os

server_socket = socket.socket()
hostname = socket.gethostname()
port_number = 9999
# IP Address of PC = 192.168.43.239

server_socket.bind((hostname, port_number))

print("Server is currently running at ", hostname, "and at the portnumber ", port_number)

print("Waiting for any incoming connections!")

server_socket.listen(1)
conn, client_address = server_socket.accept()

print(client_address, " has connected to the server successfully!")

# Connection has been established successfully