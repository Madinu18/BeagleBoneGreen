import Adafruit_BBIO.GPIO as GPIO
import time

PIN = "P8_12"

GPIO.setup(PIN, GPIO.IN)

try:
    while True:
        if (GPIO.input(PIN) == GPIO.HIGH):
            print("HIGH")
        else :
            print("LOW")
        
        time.sleep(1)

except KeyboardInterupt:
    print("Exiting Program")

finally:
    GPIO.cleanup()
    print("GPIO cleanup done")