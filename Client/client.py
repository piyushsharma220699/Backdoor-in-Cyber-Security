import socket
import os

client_socket = socket.socket()
port_number = 9999

server_address = "192.168.43.239"
client_socket.connect((server_address, port_number))

print("Connected Successfully!")

while 1:
    command = client_socket.recv(1024)
    command = command.decode()
    print("Command received successfully!")
    
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        client_socket.send(files.encode())
        print("Command view_cwd sent correctly!")
    else:
        print("Leave")