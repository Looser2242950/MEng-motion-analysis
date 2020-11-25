# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:07:27 2020

@author: johan
"""

import numpy as np
import sys
import btk
import sqlite3
import json
from tkinter import *
from tkinter import filedialog 
import os.path 
root = Tk()
MainFrame = Frame(root, bg = "blue")
MainFrame.pack(fill = BOTH) 

Triallist = []
def browseFiles1(): 
    Triallist.clear()
    global filelist
    filenames = (filedialog.askopenfilenames(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))
    #label_file_explorer1.configure(text="File Opened: "+filename1)
    print(filenames)
    filelist = list(filenames)
    length = len(filelist)
    for i in range(length):
        Triallist.append("Trial " + str(i+1))
    print(type(filenames))
    print(Triallist)
    
button_explore1 = Button(MainFrame, text = "Select Trial 1",  width = 12, bg = "ghost white",
                         command = lambda : [browseFiles1()])  
label_file_explorer1 = Label(MainFrame,  text = "", width = 80, height = 3 ,  fg = "blue" , bg = "ghost white") 
button_explore1.grid(column = 1, row = 1, rowspan = 2) 
label_file_explorer1.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 

root.mainloop()
print(filelist)