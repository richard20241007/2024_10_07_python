import json
import sqlite3
import requests


def create_database():
    """創建SQLite資料庫和資料表，並添加唯一索引"""
    conn = sqlite3.connect('air_quality.db')
    cursor = conn.cursor()

    # 創建空氣品質資料表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS air_quality (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site TEXT,
        county TEXT,
        pm25 REAL,
        aqi INTEGER,
        status TEXT,
        so2 REAL,
        co REAL,
        o3 REAL,
        no2 REAL,
        nox REAL,
        no REAL,
        wind_speed REAL,
        wind_direc REAL,
        publishtime TEXT,
        update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # 添加唯一索引以防止重複資料
    cursor.execute('''
    CREATE UNIQUE INDEX IF NOT EXISTS idx_site_publishtime 
    ON air_quality(site, publishtime)
    ''')

    conn.commit()
    return conn


def fetch_air_quality_data():
    """從API獲取空氣品質資料"""
    url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'

    try:
        response = requests.get(url)
        response.raise_for_status()  # 檢查是否有錯誤狀態碼
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"獲取API資料時發生錯誤: {e}")
        return None


def process_air_quality_data(data, conn):
    """處理空氣品質資料並存入資料庫"""
    if not data or 'records' not in data:
        print("錯誤: 無效的資料格式")
        return

    cursor = conn.cursor()

    # 準備 INSERT 語句，使用 INSERT OR IGNORE 來跳過重複資料
    insert_sql = '''
    INSERT OR IGNORE INTO air_quality (
        site, county, pm25, aqi, status, so2, co, o3, no2, nox, no,
        wind_speed, wind_direc, publishtime
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # 用於追蹤處理結果的計數器
    total_records = 0
    inserted_records = 0
    skipped_records = 0
    error_records = 0

    records = []
    for record in data.get('records', []):
        try:
            total_records += 1

            # 檢查該記錄是否已存在
            cursor.execute('''
                SELECT COUNT(*) FROM air_quality 
                WHERE site = ? AND publishtime = ?
            ''', (record.get('site'), record.get('publishtime')))

            if cursor.fetchone()[0] > 0:
                skipped_records += 1
                continue

            # 轉換資料型別
            pm25 = float(record.get('pm25', 0)) if record.get('pm25') else None
            aqi = int(record.get('aqi', 0)) if record.get('aqi') else None
            so2 = float(record.get('so2', 0)) if record.get('so2') else None
            co = float(record.get('co', 0)) if record.get('co') else None
            o3 = float(record.get('o3', 0)) if record.get('o3') else None
            no2 = float(record.get('no2', 0)) if record.get('no2') else None
            nox = float(record.get('nox', 0)) if record.get('nox') else None
            no = float(record.get('no', 0)) if record.get('no') else None
            wind_speed = float(record.get('wind_speed', 0)
                               ) if record.get('wind_speed') else None
            wind_direc = float(record.get('wind_direc', 0)
                               ) if record.get('wind_direc') else None

            # 直接使用API回傳的時間字串
            publishtime = record.get('publishtime', '')

            records.append((
                record.get('site'),
                record.get('county'),
                pm25,
                aqi,
                record.get('status'),
                so2,
                co,
                o3,
                no2,
                nox,
                no,
                wind_speed,
                wind_direc,
                publishtime
            ))

        except (ValueError, TypeError) as e:
            print(f"處理記錄時發生錯誤: {e}")
            error_records += 1
            continue

    try:
        cursor.executemany(insert_sql, records)
        inserted_records = cursor.rowcount
        conn.commit()

        print(f"\n資料處理完成:")
        print(f"- 總記錄數: {total_records}")
        print(f"- 成功匯入: {inserted_records}")
        print(f"- 重複跳過: {skipped_records}")
        print(f"- 處理失敗: {error_records}")

    except sqlite3.Error as e:
        print(f"資料庫錯誤: {e}")
        conn.rollback()


def check_database_status(conn):
    """檢查資料庫狀態"""
    cursor = conn.cursor()

    # 檢查總記錄數
    cursor.execute('SELECT COUNT(*) FROM air_quality')
    total_count = cursor.fetchone()[0]

    # 檢查最新資料時間
    cursor.execute('SELECT MAX(publishtime) FROM air_quality')
    latest_time = cursor.fetchone()[0]

    # 檢查各站點數量
    cursor.execute('''
        SELECT county, COUNT(*) as count 
        FROM air_quality 
        GROUP BY county 
        ORDER BY count DESC
    ''')
    county_stats = cursor.fetchall()

    print("\n資料庫狀態:")
    print(f"- 總記錄數: {total_count}")
    print(f"- 最新資料時間: {latest_time}")
    print("\n各縣市資料統計:")
    for county, count in county_stats:
        print(f"- {county}: {count} 筆")


def main():
    """主程式"""
    try:
        print("連接資料庫...")
        conn = create_database()

        print("從API獲取資料...")
        data = fetch_air_quality_data()

        if data:
            print("處理資料中...")
            process_air_quality_data(data, conn)
            check_database_status(conn)

    except Exception as e:
        print(f"發生錯誤: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
