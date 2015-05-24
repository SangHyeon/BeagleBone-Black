import Adafruit_DHT
import time

sensor =  Adafruit_DHT.DHT11
pin = "P9_11"

humid, temp = Adafruit_DHT.read_retry(sensor, pin)

while 1:
    if humid is not None and temp is not None:
        print "Temp={0:0.1f}*C Humid={1:0.1f}%".format(temp, humid)
    else :
        print "Failed to get reading"
    time.sleep(1)
