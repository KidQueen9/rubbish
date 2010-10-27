#!/usr/bin/env python

# privoxy log file cleaner

import sys
import tempfile
from datetime import date, timedelta

# log entries within 'num_days' days will be kept
num_days = 2
# log file path
file_path = 'D:\home\privoxy-3.0.16\privoxy.log'
# abbr string -> int month dict
month_abbr2int = {}
for i in range(1, 13):
    month = date(date.today().year, i, 1)
    month_abbr2int[month.strftime('%b')] = i

days_delta = timedelta(days = num_days)
start_date = date.today() - days_delta    # entries logged before 'start_date' will be removed
start_month, start_day = start_date.strftime('%b %d').split(' ')
start_month = month_abbr2int[start_month]
start_day = int(start_day)

f = open(file_path, 'r+b')

while True:
    prev_pos = f.tell()
    line = f.readline()
    if not line: break
    str_month, str_day = line.split(' ', 2)[:2]
    entry_date = date(start_date.year, month_abbr2int[str_month], int(str_day))
    if entry_date >= start_date: break
    #str_month, str_day = line.split(' ', 2)[:2]
    #month = month_abbr2int[str_month]
    #day = int(str_day)
    #if start_month > month:
    #    continue
    #if (start_month == month and start_day <= day) or start_month < month:
    #    break

if not line:
    print "No log entries need to be removed."
    sys.exit(1)

f.seek(prev_pos)
temp_file = tempfile.SpooledTemporaryFile()
for line in f: temp_file.write(line)
f.close()
f = open(file_path, 'wb')
temp_file.seek(0)
for line in temp_file: f.write(line)

f.close()
temp_file.close()
