# import csv
#
# with open("weather_data1.csv") as data_file:
#     data = csv.reader(data_file)
#     tempretures = []
#     for row in data:
#         if row[1] != "temp":
#           tempretures.append(int(row[1]))
#     print(tempretures)

import pandas

data = pandas.read_csv("weather_data1.csv")
print(data["temp"])

