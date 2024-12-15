from cryptography.fernet import Fernet
from utils.config import SHARED_KEY_FILE

# Load the shared key
def load_key():
    with open(SHARED_KEY_FILE, "rb") as key_file:
        return key_file.read()

# Create encryption/decryption cipher
def create_cipher():
    key = load_key()
    return Fernet(key)
