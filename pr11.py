from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox
from tkinter import messagebox
import json
import requests
from pprint import pprint

def clicked():
    str=txt1.get()
    if str!='':
        user_data = request.get(str).json()
        pprint(user_data)

        us_data={'company':None,'created_at':'2015-08-03T17:55:43Z','email':None,'id'=13629408,'name':'Kubernetes','url':'https://github.com/Automattic/wp-calypso'}
        for i in user_data:
         if i=="company" or i=="id" or i=='created_at' or i=='email' or i=='name' or i=='url':
             us_data[i]=user_data[i]
        with open("data_file.json", "w") as write_file:
            json_dump(us_data,write_file)

window = Tk()
window.title(" приложение ")
window.geometry('400x250')

txt1 = Entry(window, width=50)
txt1.grid(column=0, row=1)

btn1 = Button(window, text=" Ok ", command=clicked1)
btn.grid(column=1, row=1)

window.mainloop()