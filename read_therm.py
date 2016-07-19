import os
from serial import Serial, serialutil
from time import sleep

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

sensor_file = "/sys/bus/w1/devices/28-000006209d48/w1_slave"

def read_sensor_file():
    with open(sensor_file) as f:
        lines = f.readlines()
    return lines

#return string 
def read_temp():
    lines = read_sensor_file()
    #index of temp data
    eq_pos = lines[1].find('t=')
    if eq_pos != -1:
        temp_str = lines[1][eq_pos + 2:]
        return str(float(temp_str) / 1000.0)
