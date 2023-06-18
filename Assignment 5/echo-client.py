# echo-client.py
# python3 C:\Users\mjgai\Desktop\echo-client.py
import socket
import sys
import pickle

def validate_port():
    try:
        port = int(input("Enter Port # between 0 and 65535: "))
        if port >= 0 and port <= 65535:
            return port
        else:
            print("Port # must be within 0 and 65535")
            validate_port()
    except Exception:
        print("Invalid Port Number")
        validate_port()

def validate_ip():
    ip = input("Enter IP in Format x.x.x.x: ")
    try:
        if ip == "localhost":
            return ip
        if ip == None or ip == "":
            print("Invalid Port Address")
            validate_ip()
        splitParts = ip.split(".")
        if len(splitParts) != 4:
            print("Invalid Port Address")
            validate_ip()
        else:
            for x in splitParts:
                i = int(x)
                if i < 0 or i > 255:
                    print("Invalid Port Address")
                    validate_ip()
        return ip
    except Exception:
        print("Invalid Port Address")
        validate_ip()

server_address = (validate_ip(), validate_port())
# Create a TCP/IP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(server_address)

while True:
    try:
        # Send data
        message = bytes(input("\nEnter Message or type Q to quit: "), encoding='utf8')
        if message == b"Q":
            break
        socket.sendall(message)
        print('Message sent to server : {}'.format(message.decode("utf-8")))
        data = socket.recv(1024)
        print('Received from server : {}'.format(data.decode("utf-8")))
    except Exception:
        print("ERROR OCCURRED")
    

print('Done.')
socket.close()
