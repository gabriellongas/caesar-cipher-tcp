from socket import *
from caesar_cipher import *

serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(5)


def start_server():
    print ("Server listening\n")

    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(65000)
    received = str(sentence,"utf-8")
    print ("Received From Client: ", received)

    decrypted = caesar_decrypt(received, 3)
    print ("Decrypted message: ", decrypted)

    capitalizedSentence = decrypted.upper()

    message_bytes = bytes(capitalizedSentence, "utf-8")

    connectionSocket.send(message_bytes)

    print ("Sent back to Client: ", capitalizedSentence)
    connectionSocket.close()


start_server()