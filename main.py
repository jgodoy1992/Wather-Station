import requests
import datetime as dt
import tkinter as tk

def get_url(city):
    key = "d47b26938dbf84eb0b30416705616b68"
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + key
    response = requests.get(url).json()
    return response

def get_weather():
    try:
        city=entry1.get()
        res=get_url(city)
        desc.config(text=f"{res['weather'][0]['description']}")
        ctemp.config(text=f"{res['main']['temp']} ºC")
        ftemp.config(text=f"{res['main']['feels_like']} ºC")
        mintemp.config(text=f"{res['main']['temp_min']} ºC")
        maxtemp.config(text=f"{res['main']['temp_max']} ºC")
        hum.config(text=f"{res['main']['humidity']} %")
        sr.config(text=f"{dt.datetime.utcfromtimestamp(res['sys']['sunrise']+res['timezone'])}")
        ss.config(text=f"{dt.datetime.utcfromtimestamp(res['sys']['sunset'] + res['timezone'])}")
        print("Connection successful")
    except:
        print("OOP! something's not right")

root=tk.Tk()

canvas=tk.Canvas(root,width=400, height=780)
canvas.pack()

label1=tk.Label(root, text="Weather Station")
label1.config(font=("times", 20))
canvas.create_window(200,10, window=label1)

label2=tk.Label(root, text="Enter city name")
label2.config(font=("times", 15))
canvas.create_window(200,50, window=label2)

entry1=tk.Entry(root)
canvas.create_window(200, 90, window=entry1)

label0=tk.Label(root, text="Description")
label0.config(font=("times", 15))
canvas.create_window(200,130, window=label0)

desc=tk.Label(root)
desc.config(font=("times",15))
canvas.create_window(200,170, window=desc)

label3=tk.Label(root, text="Current temperature")
label3.config(font=("times", 15))
canvas.create_window(200,210, window=label3)

ctemp=tk.Label(root)
ctemp.config(font=("times", 15))
canvas.create_window(200,250, window=ctemp)

label4=tk.Label(root, text="Feels like")
label4.config(font=("times", 15))
canvas.create_window(200,290, window=label4)

ftemp=tk.Label(root)
ftemp.config(font=("times", 15))
canvas.create_window(200,330, window=ftemp)

label5=tk.Label(root, text="Min temperature")
label5.config(font=("times", 15))
canvas.create_window(200,370, window=label5)

mintemp=tk.Label(root)
mintemp.config(font=("times", 15))
canvas.create_window(200,410, window=mintemp)

label6=tk.Label(root, text="Max temperature ")
label6.config(font=("times", 15))
canvas.create_window(200,450, window=label6)

maxtemp=tk.Label(root)
maxtemp.config(font=("times", 15))
canvas.create_window(200,490, window=maxtemp)

label7=tk.Label(root, text="Relative humidity")
label7.config(font=("times", 15))
canvas.create_window(200,530, window=label7)

hum=tk.Label(root)
hum.config(font=("times", 15))
canvas.create_window(200,570, window=hum)

label8=tk.Label(root, text="Sunrise")
label8.config(font=("times", 15))
canvas.create_window(200,610, window=label8)

sr=tk.Label(root)
sr.config(font=("times", 15))
canvas.create_window(200,650, window=sr)

label9=tk.Label(root, text="Sunset")
label9.config(font=("times", 15))
canvas.create_window(200,690, window=label9)

ss=tk.Label(root)
ss.config(font=("times", 15))
canvas.create_window(200,730, window=ss)

button1=tk.Button(text="Get Weather", command=get_weather)
canvas.create_window(200, 750, window=button1)


root.mainloop()