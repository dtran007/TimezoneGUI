#!/usr/bin/python3

import pytz
import datetime

try:
    import tkinter
except ImportError:  
    import Tkinter as tkinter

print("Tk Version", tkinter.TkVersion)
print("Tcl Version", tkinter.TclVersion)

guiWindow = tkinter.Tk()

guiWindow.title("Time Zone GUI")
guiWindow.geometry('720x420')
#padding
guiWindow['padx'] = 8

label = tkinter.Label(guiWindow, text="Time Zone")
label.grid(row=0, column=0, columnspan=1)

guiWindow.columnconfigure(0, weight=100)
guiWindow.columnconfigure(1, weight=1)
guiWindow.columnconfigure(2, weight=1000)
guiWindow.columnconfigure(3, weight=600)
guiWindow.columnconfigure(4, weight=100)
guiWindow.rowconfigure(0, weight=1)
guiWindow.rowconfigure(1, weight=10)
guiWindow.rowconfigure(2, weight=1)
guiWindow.rowconfigure(3, weight=3)
guiWindow.rowconfigure(4, weight=3)

#image
photo = tkinter.PhotoImage(file="Timez.png")
pLabel = tkinter.Label(guiWindow, image=photo)
pLabel.grid(row=1, column=3)

#listbox
fileList = tkinter.Listbox(guiWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in pytz.all_timezones:
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(guiWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

#result
resultText = tkinter.StringVar()
result = tkinter.Label(guiWindow, textvariable=resultText, anchor='w').place(x=250, y=300)

def onSelect(cEvent):
    w = cEvent.widget
    index = int(w.curselection()[0])
    country = w.get(index)
    resultText.set(country)

    tzDisplay = pytz.timezone(str(country))
    localTime = datetime.datetime.now(tz=tzDisplay)
    timeText ="The time in {} is {}".format(country, localTime)
    timez = tkinter.Label(guiWindow, text=timeText, anchor='w').place(x=250, y=325)

fileList.bind('<<ListboxSelect>>', onSelect)

#buttons
cancelButton = tkinter.Button(guiWindow, text="Close", command=guiWindow.destroy)
cancelButton.grid(row=4, column=4, sticky='w')

guiWindow.mainloop()
