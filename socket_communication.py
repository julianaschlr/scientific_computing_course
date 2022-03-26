import socket
# AF_INET = address family that is used to designate the type of addresses that your socket can communicate with
# AF_INET6 = for Internet Protocol v6 addresses.
# TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM;
# SOCK_STREAM is a connection-based protocol two parties have a conversation until connection is terminated
# SOCK_DGRAM is a datagram-based protocol You send one datagram and get one reply and then the connection terminates
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode()
# How to create an HTTP Request: https://www.rfc-editor.org/rfc/rfc7230
mysocket.send(cmd)

while True:
    data = mysocket.recv(600)
    if len(data) < 1:
        break
    print(data.decode())
mysocket.close()
