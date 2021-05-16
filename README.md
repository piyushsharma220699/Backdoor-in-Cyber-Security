# Backdoor implementation in Python 3.x
There are two files: client.py and server.py
The attacker will run the server.py file on his system.
Then, the attacker will send the client.exe file to the client. Then once the client runs the file on his system, he will see the normal snake game implementation in front of it. However, in the backend, the client's system will connect itself to the attacker's system and the attacker will be able to access the client's system (only till the client plays the game).

The following commands can be performed on the client system once the attacker connects to it:
1. view_cwd : Used to view the current working directory in which the client.exe file is run
2. custom_dir : Used to view the names of all the files present in a directory
3. download_files : Used to download a file from client's system
4. remove_files : Used to remove a file from the client's system
5. shutdown_client : Used to shutdown the client's system
6. restart_system : Used to restart the client's system
