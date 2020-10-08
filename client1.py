import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname('localhost'), 1024))
complete_info = ''
while True:

    #take only 7 bytes of the message from the server
    message = s.recv(7)

    #if the length of the message is less than or equal to 0, jsut break the loop
    if len(message) <= 0 : 
        break
    #add the message to the complete information string
    complete_info += message.decode("utf-8")

#finally print the string
print(complete_info)
