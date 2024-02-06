import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240206.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squerrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squerrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squerrels_count)
print(black_squerrels_count)

data_dict = {
    "Fur Colors": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squerrels_count, black_squerrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")