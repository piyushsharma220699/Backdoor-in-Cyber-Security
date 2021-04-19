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

while 1:
    command = input(str("Type your command >>"))

    if command == "view_cwd":
        conn.send(command.encode())
        print("Command view_cwd has been executed successfully!")

        files = conn.recv(10000)
        files = files.decode()
        print("We are inside the directory named : ", files, " of the client named ", client_address)
    
    elif command == "custom_dir":
        conn.send(command.encode())
        print("Command custom_dir has been executed successfully!")

        directory = input(str("Input the directory whose files you want to see: "))
        conn.send(directory.encode())
        print("Directory name sent!")

        files = conn.recv(10000)
        files = files.decode()
        print("The files inside the directory ", directory, " are given as follows: ")
        print(files)

    else:
        print("Command NOT recognized!")
