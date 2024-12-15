import socket
from utils.logger import log_message

def send_request(server_address, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(server_address)
            client_socket.sendall(message.encode())
            log_message(f"Message sent to {server_address}: {message}")
            print("Message sent successfully.")
    except Exception as e:
        log_message(f"Failed to send message to {server_address}: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    entry_address = ("127.0.0.1", 8000)
    send_request(entry_address, "Hello, Tor Network!")
