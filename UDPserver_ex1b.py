from socket import *
from sys import getsizeof
serverSocket = socket(AF_INET,SOCK_DGRAM)

serverPort= 12000
serverSocket.bind(("",serverPort))
myServName = "Milosz Majtyka Server"

while  True:
    file_name, clientAddress = serverSocket.recvfrom( 2048 )
    decoded_fn = file_name.decode()
    if decoded_fn != "pan_tadeusz.txt":
        print("no such file in server directory")
    else:
        print("file found, file transfer started")
        #one char is one byte, so I have to rea 2048 chars to a string 
        with open(decoded_fn, encoding = "utf8") as f:
           for i in f:
                contents = f.read(987)
                print(clientAddress)
                serverSocket.sendto( contents.encode(), clientAddress)
    f.close()


"""while  True:
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



"""
serverSocket.close()


