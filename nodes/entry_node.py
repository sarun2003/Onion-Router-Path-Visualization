import socket
import threading
from utils.encryption_utils import create_cipher
from utils.logger import log_message
from utils.config import NODES

cipher = create_cipher()

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024)
        log_message(f"Received from client: {data.decode()}")
        encrypted_data = cipher.encrypt(data)

        # Send to relay node
        relay_address = (NODES[1]["ip"], NODES[1]["port"])
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as relay_socket:
            relay_socket.connect(relay_address)
            relay_socket.sendall(encrypted_data)
        log_message("Forwarded encrypted data to relay node.")
    except Exception as e:
        log_message(f"Error handling client: {e}")
    finally:
        client_socket.close()

def start_entry_node():
    entry_node_address = (NODES[0]["ip"], NODES[0]["port"])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(entry_node_address)
        server.listen(5)
        log_message("Entry node listening...")
        while True:
            client_socket, _ = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()

if __name__ == "__main__":
    start_entry_node()
