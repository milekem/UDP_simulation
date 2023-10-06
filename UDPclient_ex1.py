from socket import *

clientSocket = socket(AF_INET,SOCK_DGRAM)

serverName="localhost"
serverPort= 12000
myClnName = "Milosz Majtyka Client"
number = input("Input an integer from 1 - 100: ")

if int(number) > 100 or int(number) < 1 :
    print("wrong value")
    exit(0)
else:   
    clientSocket.sendto( number.encode(),(serverName, serverPort))
    clientSocket.sendto( myClnName.encode(),(serverName, serverPort))
    sumVariable, serverAddres = clientSocket.recvfrom(2048)
    myServName, serverAddres = clientSocket.recvfrom(2048)
    decMyServName = sumVariable.decode()
    print( decMyServName, sumVariable)

    clientSocket.close()


