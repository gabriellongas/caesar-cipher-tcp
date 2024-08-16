from socket import *
from caesar_cipher import *
from prime import *

serverName = '127.0.0.1'
serverPort = 1300

clientSocket = socket(AF_INET, SOCK_STREAM)


def start_client():
    #clientSocket.connect((serverName,serverPort))

    sentence = input("Input lowercase sentence: ")
    encrypted = caesar_encrypt(sentence, 3)

    clientSocket.send(bytes(encrypted, "utf-8"))

    modifiedSentence = clientSocket.recv(65000)
    text = str(modifiedSentence,"utf-8")
    print ("Received from Make Upper Case Server: ", text)
    clientSocket.close()

start_client()