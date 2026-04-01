import os
import time

def get_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        temp = int(f.read()) / 1000
    return f"{temp:.1f}C"

def get_memory():
    with open("/proc/meminfo") as f:
        lines = f.readlines()
    total = int(lines[0].split()[1])
    available = int(lines[2].split()[1])
    used = total - available
    percent = (used / total) * 100
    return f"{percent:.1f}% used"

def get_disk():
    stat = os.statvfs("/")
    total = stat.f_blocks * stat.f_frsize
    free = stat.f_bfree * stat.f_frsize
    used = total - free
    percent = (used / total) * 100
    return f"{percent:.1f}% used"

def get_uptime():
    with open("/proc/uptime") as f:
    	uptime = float(f.read().split()[0])
    minutes = int(uptime // 60) % 60
    hours = int(uptime  // 3600)
    return f"{hours}h {minutes}m"

while True:
    os.system("clear")

    print("Pi Health Report")
    print("-" * 20)
    print(f"CPU Temp:  {get_cpu_temp()}")
    print(f"Memory:    {get_memory()}")
    print(f"Disk:      {get_disk()}")
    print(f"Uptime:    {get_uptime()}")

    time.sleep(30)
