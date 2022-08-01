import webbrowser
import wmi
import os
import pythoncom
from threading import Thread
from tkinter import *

apexOn = False
windowOpen = False


def setenv():
    global pseudo
    pseudo = e.get()
    os.system(f'setx APEX_ACCOUNT "{pseudo}" /M')


pseudo = os.environ.get('APEX_ACCOUNT')
if os.environ.get('APEX_ACCOUNT') is None:
    master = Tk()
    e = Entry(master)
    e.pack()
    e.focus_set()
    b = Button(master, text="ok", width=10, command=setenv)
    b.pack()
    mainloop()


def listener():
    pythoncom.CoInitialize()
    c = wmi.WMI()
    process_watcher = c.Win32_Process.watch_for("creation")
    while True:
        new_process = process_watcher()
        if new_process.Caption == 'r5apex.exe':
            webbrowser.open(f'https://apexlegendsstatus.com/profile/PC/{pseudo}#S-match-history')


t = Thread(target=listener())
t.daemon = True
t.start()
