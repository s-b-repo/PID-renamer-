import os
import random
import time
import psutil
from setproctitle import setproctitle

def random_hex_string(length=12):
    """Generates a random hexadecimal string of the given length."""
    return ''.join(random.choice('0123456789abcdef') for _ in range(length))

def find_process_by_name(process_name):
    """Finds and returns a process PID by its name."""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return proc.info['pid']
    return None

def continuously_rename_process(pid):
    """Continuously renames the Python process (self) to a random hex string."""
    try:
        while True:
            hex_name = random_hex_string(12)
            # Set the current process name
            setproctitle(hex_name)
            print(f"Process (PID: {pid}) renamed to: {hex_name}")
            time.sleep(1)  # Sleep for 1 second before renaming again
    except KeyboardInterrupt:
        print("\nProcess renaming stopped.")

if __name__ == "__main__":
    process_name_to_find = "python3"  # Example process name to search for
    pid = find_process_by_name(process_name_to_find)

    if pid:
        print(f"Found process '{process_name_to_find}' with PID: {pid}")
        # Now run the continuous renaming on the current process
        continuously_rename_process(pid)
    else:
        print(f"No process found with the name '{process_name_to_find}'")
