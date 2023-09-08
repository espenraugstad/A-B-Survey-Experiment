import csv
import datetime
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

plt.rcParams.update({"font.size": 22})

res = []

# Cut-off date, anything before this was for testing only
startTime = datetime.datetime(2023, 8, 20)

with open("results.csv") as file:
    reader = csv.reader(file, delimiter=",")
    for i, row in enumerate(reader):
        # Separate each aspect of date and time
        if i > 0:
            datetimeRaw = row[2].split(" ")
            date = datetimeRaw[0].split(".")
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])
            timeRaw = datetimeRaw[1].split(":")
            hh = int(timeRaw[0])
            mm = int(timeRaw[1])
            ss = int(timeRaw[2])
            # Create a datetime for this entry
            thisDateTime = datetime.datetime(year, month, day, hh, mm, ss)
            if thisDateTime >= startTime:
                res.append(
                    [
                        row[1],
                        row[3],
                    ]
                )

res_tuple = map(tuple, res)
counts = Counter(res_tuple)
print(counts)

# Convert absolute numbers to percentages
cokeA = counts[("coke", "A")] * 100 / (counts[("coke", "A")] + counts[("pepsi", "A")])
pepsiA = counts[("pepsi", "A")] * 100 / (counts[("coke", "A")] + counts[("pepsi", "A")])
cokeB = counts[("coke", "B")] * 100 / (counts[("coke", "B")] + counts[("pepsi", "B")])
pepsiB = counts[("pepsi", "B")] * 100 / (counts[("coke", "B")] + counts[("pepsi", "B")])
print(cokeB)

# Plot the results
fig, ax = plt.subplots()

cokeAbar = ax.bar(0.5, cokeA, width=1, color="#F40009", label="Coke")
ax.bar_label(cokeAbar, fmt=lambda x: "{:.1f} %".format(x), padding=3)
pepsiAbar = ax.bar(1.5, pepsiA, width=1, color="#004B93", label="Pepsi")
ax.bar_label(pepsiAbar, fmt=lambda x: "{:.1f} %".format(x), padding=3)


cokeBbar = ax.bar(3.5, cokeB, width=1, color="#F40009")
ax.bar_label(cokeBbar, fmt=lambda x: "{:.1f} %".format(x), padding=3)
pepsiBbar = ax.bar(4.5, pepsiB, width=1, color="#004B93")
ax.bar_label(pepsiBbar, fmt=lambda x: "{:.1f} %".format(x), padding=3)


ax.set_title("Cola preferences A/B-survey")
ax.set_xticks(np.arange(0, 6, 3) + 1, ("Survey version A", "Survey version B"))
ax.legend(loc="upper center", ncols=4)
ax.set_ylim(0, 100)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

plt.show()
