from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_file(file_path, password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    with open(file_path, 'rb') as file:
        plaintext = file.read()

    # Agregamos un vector de inicialización (IV)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Aplicamos el padding a los datos
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    plaintext_padded = padder.update(plaintext) + padder.finalize()

    ciphertext = encryptor.update(plaintext_padded) + encryptor.finalize()

    with open(file_path + ".enc", 'wb') as encrypted_file:
        encrypted_file.write(salt + iv + ciphertext)
def decrypt_file(encrypted_file_path, password):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        data = encrypted_file.read()

    salt = data[:16]
    ciphertext = data[16:]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    cipher = Cipher(algorithms.AES(key), modes.CFB(), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(encrypted_file_path[:-4], 'wb') as decrypted_file:
        decrypted_file.write(plaintext)

# Uso
archivo_a_encriptar = "ces.txt"
password = "tu_contrasena_secreta"

encrypt_file(archivo_a_encriptar, password)
# decrypt_file(archivo_a_encriptar + ".enc", password)
