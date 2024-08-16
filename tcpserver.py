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

    # Diffie-Hellman parameters
    # p = generate_random_prime()
    # g = generate_random_prime()
    # server_private_key = generate_random_prime(1, p-1)

    p = 7
    g = 23
    server_private_key = 41

    # Send p and g to the client
    #connectionSocket.send(f"{p},{g}".encode())

    # Receive the client's public key
    client_public_key = int(connectionSocket.recv(65000).decode())

    # Calculate server's public key and send it to the client
    server_public_key = key_exchange(p, g, server_private_key)
    connectionSocket.send(str(server_public_key).encode())

    # Generate the shared key
    shared_key = generate_shared_key(client_public_key, server_private_key, p)
    print(f"Shared key (server): {shared_key}")

    # Communication loop
    sentence = connectionSocket.recv(65000)
    received = str(sentence, "utf-8")
    print("Received From Client (encrypted): ", received)

    decrypted = caesar_decrypt(received, shared_key % 26)
    print("Decrypted message: ", decrypted)

    capitalizedSentence = decrypted.upper()
    print("Final message: ", capitalizedSentence)

    message_bytes = bytes(caesar_encrypt(capitalizedSentence, shared_key % 26), "utf-8")
    connectionSocket.send(message_bytes)

    print("Sent back to Client (encrypted): ", str(message_bytes, "utf-8"))
    connectionSocket.close()

start_server()
