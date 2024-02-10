from tkinter import Tk, Label 
import time

root = Tk()
root.resizable(0, 0)
root.title("Python Digital Clock")

root.geometry("500x100")
mark = Label(root, text='python digital Clock', font='arial 20')

def Dclock():
    string = time.strftime('%H:%M:%S %p')
    mark.config(text=string)
    mark.after(1000, Dclock)
mark = Label(root, font=('calibri', 50, 'bold'), foreground='green')
mark.pack(anchor='center')
Dclock()

root.mainloop()