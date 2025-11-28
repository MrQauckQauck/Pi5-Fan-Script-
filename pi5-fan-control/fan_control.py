#!/usr/bin/env python3
import subprocess
import time

# Enable the Raspberry Pi 5 built-in fan
try:
    subprocess.run(['echo', '1'], capture_output=True)
    with open('/sys/class/thermal/cooling_device0/cur_state', 'w') as f:
        f.write('1')
    print("Fan turned ON")
    
    # Keep the script running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    with open('/sys/class/thermal/cooling_device0/cur_state', 'w') as f:
        f.write('0')
    print("Fan turned OFF")
except Exception as e:
    print(f"Error: {e}")
