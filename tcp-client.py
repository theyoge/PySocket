import socket

target_host = "www.google.com"
target_port = 80

# here we create a socket object

try:
     client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     print "Socket successfully created"
except socket.error as err:
     print "Socket creation failed with error %s" %(err)
     

# default port for socket
port = 80
try:
     target_host = socket.gethostbyname('www.google.com')
except socket.gaierror: 
     print "There was an error resolving the host"
     sys.exit()
     
# here we try to connect to client

client.connect((target_host,target_port))

print "The socket has successfully connected to google \
on port == %s" %(target_host)
