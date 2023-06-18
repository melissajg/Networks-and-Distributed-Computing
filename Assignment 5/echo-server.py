# echo-server.py
# python3 C:\Users\mjgai\Desktop\echo-server.py
import socket
import sys

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

# Create a TCP/IP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (validate_ip(), validate_port())
#Do NOT hard code the server address and port number
socket.bind(server_address)

# Listen for incoming connections
socket.listen(1)

while True:
    # Wait for a connection
    print('Server started...\n')
    connection, client_addy = socket.accept()
    try:
        print('Connected to {} at port {}.'.format(client_addy[0], client_addy[1]))
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            str_data = data.decode("utf-8")
            if data == b"Q":
                break
            if data:
                print('Received from {} : {}'.format(client_addy[0], str_data))
                mod_data = bytes(str_data.upper(), encoding='utf8')
                connection.sendall(mod_data)
                print('Message modified and sent back to client.')
            else:
                print('No data recieved from client :', client_addy[0])
                break
        print('Connecttion close to {} at port {}. \n'.format(client_addy[0], client_addy[1]))
    except Exception:
        print("ERROR OCCURRED")

print('Done.')
connection.close()

