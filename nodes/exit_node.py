import socket
from utils.encryption_utils import create_cipher
from utils.logger import log_message
from utils.config import NODES

cipher = create_cipher()

def handle_exit(client_socket):
    try:
        data = client_socket.recv(1024)
        log_message("Received encrypted data at exit node.")
        
        # Decrypt data
        decrypted_data = cipher.decrypt(data)
        log_message(f"Decrypted data: {decrypted_data.decode()}")
        print(f"Decrypted data: {decrypted_data.decode()}")
    except Exception as e:
        log_message(f"Error in exit node: {e}")
    finally:
        client_socket.close()

def start_exit_node():
    exit_node_address = (NODES[2]["ip"], NODES[2]["port"])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(exit_node_address)
        server.listen(5)
        log_message("Exit node listening...")
        while True:
            client_socket, _ = server.accept()
            handle_exit(client_socket)

if __name__ == "__main__":
    start_exit_node()
