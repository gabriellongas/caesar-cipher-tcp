from socket import *
from caesar_cipher import *
from diffie_hellman import *
from prime import *

serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)

def start_server():
    print("Server listening\n")
    
    connectionSocket, addr = serverSocket.accept()

    g = generate_random_prime(1, 1000)
    n = generate_random_prime(1, 1000)
    server_private_key = generate_random_prime(1, 1000)

    keys = f"{g},{n}".encode()

    connectionSocket.send(keys)

    client_public_key = int(connectionSocket.recv(65000).decode())

    server_public_key = key_exchange(g, n, server_private_key)
    connectionSocket.send(str(server_public_key).encode())

    shared_key = generate_shared_key(client_public_key, server_private_key, n)
    print(f"Shared key (server): {shared_key}")

    sentence = connectionSocket.recv(65000)
    received = str(sentence, "utf-8")
    print("Received From Client (encrypted): ", received)

    decrypted = caesar_decrypt(received, shared_key)
    print("Decrypted message: ", decrypted)

    capitalizedSentence = decrypted.upper()
    print("Final message: ", capitalizedSentence)

    message_bytes = bytes(caesar_encrypt(capitalizedSentence, shared_key), "utf-8")
    connectionSocket.send(message_bytes)

    print("Sent back to Client (encrypted): ", str(message_bytes, "utf-8"))
    connectionSocket.close()

start_server()
