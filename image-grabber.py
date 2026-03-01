import threading
from scanner import Scanner
import time
import string
import os

with open("config.txt", "r") as file:
    lines = file.readlines()

def get_removable_drives():
    drives = []
    for letter in string.ascii_uppercase:
        drive = letter + ":\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives

def monitor_usb(scanner_class, target_folder, dest_folder):
    seen_drives = set()
    while True:
        current_drives = set(get_removable_drives())
        new_drives = current_drives - seen_drives

        for drive in new_drives:
            full_path = os.path.join(drive, target_folder)
            s = scanner_class(full_path, dest_folder)
            t = threading.Thread(target=s)
            t.start()

        seen_drives = current_drives
        time.sleep(5)

if __name__ == "__main__":
    dest = lines[1]
    src = lines[3]
    t = threading.Thread(target=monitor_usb, args=(Scanner, "images", dest))
    t.daemon = True
    t.start()