import os
import time


def get_stations_dict():
    path = 'stations.csv'
    stations_dict = {}
    dirs = os.listdir('data')
    for d in dirs:
        if d == path:
            with open('data/' + path, 'r') as f:
                data = []
                for line in f:
                    line = line.replace('\n', '').split(';')
                    stations_dict[line[1]] = line[0]
    return stations_dict


def input_datetime(msg):
    while 1:
        st = input(msg)
        try:
            time.strptime(st, "%Y-%m-%d")
            return st
        except ValueError:
            print('Incorrect format')


def get_data_set(file_name):
    data_set = []

    with open('data/' + file_name, 'r') as f:
        mean_temperature = 'actual_mean_temp'
        mean_temperature_index = 0
        actual_precipitation = 'actual_precipitation'
        actual_precipitation_index = 0
        date = 'date'
        date_index = 0

        names = f.readline()
        names = names.split(',')

        for n in names:
            if n == mean_temperature:
                break
            else:
                mean_temperature_index += 1

        for n in names:
            if n == actual_precipitation:
                break
            else:
                actual_precipitation_index += 1

        for n in names:
            if n == date:
                break
            else:
                date_index += 1

        for line in f:
            weather = {}
            line = line.split(',')
            weather[date] = line[date_index]
            weather[mean_temperature] = line[mean_temperature_index]
            weather[actual_precipitation] = line[actual_precipitation_index]
            data_set.append(weather)
        return data_set


def get_weather(data_set, needed_date):
        for d in data_set:
            if d['date'] == needed_date:
                return d


def get_file_name_by_city(city_name, stations_dict):
    file_name = ''
    city = ''
    for k, v in stations_dict.items():
        if k.startswith(city_name):
            file_name = v + '.csv'
            city = k
            break
    return [file_name, city]


def fahrenheit_to_celsius(temp):
    return round((temp-32)*5/9, 1)


stations = get_stations_dict()


while 1:
    city = input('enter city name: ')
    date = input_datetime('enter date: ')
    data = get_file_name_by_city(city, stations)
    file_name = data[0]
    city = data[1]
    data_set = get_data_set(file_name)
    weather = get_weather(data_set, date)
    print('Weather in {city_name}: temperature: {temp} degrees, precipitation: {precipitation}'
          .format(city_name=city, temp=fahrenheit_to_celsius(int(weather['actual_mean_temp'])),
                  precipitation=weather['actual_precipitation']))






