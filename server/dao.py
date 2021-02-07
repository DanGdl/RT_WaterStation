import sqlite3


DB_FILE_NAME = "water_stations.db"


class StationsDao:

    def __init__(self) -> None:
        super().__init__()
        try:
            db = sqlite3.connect(DB_FILE_NAME)
            cursor = db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS station_status (station_id INT,last_date TEXT,alarm1 INT,"
                           "alarm2 INT,PRIMARY KEY(station_id))")
            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print("can't create a table ", e)

    def save(self, data):
        try:
            db = sqlite3.connect(DB_FILE_NAME)
            cursor = db.cursor()
            query = str.format("INSERT OR REPLACE INTO station_status (station_id, last_date, alarm1, alarm2)"
                               " VALUES (%d, \"%s\", %d, %d)" %
                               (data.get_station_id(), data.get_date(), data.get_alarm1(), data.get_alarm2()))

            cursor.execute(query)
            db.commit()
            cursor.close()
            db.close()
        except Exception as e:
            print("can't save data to db ", e)
            db.rollback()
            db.close()
