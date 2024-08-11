import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Received message: {data}")

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)

    print("Server listening on port 12345...")

    while True:
        # Wait for a connection from a client
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
