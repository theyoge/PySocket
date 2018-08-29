import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] I am Listening ons %s:%d" %(bind_ip,bind_port)

# Now we make another thread to handle clients

def handle_client(client_socket):
    
    # this will print what our client will send to us
    
    request = client_socket.recv(1024)
    
    print "[*] Received: %s" %request
    
    # this will send the data back to client
    client_socket.send("ACK!")
    
    client_socket.close()
    
while True:
   
    client,addr = server.accept()
    
    print "[*] Accepted connection from: %s:%d" %(addr[0],addr[1])
    
    # New thread to handle incoming data
    
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()