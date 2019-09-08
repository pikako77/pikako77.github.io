import os
import csv


city_csv = os.path.join('..','Resources', 'cities.csv')


city_id=[]
city=[]
cloudiness=[]
country=[]
date=[]

humidity=[]
lat=[]
lon=[]
max_temp=[]
wind_speed=[]


with open(city_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        city_id.append(row[0])
        city.append(row[1])
        cloudiness.append(row[2])
        country.append(row[3])
        date.append(row[4])
        humidity.append(row[5])
        lat.append(row[6])
        lon.append(row[7])
        max_temp.append(row[8])
        wind_speed.append(row[9])

# print(len(city_id))
# print(header)
# print(city_id[0])



for i in range (len(city_id)):
    print("<tr>")
    print(f"   <td> {city_id[i]} </td>")
    print(f"   <td> {city[i]} </td>")
    print(f"   <td> {cloudiness[i]} </td>")
    print(f"   <td> {country[i]} </td>")
    print(f"   <td> {date[i]} </td>")
    print(f"   <td> {humidity[i]} </td>")
    print(f"   <td> {lat[i]} </td>")
    print(f"   <td> {lon[i]} </td>")
    print(f"   <td> {max_temp[i]} </td>")
    print(f"   <td> {wind_speed[i]} </td>")
    print("</tr>")
