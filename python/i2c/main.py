import Adafruit_BBIO.GPIO as GPIO
import smbus2
import time

bus = smbus2.SMBus(2)
time.sleep(1)

SLAVE_ADDRESS = 0x40

def char_to_ascii(text):
    data = []

    for c in text:
        ascii_value = ord(c)
        data.append(ascii_value)
    
    return data

def ascii_to_char(data):
    text = ''.join([chr(i) for i in data if i > 0])
    return text

def i2c(message):
    try:
        print("===============================================\n")
        print("Message sent to ESP32: ", message)
        data = char_to_ascii(message)
        write = bus.write_i2c_block_data(SLAVE_ADDRESS,0,data)
        time.sleep(1)

        read = bus.read_i2c_block_data(SLAVE_ADDRESS, 0, 15)
        response = ascii_to_char(read)
        print("Response from ESP32: ", response)
        print("\n===============================================\n")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    while True:
        message = "Hello ESP32"
        i2c(message)
        time.sleep(1)
