#import the socket module
import socket

#create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the servert to the client 
s.bind((socket.gethostbyname('localhost'),1024))

#listen to the client 
s.listen(5)


while True:

    client_socket, address = s.accept()
    print(f"Conncetion established  to {address} successfully!")


    client_socket.send(bytes("Socket Programming in Python", "utf-8"))

    #close the connection
    client_socket.close()

