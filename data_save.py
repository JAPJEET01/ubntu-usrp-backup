import socket

def main():
    # Define the server address and port
    server_address = '127.0.0.1'  # Change this to your server's IP address
    server_port = 6000  # Change this to your server's port

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Connect to the server
            client_socket.connect((server_address, server_port))
            print("Connected to server.")
 
            # Open the IQ file in binary write mode
            with open("new.iq", "wb") as iq_file:
                # Receive data from the server and write to the IQ file
                while True:
                    data = client_socket.recv(1024)  # Receive up to 1024 bytes of data
                    if not data:
                        break  # If no more data is received, break the loop
                    iq_file.write(data)
                    # print(data)

        except ConnectionRefusedError:
            print("Connection to server refused.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()