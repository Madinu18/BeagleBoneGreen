import serial
import time

uart_port = "/dev/ttyO1"
baud_rate = 9600

try:
    uart = serial.Serial(uart_port, baud_rate, timeout=1)
    print(f"Opened {uart_port} with baud rate {baud_rate}")
    
    if uart.isOpen():
        print("Init UART connection success.")
    else:
        print("Failed to init UART connection.")
        
    while True:
        message = "Hello from BBG"
        uart.write(message.encode())
        print(f"Sent: {message}")

        time.sleep(1)

        if uart.inWaiting() > 0:
            incoming_data = uart.readline().decode('utf-8').strip()
            print(f"Received from ESP32: {incoming_data}")
        
        time.sleep(2)

except Exception as e:
    print(f"Error: {e}")
finally:
    if uart.isOpen():
        uart.close()
        print(f"Closed {uart_port}")
