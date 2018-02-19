import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connectiong to %s port %s' % server_address)
sock.connect(server_address)

try:
    message = "This is a message. It will be repeated"
    print("sending %s" % message)
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('Closing Socket')
    sock.close