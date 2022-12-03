import requests
from tkinter import *

def click():
    rep = txt.get()
    r = requests.get(f"https://api.github.com/repos/{rep}") #txmxzDima/PL-Tomozov

    with open("C:\\Users\\HP\\Desktop\\12.txt", "a+") as f:
        if 'company' in r.json():
            f.write(f"'company': '{r.json()['company']}'\n")
        else:
            f.write("'company':")
            f.write("None\n")
        f.write(f"'created_at': '{r.json()['created_at']}'\n")
        if 'email' in r.json():
            f.write(f"'email': '{r.json()['email']}'\n")
        else:
            f.write("'email':")
            f.write("None\n")
        f.write(f"'id': '{r.json()['id']}'\n")
        f.write(f"'name': '{r.json()['name']}'\n")
        f.write(f"'url': '{r.json()['url']}'\n")

window = Tk()
window.title('Dmitriy Tomozov UB-22')
window.geometry('400x250')
lbl = Label(window, text='Введите репозиторий', font=('Times New Roman', 14))
lbl.grid(column=0, row=0)
btn = Button(window, text='Подтвердить', command=click)
btn.grid(column=2, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
window.mainloop()
