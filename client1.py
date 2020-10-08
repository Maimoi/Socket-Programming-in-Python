import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname('localhost'), 1024))
message = s.recv(1024)
print(message.decode("utf-8"))
