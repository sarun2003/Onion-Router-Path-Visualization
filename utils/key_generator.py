from cryptography.fernet import Fernet

# Generate and save a shared key
def generate_key():
    key = Fernet.generate_key()
    with open("shared_key.key", "wb") as key_file:
        key_file.write(key)

if __name__ == "__main__":
    generate_key()
