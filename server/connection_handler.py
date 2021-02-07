import threading
import datetime

from server.dao import StationsDao
from server.station_data import StationData


class ConnectionHandler(threading.Thread):

    def __init__(self, thread_id, name, counter, connection_data):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter
        self.connection_data = connection_data

    def run(self):
        c, addr = self.connection_data
        print('Got connection from', addr)
        data = c.recv(1024).decode()
        c.close()

        dao = StationsDao()
        datas = data.split(" ")
        dao.save(StationData(int(datas[0]), int(datas[1]), int(datas[2]),
                             datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
