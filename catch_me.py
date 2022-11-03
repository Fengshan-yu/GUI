#Catch me!

import tkinter as tk
from tkinter import messagebox
import random

def click(event=None):
    tk.messagebox.showinfo("Click!", "Congratulations, you won!")

def move(event=None):
    button.place(x=random.randrange((event.x+50),450), y=random.randrange((event.y+50), 490))

window = tk.Tk()
window.title("Catch me!")
window.geometry("500x500")
window.resizable(False, False)
button = tk.Button(window, text="Catch me!", bg="#00FFFF", command=click)
button.place(x=10, y=10)
button.bind("<Enter>", move)

window.mainloop()