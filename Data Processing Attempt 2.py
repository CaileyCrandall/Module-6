import fileinput
from datetime import datetime

# get the current date and time
current_datetime = datetime.now()
current_date = current_datetime.strftime('%Y-%m-%d')
current_time = current_datetime.strftime('%H:%M:%S')

# Initialize variables with default values
date = current_date
time = current_time

with fileinput.input(files='data2.txt') as file:
    for line in file:
        data = line.split()
        if len(data) == 6:
            _, _, store, item, cost, payment = data
            print("{0}\t{1}".format(item, cost))
    print("{0}\t{1}".format(date, time))
