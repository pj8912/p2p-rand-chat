import socket
import threading
import sys

class Server:


    def __init__(self, msg, bootnode_address):
        self.msg = msg
        self.bootnode_address = bootnode_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connections = []
        self.peers = []
        self.sock.bind('0.0.0.0', 0)
        self.sock.listen(1)
        print("running...")
        self.run()
        self.register_to_bootnode()
        self.run()



    def register_to_bootnode(self):
        try:
            with self.sock as bootnode:
                bootnode.connect(self.bootnode_address)
                bootnode.send("join".encode("utf-8"))
        except Exception as e:
            print("Can't reach bootnode")



    def handler(self, connection, a):
        while True:
            data = connection.recv(1024)
            for connection in self.connections:
                if data and data.decode('utf-8')[0].lower() == "q":
                    self.disconnect(connection, a)
                    return 
                elif data and data.decode('utf-8') == "req":
                    conenction.send(self.msg)


    def disconnect(self, connection ,a ):
        self.connections.remove(connection)
        self.peers.remove(a)
        connection.close()
        print("-"*50)


    def run(self):
        while True:
            connection, a  = self.sock.accept()
            self.peers.append(a)
            c_thread = threading.Thread(target=self.handler, args=(connection,a))
            c_thread.daemon = True
            c_thread.connections.append(connection)
            print("\n", a, "connected", "\n")


        
