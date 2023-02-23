import subprocess

def get_boot_time():
    output = subprocess.check_output(["adb", "shell", "dumpsys", "activity", "|", "grep", "TotalTime"])
    total_time = int(output.decode().split()[1])
    return total_time

if __name__ == '__main__':
    boot_time = get_boot_time()
    print(f"Boot time: {boot_time} milliseconds")