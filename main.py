import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
def conv():
    x=entry_int.get()
    output_string.set(f'{x*1.61}km')


#window
window = ttk.Window(themename='darkly')
window.title("Hello")
window.geometry("600x300")

#title
title_label = ttk.Label(master=window, text="Miles to Kilometers", font="popins 24 bold")
title_label.pack()

#input Filed
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=conv)
entry.pack(side='left', padx = 10)
button.pack(side='left', )
input_frame.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text="Output",
    font="popins 20",
    textvariable=output_string)
output_label.pack(pady=5)

#run
window.mainloop()