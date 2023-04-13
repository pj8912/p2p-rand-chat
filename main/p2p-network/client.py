import socket
import threading
import sys

class Client:
  
    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((addr, 7000))
        
        i_thread = threading.Thread(target=self.send_message)
        i_thread.daemon = True
        i_thread.start()
        
        while True:
            data = self.receive_message()
            if not data:
                print("*"*20, "server failed", "*"*20)
                break
            elif data[0:1] == b"\x11":
                print("Got peers!")
                self.update_peers(data[1:])
            

    def receive_message(self):
        try:
            data = self.s.recv(1024)
            return data
        except KeyboardInterrupt:
            self.send_disconnect_signal()


    def update_peers(self, peers):
        p2p.peers = str(peers, "utf-8").split(','1)[-1]
    
    def send_message(self)L:
        try:
            self.sock.send("join".encode("utf-8"))
        except KeyboardInterrupt as e:
            self.send_disconnect_signal()
            return
    

    def send_disconnect_signal(self):
        print("Disconnected from the server")
        self.sock.send("q".encode("utf-8"))
        sys.exit()


