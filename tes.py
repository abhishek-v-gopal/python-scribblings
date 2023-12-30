# this is the code for controll arduino using virtual serial monitor

import serial
import time
import tkinter as tk

ser = serial.Serial('COM6',9600,timeout=0)

root = tk.Tk()
root.title("Tkinter exapmle")
root.geometry("400x230")

root.resizable(True,True)

def on_button_click():
    ser.write(b"o") #o is the key which condition is defined (for on)

button2=tk.Button(root, text="led on", command=on_button_click)
button2.place(x=130, y=90)

def off():
    ser.write(b"f")#f is the key which condition is defined (for off)

button1=tk.Button(root, text="led off", command=off)
button1.place(x=130, y=140)

root.mainloop()