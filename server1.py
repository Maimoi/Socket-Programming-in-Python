import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname('localhost'),1024))
s.listen(5)
while True:
    client_socket, address = s.accept()
    print(f"Conncetion established  to {address} successfully!")
    client_socket.send(bytes("Socket Programming", "utf-8"))

