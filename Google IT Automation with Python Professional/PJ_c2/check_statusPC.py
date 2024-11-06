# Disk Usage
import shutil
# CPU
import psutil

def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free/du.total*100
  print(f"disk usage: {free} %")
  return free > 20

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  print(f"cpu usage: {usage} %")
  return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
  print("ERROR!!")
else:
  print("Everything OK!!")
