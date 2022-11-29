"Note: The sources I used involved the book(recommended from the lab) and help from TAs. "

import socket
"Establish Server name, IP, and Port # as well as what is being requested"

serverName = 'gaia.cs.umass.edu'
serverIP = socket.gethostbyname(serverName)
serverPort = 80
req = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

"Establishes we're using network IPv4 and that we're using a TCP socket'"
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"Creates TCP connection"
clientSocket.connect((serverIP, serverPort))
"Sends the request (all of it) into TCP connection"
clientSocket.sendall(req.encode())
"Creates loop to continue to recv/print until entire message is through"
while True:
    res = clientSocket.recv(1024)
    print(res.decode())
    if not res:
        break

