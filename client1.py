import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname('localhost'), 1024))
complete_info = ''
while True:
    message = s.recv(7)
    if len(message) <= 0 : 
        break
    complete_info += message.decode("utf-8")

print(complete_info)
