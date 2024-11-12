import csv
import pandas

# with open('Day25_CSVData&Pandas\weather_data.csv') as rawfile:
#     data = []
#     for line in rawfile.readlines():
#         data.append(line.strip('\n'))
# print(data)

# with open('Day25_CSVData&Pandas\weather_data.csv') as rawfile:
#     data = csv.reader(rawfile)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except Exception as e:
#             print(f'Exception {e}, skipping row with values {row}.')
#     # print(temperatures)

# data = pandas.read_csv('Day25_CSVData&Pandas\weather_data.csv')
# print(round(data.temp.mean(), 3))
# print(data.temp.max())
# print(data[data.temp == data.temp.max()])
# temp_fahrenheit = data[data.day == 'Monday'].temp*1.8 + 32
# print(temp_fahrenheit)
# data_dict = {
#     "students": ['Amy', 'James', 'Angela'],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)

# SQUIRREL ANALYSIS SECTION
# squirrel_path = r'Day25_CSVData&Pandas\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
# data = pandas.read_csv(squirrel_path)
# print(data["Primary Fur Color"].value_counts().to_csv(
#     'Day25_CSVData&Pandas/squirrel_fur_data.csv'))
