import telnetlib

# Honeypot IP address and port (replace with the actual IP address)
honeypot_ip = "192.168.1.10"  # Replace <honeypot_ip> with your honeypot IP
port = 2223

try:
    # Connect to the honeypot via Telnet
    connection = telnetlib.Telnet(honeypot_ip, port)
    
    # Send a command to the honeypot
    connection.write(b"whoami\n")
    output = connection.read_all()
    
    # Decode and print the response
    print(output.decode())
except Exception as e:
    print(f"Error: {e}")
