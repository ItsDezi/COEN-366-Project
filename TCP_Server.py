#Beshoi Khair ID 
#Julien Desmangles ID 40084151
#COEN 366 project
#TCP Server script

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
    for line in sentence.splitlines():
        if ".html" in line:

            path = os.getcwd() + "/" + filename
            if(os.path.exists(path)):
                print (line + '\n' + "file found")
                file = open(path, "r")
                data = file.read()
                httpResponse = "HTTP/1.1 200 OK \nContent-Type: text/html\r\n\r\n" + data
                connectionSocket.send(httpResponse.encode('utf-8'))

    capitalizedSentence = sentence.upper()
    connectionSocket.close()