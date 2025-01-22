import socket
import threading

# Set the timeout for socket connection
TIMEOUT = 1
open_ports = []

# Function to scan individual ports
def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
    except socket.error:
        pass
    finally:
        sock.close()

# Function to start scanning ports with multiple threads
def scan_ports(target, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Main function to handle user input and execute the scan
def main():
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    print(f"Scanning ports on {target_ip} from {start_port} to {end_port}...")

    scan_ports(target_ip, start_port, end_port)

    if not open_ports:
        print("No open ports found.")
    else:
        print("\nOpen ports found:")
        for port in open_ports:
            print(f"Port {port} is open")

if __name__ == "__main__":
    main()

