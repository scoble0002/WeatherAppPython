import tkinter as tk
from pip._vendor import requests
##import pip._vendor.requests
##import requests
import time

##Changes Azimuth degrees to Compass direction
def getCompass(d):
    dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    ix = round(d / (360. / len(dirs)))
    return dirs[ix % len(dirs)]

##Calls API and reads json file
def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&APPID=11a24e577555163923af2fbf234d3f66"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'])
    real_feel = int(json_data['main']['feels_like'])
    low_temp = int(json_data['main']['temp_min'])
    hi_temp = int(json_data['main']['temp_max'])
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    wind_dir = json_data['wind']['deg']

    
    ##Displays weather Info
    ultimate_info = condition + "\n" + str(temp) + "°F"
    ultimate_data = "\n" + "Feels Like: " + str(real_feel) + "°F" + "\n" + "High Temp: " + str(hi_temp) + "°F" + "\n" + "Low Temp: " + str(low_temp) + "°F" +"\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "%" +"\n" + "Wind Speed: " + str(wind) + " mph" +"\n" + "Wind Direction: " + getCompass(wind_dir) +"\n" 
    label1.config(text = ultimate_info)
    label2.config(text = ultimate_data)

##Creates and formats Canvas Widget
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.config(bg="black")

##Creates and formats Label Widget
label = tk.Label(canvas, text="Enter City, State(if US), 2 Digit Country Code", bg="black", fg="white" ,font = ("times", 20, "bold"))
label.pack(pady=(10, 10)) 

##Sets text variables for label and label2
f1 = ("times", 15, "bold")
f2 = ("times", 35, "bold")

##Creates textfield for user input
textfield = tk.Entry(canvas, font = f2)
textfield.pack()
textfield.focus()
textfield.bind('<Return>', getWeather)

##Formats display area for ultimate_data and ultimate_info
label1 = tk.Label(canvas, bg="black", fg="white", font = f2)
label1.pack() 
label2 = tk.Label(canvas, bg="black", fg="white", font = f1)
label2.pack()

tk.mainloop()