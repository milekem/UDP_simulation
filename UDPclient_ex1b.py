from socket import *

clientSocket = socket(AF_INET,SOCK_DGRAM)

serverName="localhost"
serverPort= 12000
file_name= "pan_tadeusz.txt"


#one char is one byte, so I have to rea 2048 chars to a string 
clientSocket.sendto( file_name.encode(),(serverName, serverPort))

while True:
    sent_contents, serverAddres = clientSocket.recvfrom(2048)
    decoded_sc = sent_contents.decode()
    print(decoded_sc)
    print('-----------------------------------')
    






""" clientSocket.sendto( number.encode(),(serverName, serverPort))
    clientSocket.sendto( myClnName.encode(),(serverName, serverPort))
    sumVariable, serverAddres = clientSocket.recvfrom(2048)
    myServName, serverAddres = clientSocket.recvfrom(2048)
    decMyServName = sumVariable.decode()
    print( decMyServName, sumVariable)
"""
clientSocket.close()


