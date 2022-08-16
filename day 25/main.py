# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].max())
#
# # Get data in a column
# print(data["condition"])
# print(data.condition)

# Get data in a row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])

# Get a particular piece of data in a row

# monday = data[data.day == "Monday"]
# print(monday.temp * 9 / 5 + 32)
#
# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
import pandas
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"].value_counts())

## OR

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_2 = pandas.DataFrame(data_dict)

data_2.to_csv("data_2.csv")