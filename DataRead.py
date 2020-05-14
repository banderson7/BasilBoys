from influxdb import InfluxDBClient
import json

dbName = 'testdb3'
db = InfluxDBClient(host='localhost', port=8086)
db.switch_database(dbName)

def getHumidity():
    results = db.query("SELECT * FROM humidity ORDER BY time DESC LIMIT 1")
    humidity = list(results.get_points(measurement="humidity"))
    percent = humidity[0]
    percent = json.dumps(percent["percent"]).split(".")[0]
    return percent[1:]

def getTemperature():
    results = db.query("SELECT fahrenheit FROM temperature ORDER BY time DESC LIMIT 1")
    temp = list(results.get_points(measurement="temperature"))
    degrees = temp[0]
    degrees = json.dumps(degrees["fahrenheit"]).split(".")[0]
    return degrees[1:]
