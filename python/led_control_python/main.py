import Adafruit_BBIO.GPIO as GPIO
import time

RED_LED = "P8_9"
GREEN_LED = "P8_10"
BLUE_LED = "P8_11"

def led_blink(pin):
     GPIO.setup(pin, GPIO.OUT)

     GPIO.output(pin, GPIO.HIGH)
     time.sleep(1)
     GPIO.output(pin, GPIO.LOW)
     time.sleep(1)

try :
     while True:
          led_blink(RED_LED)
          led_blink(GREEN_LED)
          led_blink(BLUE_LED)
except KeyboardInterrupt:
     print("Exiting program")
finally:
     GPIO.cleanup()
     print("GPIO cleanup done")
