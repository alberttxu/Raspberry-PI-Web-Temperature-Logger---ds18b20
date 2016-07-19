#!/usr/bin/env python
from time import strftime 
from read_therm import read_temp

log_file = "/var/www/html/temp_data.dat"

if __name__ == '__main__':
    temp = read_temp()
    with open(log_file, 'a') as f:
        f.write(strftime("%H:%M " + temp + '\n'))
