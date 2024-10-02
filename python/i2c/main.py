import subprocess
import re

def detect_i2c_devices(bus_number=1):
    try:
        # Run the i2cdetect command
        command = f"i2cdetect -y {bus_number}"
        output = subprocess.check_output(command, shell=True, text=True)

        # Print the raw output from i2cdetect
        print(output)

        # Find all I2C addresses in the output
        addresses = []
        for line in output.splitlines():
            # Match the hex addresses (e.g., 0x03)
            matches = re.findall(r'0x[0-9A-Fa-f]{2}', line)
            if matches:
                addresses.extend(matches)

        return addresses

    except subprocess.CalledProcessError as e:
        print(f"Error executing i2cdetect: {e}")
        return []

if __name__ == "__main__":
    bus_number = 1  # Change this if using a different I2C bus
    print(f"Scanning I2C bus {bus_number} for devices...\n")
    devices = detect_i2c_devices(bus_number)

    if devices:
        print("Detected I2C devices at addresses:")
        for address in devices:
            print(address)
   
