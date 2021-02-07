#!/usr/bin/env python3
import os
import socket
import sys
import time


HOST = '127.0.0.1'
PORT = 1031
DELAY_TIME = 20


def setup_water_station():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    path = str.format("%s/%s" % (dirname, "resources/status2.txt"))
    while True:
        content = ""
        try:
            f = open(path, "r")
            for i in range(3):
                content += f.readline()

            f.close()
        except IOError as e:
            print("file not found, error: {0}, {1}".format(e.errno, e.strerror))

        if content:
            content = content.replace("\n", " ")
            print(content)

            try:
                s = socket.socket()
                s.connect((HOST, PORT))
                s.send(content.encode())
            except IOError as e:
                print("can't send data, error: {0}, {1}".format(e.errno, e.strerror))
            finally:
                s.close()

        time.sleep(DELAY_TIME)


if __name__ == "__main__":
    setup_water_station()
