CREATE TABLE IF NOT EXISTS air_quality (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_name TEXT,
    county TEXT,
    AQI INTEGER,
    PM25 REAL,
    PM10 REAL,
    status TEXT,
    import_date TEXT,
    UNIQUE(site_name, import_date)
);




INSERT OR IGNORE INTO air_quality (site_name, county, AQI, PM25, PM10, status, import_date)
VALUES ('City A', 'County A', 75, 35, 50, 'Good', '2023-10-12 10:00:00');

SELECT * FROM air_quality