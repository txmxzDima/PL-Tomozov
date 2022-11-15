from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton


def calculator():
    if combo.get() == "+":
        lb1.configure(text=int(spin.get()) + int(spin1.get()))
    elif combo.get() == "-":
        lb1.configure(text=int(spin.get()) - int(spin1.get()))
    elif combo.get() == "*":
        lb1.configure(text=int(spin.get()) * int(spin1.get()))
    elif combo.get() == "/":
        lb1.configure(text=int(spin.get()) / int(spin1.get()))


def push():
    if selected.get() == 0: messagebox.showinfo("Первый", "Вы выбрали первый вариант")
    if selected.get() == 1: messagebox.showinfo("Второй", "Вы выбрали второй вариант")
    if selected.get() == 2: messagebox.showinfo("Третий", "Вы выбрали третий вариант")


def download():
    with open('text.txt', 'r') as file:
        text.delete(1.0, END)
        text.insert(1.0, file.read())
    file.close()


def save():
    with open('text.txt', 'w') as file1:
        file1.write(text.get(1.0, END))
    file1.close()


window = Tk()
window.title("Томозов Дмитрий Юрьевич УБ-22")
window.geometry("480x300+500+150")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Первая")
tab_control.add(tab2, text="Вторая")
tab_control.add(tab3, text="Третья")
tab_control.pack(expand=1, fill='both')

var = IntVar()
var.set(0)
spin = Spinbox(tab1, from_=-100000, to=100000, width=10, justify="center", textvariable=var)
spin.grid(column=0, row=0)
combo = Combobox(tab1, justify="center", width=5)
combo["values"] = ("+", "-", "*", "/")
combo.current(0)
combo.grid(column=1, row=0)
var1 = IntVar()
var1.set(0)
spin1 = Spinbox(tab1, from_=-100000, to=100000, width=10, justify="center", textvariable=var1)
spin1.grid(column=2, row=0)
btn = Button(tab1, text="=", command=calculator)
btn.grid(column=3, row=0)
lb1 = ttk.Label(tab1, text="0")
lb1.grid(column=4, row=0)

selected = IntVar()
selected.set(0)
rad1 = Radiobutton(tab2, text="Первый", value=0, variable=selected)
rad2 = Radiobutton(tab2, text="Второй", value=1, variable=selected)
rad3 = Radiobutton(tab2, text="Третий", value=2, variable=selected)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn1 = Button(tab2, text="Нажми", command=push)
btn1.grid(column=0, row=1)

text = scrolledtext.ScrolledText(tab3, width=50, height=10, bg="white", fg="black")
text.grid(row=0, column=0, columnspan=2, padx=35)
btn2 = Button(tab3, text="Загрузить", command=download)
btn2.grid(row=1, column=0, pady=10)
btn3 = Button(tab3, text="Сохранить", command=save)
btn3.grid(row=1, column=1)

window.mainloop()