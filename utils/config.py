# Configuration for the Onion Router project

# Filepath for the shared key
SHARED_KEY_FILE = "shared_key.key"

# Node configurations
NODES = [
    {"name": "Entry Node", "ip": "127.0.0.1", "port": 8000},
    {"name": "Relay Node", "ip": "127.0.0.1", "port": 9001},
    {"name": "Exit Node", "ip": "127.0.0.1", "port": 10001},
]
