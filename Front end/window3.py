import tkinter as tk
from tkinter import ttk;
import sqlite3
import random
import tkinter.messagebox
from PATDELSU import P_display
from PATDELSU import D_display
from PATDELSU import P_UPDATE

conn=sqlite3.connect("MDBA.db")
print("DATABASE CONNECTION SUCCESSFUL")

def doctormenu():
    scores = tk.Tk() 
    tk.Label(scores, text="Patient List", font=("Arial",30)).grid(row=0, columnspan=3)
    # create Treeview with 3 columns
    cols = ('No risk', 'Mild risk', 'High risk')
    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=2)

    # tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
    # tempList.sort(key=lambda e: e[1], reverse=True)

    # for i, (name, score) in enumerate(tempList, start=1):
    for i in range(100):  
        listBox.insert("", "end", values=(random.randint(1000,6000),random.randint(1000,7000),random.randint(1000,6000)))
