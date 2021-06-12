import socket, cv2, pickle,struct,imutils
# Socket Create
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 10050
socket_address = (host_ip,port)

# Socket Bind
s.bind(socket_address)

# Socket Listen
s.listen(5)
print("LISTENING AT:",socket_address)

# Socket Accept
while True:
    client_socket,addr = s.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_socket:
        cap = cv2.VideoCapture(0)

        while(cap.isOpened()):
            ret,vdo = cap.read()
            vdo = imutils.resize(vdo,width=320)
            a = pickle.dumps(vdo)
            message = struct.pack("Q",len(a))+a
            
            # Socket client
            client_socket.sendall(message)
            cv2.imshow('Server Side',vdo)
            key = cv2.waitKey(1) & 0xFF
           
            # Close client
            if key ==ord('c'):
                client_socket.close()
                break
cv2.destroyAllWindows()