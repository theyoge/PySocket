import socket

target_host = '127.0.0.1'
target_port = 80

# here we create a socket object

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# this is used for sending some data
client.sendto("hiHellohiHello",(target_host,target_port))

# this is used for receiving some data
data, addr = client.recvfrom(4096)

print data