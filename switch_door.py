import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_8", GPIO.IN)

if GPIO.input("P8_8") == True:
    print "Door is close..."
else:
    print "Door is OPEN!"
