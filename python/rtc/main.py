import subprocess

def sync_hwclock():
    try:
        subprocess.run(['sudo', 'hwclock', '-w', '-f', '/dev/rtc0'], check=True)
        print("Hardware clock synchronized successfully!")
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while synchronizing hardware clock: {e}")

def read_hwclock():
    try:
        result = subprocess.run(['sudo', 'hwclock', '--utc', '-r', '-f', '/dev/rtc0'], capture_output=True, text=True, check=True)
        
        hwclock_time = result.stdout.strip()

        words = hwclock_time.split()
        
        date = words[0]
        times = words[1]

        words = times.split('+')
        clock = words[0]
        zone = '+' + words[1]

        print(f"Date: {date}")
        print(f"Clock: {clock}")
        print(f"Zone: {zone}")
        print()

    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while reading hardware clock: {e}")
        return None

if __name__ == "__main__":
    sync_hwclock()
    try:
        while True:
            read_hwclock()
    except:
        print("Exiting Program")