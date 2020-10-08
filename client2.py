import socket 
import  pickle
a = 10
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname('localhost'),2098))

while True:
    complete_info = b''
    rec_msg = True
    while True:
        message = s.recv(16)
        if rec_msg:
            print(f"The length of the messag = {message[:a]}")
            x = int(message[:a])
            rec_msg= False

        complete_info += message
        if len(complete_info) - a == x:
            print("Recieved the complete info")
            print(complete_info[a:])
            m = pickle.loads(complete_info[a:])
            print(message)
            rec_msg = True
            complete_info = b''
    print(complete_info)

 
