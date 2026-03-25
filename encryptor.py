import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("\n[+] Success: 'secret.key' generated!")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_path):
    key = load_key()
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print(f"\n[+] Success: '{file_path}' ENCRYPTED.")

def decrypt_file(file_path):
    key = load_key()
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"\n[+] Success: '{file_path}' DECRYPTED.")

# --- Simple Menu ---
print("1. Generate Key\n2. Encrypt File\n3. Decrypt File")
choice = input("Select (1/2/3): ")

if choice == '1':
    generate_key()
elif choice == '2':
    filename = input("Enter file name: ")
    encrypt_file(filename)
elif choice == '3':
    filename = input("Enter file name: ")
    decrypt_file(filename)