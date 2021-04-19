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
        print("Command has been executed successfully!")

        files = conn.recv(10000)
        files = files.decode()
        print("We are inside the directory named : ", files, " of the client named ", client_address)
    else:
        print("Command NOT recognized!")
