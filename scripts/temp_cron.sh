#!/bin/bash
/home/pi/bin/logger.py
/home/pi/bin/plot_temp

hour=$(date +%H)
minute=$(date +%M)

if [ $hour == 23 ] && [ $minute == 59 ]; then
    cp /var/www/html/temp.png /var/www/html/logs/`date +%Y-%m-%d`.png
    truncate -s 0 /var/www/html/temp_data.dat
fi
