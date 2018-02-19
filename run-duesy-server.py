import socket
import sys
from threading import Thread
import pickle

import Structures

mainDueDateOrg = Structures.DueDateOrganizer()

class DuesyInstance(object):
    def __init__(self, port_num):
        self.server = ThreadedServer('localhost',port_num)
        print("Initializing Server...")
        self.server.start()
        

class ThreadedServer(Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host,self.port))
    
    def listenToClient(self, client, add):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    print("Received: '%s'"%data)
                    response = data
                    client.send(response)
                else:
                    raise error('Client Disconnected')
            except:
                client.close()
                return False
    
    def run(self):
        self.sock.listen(3)
        while True:
            client, add = self.sock.accept()
            client.settimeout(60)
            Thread(target= self.listenToClient, args=(client,add)).start()

def main():

    print("Creating Instance...")
    inst = DuesyInstance(10000)
    print("Created Instance")

if __name__ == '__main__':
    main()