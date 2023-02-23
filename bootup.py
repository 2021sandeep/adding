import time
import subprocess

def get_boot_time():
    # Get the boot time from the dumpsys activity service
    boot_time_str = subprocess.check_output(["adb", "shell", "dumpsys", "activity", "service", "dump", "--proto"])
    lines = boot_time_str.splitlines()
    for line in lines:
        if b"long bootTime=" in line:
            boot_time = int(line.split(b"=")[1].rstrip(b";")) / 1000.0
            return boot_time
    raise Exception("Unable to get boot time from dumpsys")

start_time = time.time()
boot_time = get_boot_time()
end_time = time.time()

print("The boot-up time of the Android device is %.2f seconds." % (end_time - start_time - boot_time))
