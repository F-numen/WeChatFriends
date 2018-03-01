import json
import requests
import csv

def getlnglat(address):
    u = 'http://api.map.baidu.com/geocoder/v2/?'
    output = 'json'
    ak = 'NmSp0mBhxxZtEG4uZfuj14tabphIjrED'
    url = u + 'address=' + address + '&output=json&ak=' + ak
    req = requests.get(url)

    return req.json()

with open('point.json','w') as file:
    with open('friend-city.csv','r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if reader.line_num == 1:
                continue
            b = line[0]
            c = line[1]
            a = getlnglat(b)
            lng = a['result']['location']['lng']
            lat = a['result']['location']['lat']
            str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) +'},'
            file.write(str_temp)


if __name__ == '__main__':
    req = getlnglat('沈阳')

