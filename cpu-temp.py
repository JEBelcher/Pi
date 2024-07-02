import os
import time
# Python3 terminal version
# Display the CPU temperature every 30 Seconds
def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=",""))
while True:
    os.system('clear')
    print(" Refresh every 30 Seconds Ctrl Z to stop")

    print("============ CPU Temperature ===========\n")
    print("                ",measure_temp())
    print("========================================\n")
    time.sleep(30)
# Uses a terminal session to provide temerature information
# using the vcgencmd measure_temp function in a loop.
# (c) J E Belcher
