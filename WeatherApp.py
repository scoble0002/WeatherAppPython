import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    
    ##added &units=imperialinto api might ne in wrong place
    api = "api.openweathermap.org/data/2.5/weather?q=" + city +"units=imperial&APPID=11a24e577555163923af2fbf234d3f66"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    low_temp = int(json_data['main']['temp-min'] - 273.15)
    hi_temp = int(json_data['main']['temp-max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    
    ultimate_info = condition + "\n" + str(temp) + "F"
    ultimate_data = "\n" + "High Temp: " + str(hi_temp) + "\n" + "Low Temp: " + str(low_temp) +"\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) +"\n" + "Wind Speed: " + str(wind) +"\n" + "Sunrise: " + sunrise +"\n" + "Sunset: " + sunset +"\n"
    label1.config(text = ultimate_info)
    label2.config(text = ultimate_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack() 

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()