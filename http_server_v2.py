# Julien Desmangles 
# ID 40084151
# Socket programming assignment 
# Section FK-X
from socket import *
import os.path
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('\nServer ready to recieve\n')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    # print(sentence)
    for line in sentence.splitlines():
        if ".html" in line:
            filename = line.replace("GET", "")
            filename = filename.replace("/", "")
            filename = filename.replace("HTTP", "")
            filename = filename.replace("1.1", "")
            filename = filename.replace(" ", "")
            print('Filename: ' + filename)
            # path = "C:/Users/Julie/OneDrive/Desktop/VS_code/COEN_366/" + filename
            path = os.getcwd() + "/" + filename
            # path = path + ".html"
            print(path)
            if(os.path.exists(path)):
                print (line + '\n' + "file found")
                file = open(path, "r")
                data = file.read()
                httpResponse = "HTTP/1.1 200 OK \nContent-Type: text/html\r\n\r\n" + data
                # httpResponseBytes = bytes(httpResponse, 'utf-8')
                connectionSocket.send(httpResponse.encode('utf-8'))
                # connectionSocket.send(data.encode('utf-8'))

    capitalizedSentence = sentence.upper()
    # print(capitalizedSentence)
    # connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
