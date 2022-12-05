def get_average_temps():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()

    temps = data[1:]
    temps = [float(i) for i in temps]

    average_local = sum(temps) / len(temps)
    return average_local


average = get_average_temps()
print(average)
