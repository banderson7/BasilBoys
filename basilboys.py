import camera
import datetime
import twitter
import DataRead

plantDate = datetime.date(2019,3,12)
currentDate = datetime.date.today();
delta = currentDate - plantDate
imageName = '%s-Day-%s' % (currentDate, delta.days)
humidity = DataRead.getHumidity()
temperature = DataRead.getTemperature()
message = 'Basil Day {0}, Humidity: {1}%, Temperature: {2}'.format(delta.days, humidity, temperature)
camera.takePicture(imageName)
twitter.Tweet(imageName, message)
#print(message)