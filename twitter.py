from twython import Twython
from influxdb import InfluxDBClient

dbName = 'testdb3'
db = InfluxDBClient(host='localhost', port=8086)
db.switch_database(dbName)

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def Tweet(image, message):
    image = open('/home/pi/Documents/BasilBoys/%s.jpg' % image, 'rb')
    response = twitter.upload_media(media=image)
    media_id = [response['media_id']]
    twitter.update_status(status=message, media_ids=media_id)
    print("Tweeted: %s" % message)
