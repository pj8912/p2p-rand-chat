import sys
from client import * 
from server import *
import time
import socket


class p2p:
    peers = []


def get_peers_from_bootnode(bootnode_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((bootnode_address, 7000))

    sock.send("req".encode("utf-8"))
    data  = sock.recv(1024)
    sock.close()

    if data:
        peer_list = data.decode("utf-8").split(",")
        p2p.peers = [peer for peer in peer_list if peer]


def main():
    bootnode_address = ""
    msg = "test".encode("utf-8")
    while True:
        try:
            print("connecting....")
            print("\n")
            time.sleep(2)
            get_peers_from_bootnode(bootnode_address)
            for peer in p2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

                try:
                    server = Server(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    main()

