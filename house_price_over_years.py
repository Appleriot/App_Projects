import csv
import matplotlib.pyplot as plt
import datetime

filename = "City_MedianRentalPrice_3Bedroom.csv"

date = datetime.datetime.strptime('2010 120', '%Y %j')
date = datetime.datetime(2010, 4, 30, 0, 0)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    new = []
    for row in reader:
        state_name = str(row[1])
        coutry_name = str(row[4])
        prices = str(row[91:])

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(date, prices, c='red', alpha=0.5)

# Format plot
title = "Average Hosue price over ten years"
ax.set_title(title, fontsize=20)
ax.set_xlabel('Time', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('House price', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

