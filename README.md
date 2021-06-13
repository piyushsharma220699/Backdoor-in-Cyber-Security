# BACKDOOR IMPLEMENTATION IN PYTHON 3.X

## Introduction
Backdoor is a type of malware which is used to gain unauthorised access of a system. Basically it is difficult for the hackers to find the unsecured points of entry in a system again and again, so what they do is they try to get into a system once, where they create a backdoor (which they can use for gaining access of that system again). Also, sometimes hackers create malicious files which when executed on the client's system hacks it and provides the attacker access of the system.

## About the Code
There are two files: client.py and server.py
The attacker will run the server.py file on his system first. This will show the following on his terminal ::

![Waiting for Incoming Connections](https://github.com/piyushsharma220699/Backdoor-in-Cyber-Security/blob/main/Images/Waiting%20for%20incoming%20connections.jpg)

Then, the attacker will send the client.exe file to the client. Then once the client runs the file on his system, he will see the normal snake game implementation in front of it, which will look like this.

![Snake Game](https://github.com/piyushsharma220699/Backdoor-in-Cyber-Security/blob/main/Images/Snake_Game.jpg)

However, in the backend, the client's system will connect itself to the attacker's system and the attacker will be able to access the client's system (only till the client plays the game).

![Connected](https://github.com/piyushsharma220699/Backdoor-in-Cyber-Security/blob/main/Images/Successful%20connection.jpg)

<br><br>

_Don't forget to change the IP Address in the client.py and server.py! You can find your IP Address by executing the following command in your command prompt_

![IPv4 Address](https://github.com/piyushsharma220699/Backdoor-in-Cyber-Security/blob/main/Images/IPv4_Address.jpg)
<br><br>

## Commands
The following commands can be performed on the client system once the attacker connects to it:
1. view_cwd : Used to view the current working directory in which the client.exe file is run
2. custom_dir : Used to view the names of all the files present in a directory
3. download_files : Used to download a file from client's system
4. remove_files : Used to remove a file from the client's system
5. shutdown_client : Used to shutdown the client's system
6. restart_system : Used to restart the client's system
