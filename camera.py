from picamera import PiCamera

camera = PiCamera()

def takePicture(fileName):
    filePath = '/home/pi/Documents/BasilBoys/{0}.jpg'.format(fileName)
    camera.capture(filePath)
