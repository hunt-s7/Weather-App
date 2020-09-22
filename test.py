import tkinter as tk
from tkinter import font
import requests


window=tk.Tk()
window.title('Weather Monitor')

HEIGHT=400
WIDTH=500


def get_weather(city):
    weather_key='922d7a822d61475682cc51a401e09162'
    url='http://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'metric'}
    response=requests.get(url,params=params)
    weather=response.json()
    label['text']=weather_report(weather)
    

def weather_report(weather):
    try:
        name=weather['name']
        w=weather['weather'][0]['description']
        temp=weather['main']['temp']
        country=weather['sys']['country']
        return "City:"+name+'\n'+"Weather:"+w+"\n"+"Temperature(^C):" + str(temp)+"\n"+"Country:"+country
    except:
        return "There was some problem\nin retrieving your data!\nCheck your City Again!"



canvas=tk.Canvas(window,height=HEIGHT,width=WIDTH)
canvas.pack()

bk_image=tk.PhotoImage(file='landscape.png')
bk_label=tk.Label(window,image=bk_image)
bk_label.place(relwidth=1,relheight=1)

frame1=tk.Frame(window,bg='#B3E5F4',bd=3)
frame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)

city=tk.Entry(frame1,font=('Lucida Fax',12))
city.place(relx=0,rely=0,relwidth=0.7,relheight=1)

button=tk.Button(frame1,text='Get Weather',command=lambda : get_weather(city.get()),font=('Lucida Fax',10))
button.place(relx=0.7,rely=0,relwidth=0.3,relheight=1)

frame2=tk.Frame(window,bg='#B3E5F4',bd=3)
frame2.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.5)

label=tk.Label(frame2,font=('Lucida Fax',15),justify='left',anchor='nw',bg='white')
label.place(relwidth=1,relheight=1)


window.mainloop()
