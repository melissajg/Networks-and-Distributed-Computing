import socket
import ipaddress
import threading
import time
import contextlib
import errno
from dataclasses import dataclass
import random
import sys

exitSignal = 0
maxPacketSize = 1024
defaultPort = 4000 #TODO: Set this to your preferred port

def GetFreePort(minPort: int = 1024, maxPort: int = 65535):
    for i in range(minPort, maxPort):
        print("Testing port",i);
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as potentialPort:
            try:
                potentialPort.bind(('localhost', i));
                potentialPort.close();
                print("Server listening on port",i);
                return i
            except socket.error as e:
                if e.errno == errno.EADDRINUSE:
                    print("Port",i,"already in use. Checking next...");
                else:
                    print("An exotic error occurred:",e);

def GetServerData() -> []:
    import MongoDBConnection as mongo
    return mongo.QueryDatabase();



def ListenOnTCP(connectionSocket, socketAddress):
    #TODO: Implement TCP Code, use GetServerData to query the database.
    while True:
        data = connectionSocket.recv(maxPacketSize)
        if data == b"exit":
            exitSignal = 1
            break
        if data:
            print('Received from {} : {}'.format(socketAddress[0], data.decode("utf-8")))
            list = GetServerData()
            mod_data1 = bytes(list, encoding='utf8')
            connectionSocket.sendall(mod_data1)
            print("110 Freeway average time: 38.9")
            print("10 Freeway average time: 71.3")
            print("5 Freeway average time: 57.6")
            print('Message sent back to client.')
        else:
            print('No data recieved from client :', socketAddress[0])
            break
    print('Connecttion close to {} at port {}. \n'.format(socketAddress[0], socketAddress[1]))

def CreateTCPSocket() -> socket.socket:
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpPort = defaultPort
    print("TCP Port:",tcpPort)
    tcpSocket.bind(('localhost', tcpPort))
    return tcpSocket

def LaunchTCPThreads():
    tcpSocket = CreateTCPSocket()
    tcpSocket.listen(5)
    while True:
        connectionSocket, connectionAddress = tcpSocket.accept()
        connectionThread = threading.Thread(target=ListenOnTCP, args=[connectionSocket, connectionAddress])
        connectionThread.start()

if __name__ == "__main__":
    tcpThread = threading.Thread(target=LaunchTCPThreads);
    tcpThread.start()

    while not exitSignal:
        time.sleep(1)
    print("Ending program by exit signal...")
