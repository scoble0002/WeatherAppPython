import tkinter as tk
from pip._vendor import requests
##import pip._vendor.requests
##import requests
import time

def degrees_to_cardinal(d):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = round(d / (360. / len(dirs)))
    return dirs[ix % len(dirs)]

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&APPID=11a24e577555163923af2fbf234d3f66"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'])
    low_temp = int(json_data['main']['temp_min'])
    hi_temp = int(json_data['main']['temp_max'])
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    wind_dir = json_data['wind']['deg']
    ##sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    ##sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600)) + "Sunrise: " + sunrise +"\n" + "Sunset: " + sunset +"\n"
    
    ultimate_info = condition + "\n" + str(temp) + "°F"
    ultimate_data = "\n" + "High Temp: " + str(hi_temp) + "°F" + "\n" + "Low Temp: " + str(low_temp) + "°F" +"\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "%" +"\n" + "Wind Speed: " + str(wind) + "mph" +"\n" + "Wind Direction: " + str(wind_dir) +"\n" 
    label1.config(text = ultimate_info)
    label2.config(text = ultimate_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("times", 15, "bold")
t = ("times", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack() 

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()
