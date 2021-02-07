
class StationData:

    def __init__(self, station_id, alarm1, alarm2, date):
        self.station_id = station_id
        self.alarm1 = alarm1
        self.alarm2 = alarm2
        self.date = date

    def __str__(self) -> str:
        return str.format("StationData: stationId = %d, alarm1 = %d, alarm2 = %d, date = %s" %
                          (self.station_id, self.alarm1, self.alarm2, self.date))

    def get_station_id(self):
        return self.station_id

    def get_date(self):
        return self.date

    def get_alarm1(self):
        return self.alarm1

    def get_alarm2(self):
        return self.alarm2