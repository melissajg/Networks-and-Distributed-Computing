import socket
import ipaddress
import threading
import time
import contextlib
import errno

maxPacketSize = 1024
defaultPort = 4000 # TODO: Change this to your expected port
serverIP = 'localhost' #TODO: Change this to your instance IP

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
try:
    tcpPort = int(input("Please enter the TCP port of the host..."))
except:
    tcpPort = 0
if tcpPort == 0:
    tcpPort = defaultPort;
tcpSocket.connect((serverIP, tcpPort))

while True:
    clientMessage = bytes(input("Please type the message that you'd like to send (Or type \"exit\" to exit):\n>"), encoding='utf8')
    if clientMessage == b"exit":
        break
    #TODO: Send the message to your server
    tcpSocket.sendall(clientMessage)
   # print('Message sent to server : {}'.format(clientMessage.decode("utf-8")))
    #TODO: Receive a reply from the server for the best highway to take
    data = tcpSocket.recv(1024)
    #TODO: Print the best highway to take
    print('Received from server : {}'.format(data.decode("utf-8")))
    
tcpSocket.close();

