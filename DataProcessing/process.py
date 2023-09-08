import csv
import datetime
import time
import operator

# Function to write data to a new csv-file
def write2csv(data):
    with open("processed.csv", "w", newline="") as psd:
        writer = csv.writer(psd)
        for entry in data:
            writer.writerow(entry)


# List to store processed data
tempData = []

# Cut-off date, anything before this was for testing only
startTime = datetime.datetime(2023, 8, 20)

with open("results.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for i, row in enumerate(csv_reader):
        if i > 0:
            # Separate each aspect of date and time
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
            timestamp = time.mktime(thisDateTime.timetuple())
            if thisDateTime >= startTime:
                tempData.append(
                    [
                        row[0],
                        row[1],
                        thisDateTime.strftime("%d.%m.%Y"),
                        row[3],
                        timestamp,
                    ]
                )

    # Sort tempData by date (timestamp)
    tempDataSrt = sorted(tempData, key=operator.itemgetter(4))

    # Write it to a new csv file
    write2csv(tempDataSrt)

    print("Done")
