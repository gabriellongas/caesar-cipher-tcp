from socket import *
from caesar_cipher import *
from diffie_hellman import *
from prime import *

serverName = '127.0.0.1'
serverPort = 1300

clientSocket = socket(AF_INET, SOCK_STREAM)

def start_client():
    clientSocket.connect((serverName, serverPort))

    # Receive p and g from the server
    # p, g = map(int, clientSocket.recv(65000).decode().split(','))
    # client_private_key = generate_random_prime(1, p-1)

    p = 7
    g = 23
    client_private_key = 33

    # Calculate client's public key and send it to the server
    client_public_key = key_exchange(p, g, client_private_key)
    clientSocket.send(str(client_public_key).encode())

    # Receive server's public key
    server_public_key = int(clientSocket.recv(65000).decode())

    # Generate the shared key
    shared_key = generate_shared_key(server_public_key, client_private_key, p)
    print(f"Shared key (client): {shared_key}")

    # Communication loop
    sentence = input("Input lowercase sentence: ")
    encrypted = caesar_encrypt(sentence, shared_key % 26)
    clientSocket.send(bytes(encrypted, "utf-8"))

    modifiedSentence = clientSocket.recv(65000)
    text = str(modifiedSentence, "utf-8")
    decrypted = caesar_decrypt(text, shared_key % 26)
    print("Received from Server (decrypted): ", decrypted)
    clientSocket.close()

start_client()
