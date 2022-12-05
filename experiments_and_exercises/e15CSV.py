import csv

with open("sanjoseweather.csv", "r") as file:
    data = list(csv.reader(file))

date = input("Enter the day of the month (e.g. Sat 03) to get weather data for San Jose:  ")
for item in data:
    if item[0] == date:
        print(f"Temp will be {item[1]}F, weather will be {item[2]}")
