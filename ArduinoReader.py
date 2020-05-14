#!/usr/bin/env python3

import serial
from influxdb import InfluxDBClient

dbName = 'testdb3'
awsDBName = 'basilboys'

ser = serial.Serial('/dev/ttyACM0', 9600)
db = InfluxDBClient(host='localhost', port=8086)
awsDB = InfluxDBClient(host='3.16.158.54', port=8086)

db.switch_database(dbName)
awsDB.switch_database(awsDBName)

def GetCelcius(temps):
    bothTemps = temps.split(',')
    celcius = bothTemps[0]
    celcius = celcius.split(" ")[1]
    return celcius

def GetFahrenheit(temps):
    bothTemps = temps.split(',')
    fahrenheit = bothTemps[1]
    fahrenheit = fahrenheit.split(" ")[1]
    return fahrenheit

def GetHumidity(temps):
    allValues = temps.split(',')
    humidity=allValues[2]
    humidity = humidity.split(" ")[1]
    return humidity

def GetLightLevel(temps):
    allValues = temps.split(',')
    light = allValues[3]
    light = light.split(" ")[1]
    return light

def GetTempJSON(c, f, l, h):
    return [
            {
            "measurement": "temperature",
            "fields": {
                "fahrenheit": f,
                "celcius": c
            }
            },
            {
                "measurement": "light",
                "fields":{
                    "level": l
                    }
            },
            {
                "measurement": "humidity",
                "fields":{
                    "percent": h
                    }
            },
        ]

while True:
    buffer = (ser.readline().strip()).decode('utf-8')
    jsonBody = GetTempJSON(GetCelcius(buffer), GetFahrenheit(buffer), GetLightLevel(buffer), GetHumidity(buffer))
    print(jsonBody)
    db.write_points(jsonBody)
    awsDB.write_points(jsonBody)
