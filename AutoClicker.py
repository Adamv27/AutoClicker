import time
import keyboard
import threading
import pyautogui
from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry('225x175')

def clicker():
    try:
        delay = float(delay_entry.get())
    except ValueError:
        return

    start_key = resume_entry.get()
    stop_key = pause_entry.get()

    if not start_key.isalpha() or not stop_key.isalpha():
        return

    while True:
        try:
            if keyboard.is_pressed(start_key):
                time.sleep(delay)
                while True:
                    try:
                        if keyboard.is_pressed(stop_key):
                            break
                    except:
                        break
                    pyautogui.click()
        except:
            break
    return


def start():
    thread = threading.Thread(target=clicker)
    thread.daemon = True
    thread.start()

myFont = font.Font(size=10)

delay_label = Label(root, text='Delay', bg='#808B96', fg='white')
resume_label = Label(root, text='Resume', bg='#808B96', fg='white')
pause_label = Label(root, text='Pause', bg='#808B96', fg='white')
delay_label['font'] = myFont
resume_label['font'] = myFont
pause_label['font'] = myFont

delay_entry = Entry(root, justify='center')
delay_entry.insert(0, '0')
resume_entry = Entry(root, justify='center')
resume_entry.insert(0, 'C')
pause_entry = Entry(root, justify='center')
pause_entry.insert(0, 'X')

delay_label.grid(row=0, sticky=E)
resume_label.grid(row=1, sticky=E)
pause_label.grid(row=2, sticky=E)

delay_entry.grid(row=0, column=1)
resume_entry.grid(row=1, column=1)
pause_entry.grid(row=2, column=1)

start_button = Button(root, width=25, text='START', command=start)
start_button.place(x=77, y=75, width=75, height=25)

root.configure(bg='#808B96')
root.mainloop()


