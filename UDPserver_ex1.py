from socket import *
serverSocket = socket(AF_INET,SOCK_DGRAM)

serverPort= 12000
serverVariable = "10"
serverSocket.bind(("",serverPort))
myServName = "Milosz Majtyka Server"

while  True:
    clientVariable, clientAddress = serverSocket.recvfrom( 2048 )
    decodedClVar = clientVariable.decode()
    myClnName, clientAddress = serverSocket.recvfrom( 2048 )
    clientName = myClnName.decode()
    intSumVariable = int(decodedClVar) + int(serverVariable)
    sumVariable = str(intSumVariable)
    print("client name" + clientName)
    print("server name" + myServName)
    print("client val ; server val ; sum val")
    print(decodedClVar, serverVariable, sumVariable, sep=(";"))
    
    serverSocket.sendto( sumVariable.encode(), clientAddress)
    serverSocket.sendto( myServName.encode(), clientAddress)




serverSocket.close()


