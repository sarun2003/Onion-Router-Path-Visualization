import socket
import threading
from utils.logger import log_message
from utils.config import NODES

def handle_relay(client_socket):
    try:
        data = client_socket.recv(1024)
        log_message("Received encrypted data at relay node.")
        
        # Send to exit node
        exit_address = (NODES[2]["ip"], NODES[2]["port"])
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as exit_socket:
            exit_socket.connect(exit_address)
            exit_socket.sendall(data)
        log_message("Forwarded encrypted data to exit node.")
    except Exception as e:
        log_message(f"Error in relay node: {e}")
    finally:
        client_socket.close()

def start_relay_node():
    relay_node_address = (NODES[1]["ip"], NODES[1]["port"])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(relay_node_address)
        server.listen(5)
        log_message("Relay node listening...")
        while True:
            client_socket, _ = server.accept()
            thread = threading.Thread(target=handle_relay, args=(client_socket,))
            thread.start()

if __name__ == "__main__":
    start_relay_node()
