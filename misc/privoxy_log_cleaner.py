#!/usr/bin/env python

# privoxy log file cleaner

from datetime import date, timedelta

# log entries within 'num_days' days will be kept
num_days = 2
# log file path
file_path = 'D:\home\privoxy-3.0.16\sandbox\privoxy.log'
# abbr string -> int month dict
months = {}
for i in range(1, 13):
    month = date(date.today().year, i, 1)
    months[month.strftime('%b')] = i

days_delta = timedelta(days = num_days)
start_date = date.today() - days_delta    # entries logged before 'start_date' will be removed

f = open(file_path, 'r+b')

while True:
    prev_pos = f.tell()
    line = f.readline()
    if not line: break;
    str_month, str_day = line.split(' ', 2)[:2]
    log_date = date(start_date.year, months[str_month], int(str_day))
    if start_date <= log_date: break
    
f.close()



