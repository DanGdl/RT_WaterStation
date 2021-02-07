#!/usr/bin/env python3

import socket
from server.connection_handler import ConnectionHandler

HOST = '127.0.0.1'
PORT = 1031
CONNECTIONS_QUEUE = 10


def setup_server():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(CONNECTIONS_QUEUE)
    while True:
        c, addr = s.accept()
        t = ConnectionHandler(1, "Thread-1", 1, (c, addr))
        t.start()


if __name__ == "__main__":
    setup_server()
