import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()

while 1:
    print ADC.read("P9_38")
    time.sleep(1)
