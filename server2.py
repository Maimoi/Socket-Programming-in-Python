import socket 
import pickle

a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostbyname('localhost'), 2098))

s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection to {address} successfully established!")
    m = {1: "Client" , 2: "Server"}
    message = pickle.dumps(m)
    message = bytes(f'{len(message) : <{a}}', "utf-8") + message
    client_socket.send(message)




    


