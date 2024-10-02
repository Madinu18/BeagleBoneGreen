import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC
import time
import random

PWM_PIN = "P8_13"
ANALOG_PIN = "P9_39"

ADC.setup()

PWM.start(PWM_PIN, 0, 1000)

try:
    while True:
        analog_value = ADC.read(ANALOG_PIN)

        duty_cycle = analog_value * 100

        voltage_value = analog_value * 3.3

        PWM.set_duty_cycle(PWM_PIN, random.uniform(0,100))

        print(f"Voltage Value: {voltage_value:.2f} volt | Duty Cycle: {duty_cycle:.2f}%")

        time.sleep(1);
except:
    print("Exiting program")
finally:
    PWM.stop(PWM_PIN)
    PWM.cleanup()
