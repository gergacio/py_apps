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

data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(data_list)

# avarage = sum(data_list) / len(data_list)
# print(avarage)

print(data["temp"].mean())
print(data["temp"].max())
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


