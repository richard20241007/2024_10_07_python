import sqlite3
import requests


def get_data() -> list[list]:
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    datalist = []
    for items in data['records']:
        innerlist = [items['sitename'],
                     items['datacreationdate'],
                     items['county'],
                     items['aqi'],
                     items['pm2.5'],
                     items['status'],
                     items['latitude'],
                     items['longitude']]
        datalist.append(innerlist)
    return datalist


def insert_data(conn, AQI_data):
    insertSQL = """
    INSERT OR IGNORE INTO records(sitename, date, county, aqi, pm25, status, lat, lon)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """

    cursor2 = conn.cursor()
    cursor2.executemany(insertSQL, AQI_data)
    conn.commit()
    cursor2.close()


def main():
    sql = '''
    CREATE TABLE IF NOT EXISTS records (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	sitename TEXT NOT NULL,
    date TEXT,
	County TEXT,
	aqi INTEGER,
    pm25 NUMERIC,
	status TEXT,
	lat NUMERIC,
	lon NUMERIC,
    UNIQUE (sitename, date)
    );
    '''

    conn = sqlite3.connect("air_quality.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()
    AQI_data = get_data()
    insert_data(conn, AQI_data)
    conn.close()


if __name__ == "__main__":
    main()
