import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()

def checkTMP():
    print ((ADC.read("P9_40")*1800) - 500)/10

while 1:
    checkTMP()
    time.sleep(1)
