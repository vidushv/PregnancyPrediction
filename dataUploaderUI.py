from tkinter import *
import requests
import os
import sys
import time
import json
from threading import Thread

trigger_url = 'https://functions-vivid.azurewebsites.net/api/HttpTrigger1?code=I3VJhugK6llvTNwAcNc53tRasmK/qKR0EXnOTccdc0Xcaw251w/bCw=='

def getSearch():
    t= Thread(target=insert_entry_fields)#this should work, in case it doesn't, try "t= Thread(target=Search.getSearch,args=[self])" instead.
    t.start()

def insert_entry_fields():
   Label(master, text= '                           ...                           ', font='Arial 11 bold',fg='grey', anchor='center').grid(row=8)
   print("Trying to upload data:", (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))

   cowId = e1.get()
   date1 = e2.get()
   lbd = e3.get()
   lact_d = e4.get()
   lact_n = e5.get()
   prod_d = e6.get()
   label = e7.get()

   # Empty values rejected
   try:
       cowId = int(cowId)
       date1 = int(date1[:2]) + 30*int(date1[2:4]) + 365*int(date1[4:])
       lbd = int(lbd[:2]) + 30*int(lbd[2:4]) + 365*int(lbd[4:])
       lact_d = int(lact_d)
       lact_n = int(lact_n)
       prod_d = float(prod_d)
       label = int(label)
       if label not in [0, 1]:
           raise Exception()
   except:
       Label(master, text='Error uploading data! Please check values.', fg='red', anchor='center', font='Arial 11 bold').grid(row=8)

   payload = {
       "ID": cowId,
       "lact_d": lact_d,
       "lact_n":lact_n,
       "lbd_d": date1-lbd,
       "daily_prod": prod_d,
       "label": label,
   }

   request1 = requests.get(trigger_url, params = payload)
   print(request1.text)
   Label(master, text= 'Status Code: '+str(request1.status_code), font='Arial 11 bold',fg='green', anchor='center').grid(row=8)

   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)
   e4.delete(0,END)
   e5.delete(0,END)
   e6.delete(0,END)
   e7.delete(0,END)

master = Tk()
master.title('Farm Data Uploader')

Label(master, text="Cow ID").grid(row=0)
Label(master, text="Date").grid(row=1)
Label(master, text="Last Breeding Date").grid(row=2)
Label(master, text="Days in Lactation").grid(row=3)
Label(master, text="Lactation Number").grid(row=4)
Label(master, text="Daily Production").grid(row=5)
Label(master, text="Lactation Status").grid(row=6)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)

e1.bind("<FocusIn>", lambda args: e1.delete('0', 'end'))
e2.bind("<FocusIn>", lambda args: e2.delete('0', 'end'))
e3.bind("<FocusIn>", lambda args: e3.delete('0', 'end'))
e4.bind("<FocusIn>", lambda args: e4.delete('0', 'end'))
e5.bind("<FocusIn>", lambda args: e5.delete('0', 'end'))
e6.bind("<FocusIn>", lambda args: e6.delete('0', 'end'))
e7.bind("<FocusIn>", lambda args: e7.delete('0', 'end'))

e1.insert(10,"like 12345")
e2.insert(10,"DDMMYYYY")
e3.insert(10,"DDMMYYYY")
e4.insert(10,"like 62")
e5.insert(10,"like 4")
e6.insert(10,"like 12.41")
e7.insert(10,"0 or 1")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)

Button(master, text='Quit', command=master.quit).grid(row=7, column=0, sticky=W, pady=4)
Button(master, text='Upload Data', command=getSearch).grid(row=7, column=1, sticky=W, pady=4)

mainloop( )
