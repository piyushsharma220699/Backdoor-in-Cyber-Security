import socket
import os

client_socket = socket.socket()
port_number = 9999

server_address = "192.168.43.239"
client_socket.connect((server_address, port_number))

print("Connected Successfully!")