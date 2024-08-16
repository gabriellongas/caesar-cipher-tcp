from socket import *
from caesar_cipher import *
from diffie_hellman import *
from prime import *

serverName = '127.0.0.1'
serverPort = 1300

clientSocket = socket(AF_INET, SOCK_STREAM)

def start_client():
    clientSocket.connect((serverName, serverPort))

    keys = clientSocket.recv(65000).decode().split(',')

    g, n = map(int, keys)
    client_private_key = generate_random_prime(1, 1000)

    client_public_key = key_exchange(g, n, client_private_key)
    clientSocket.send(str(client_public_key).encode())

    server_public_key = int(clientSocket.recv(65000).decode())

    shared_key = generate_shared_key(server_public_key, client_private_key, n)
    print(f"Shared key (client): {shared_key}")

    sentence = input("Input lowercase sentence: ")
    encrypted = caesar_encrypt(sentence, shared_key)
    clientSocket.send(bytes(encrypted, "utf-8"))

    modifiedSentence = clientSocket.recv(65000)
    text = str(modifiedSentence, "utf-8")
    decrypted = caesar_decrypt(text, shared_key)
    print("Received from Server (decrypted): ", decrypted)
    clientSocket.close()

start_client()
