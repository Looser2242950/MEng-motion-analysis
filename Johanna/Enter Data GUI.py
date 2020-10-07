# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:24:07 2020

@author: johan
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import btk
import sqlite3
from tkinter import *
from tkinter import filedialog 
   

# Create the root window 
window = Tk() 
# Set window title 
window.title('Load New Trial')  
# Set window size 
window.geometry("1050x480")  
#Set window background color 
window.config(background = "white")    


"""First Block of input  Used ot give patient Data"""

label_info = Label(window, text = "Input new patient motion sensor assessment. Please fill in all relevant fields", height = 4, fg = "red")
label_ID = Label(window, text = "Patient ID: ")
vID = StringVar()
entry_ID = Entry(window, textvariable = vID)

label_limb = Label(window, text = "Affected Limb: ")
vlimb = IntVar()
radioleftlimb = Radiobutton(window, text="Left",variable=vlimb, value="1")
radiorightlimb = Radiobutton(window, text="Right",variable=vlimb, value="2")
def control():
    if vlimb.get() == 3:
        vtype.set("control")

radiocontlimb = Radiobutton(window, text="Control",variable=vlimb, value="3", command = control)


label_dom = Label(window, text = "Dominant Limb: ")
vdom = IntVar()
radioleftdom = Radiobutton(window, text="Left",variable=vdom, value="1")
radiorightdom = Radiobutton(window, text="Right",variable=vdom, value="2")




"""Second Block that select trials and inputs whether data is clan or not"""

#in intitialdir put directory where we can expect the files to be
def browseFiles1(): 
    global filename1
    filename1 = filedialog.askopenfilename(initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
                                          title = "Select a File", 
                                          filetypes = (("C3D files","*.c3d*"), 
                                                       ("all files", "*.*")))   
    label_file_explorer1.configure(text="File Opened: "+filename1) 
    
def browseFiles2(): 
    global filename2
    filename2 = filedialog.askopenfilename(initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
                                          title = "Select a File", 
                                          filetypes = (("C3D files", "*.c3d*"), 
                                                       ("all files", "*.*")))   
    label_file_explorer2.configure(text="File Opened: "+filename2)     # Change label contents 
    
def browseFiles3(): 
    global filename3
    filename3 = filedialog.askopenfilename(initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
                                          title = "Select a File", 
                                          filetypes = (("C3D files", "*.c3d*"), 
                                                       ("all files", "*.*")))   
    # Change label contents 
    label_file_explorer3.configure(text="File Opened: "+filename3)
   
                                                                                                   
cleanFP = Label(window, text="""Select which limb has clean Force Plate data:""", height = 3)
cleanK = Label(window, text = "Use Kinetic Data?", width = 20, height = 3 )

button_explore1 = Button(window, text = "Select Trial 1", command = browseFiles1)  
label_file_explorer1 = Label(window,  text = "", width = 80, height = 4,  fg = "blue") 
v1 = IntVar()
v1c = IntVar()
v1c.set(1)
radioleft1 = Radiobutton(window, text="Left",variable=v1, value="1")
radioright1 = Radiobutton(window, text="Right",variable=v1, value="2")
radioboth1 = Radiobutton(window, text="Both",variable=v1, value="3")
radioneither1 = Radiobutton(window, text="Neither",variable=v1, value="4")
check1 = Checkbutton(window, text = "yes", variable = v1c)

button_explore2 = Button(window, text = "Select Trial 2", command = browseFiles2)  
label_file_explorer2 = Label(window, text = "", width = 80, height = 4, fg = "blue")
v2 = IntVar()
v2c = IntVar()
v2c.set(1)
radioleft2 = Radiobutton(window,text="Left",variable=v2, value="1")
radioright2 = Radiobutton(window, text="Right",variable=v2, value="2")
radioboth2 = Radiobutton(window, text="Both",variable=v2, value="3")
radioneither2 = Radiobutton(window, text="Neither",variable=v2, value="4")
check2 = Checkbutton(window, text = "yes", variable = v2c)

button_explore3 = Button(window, text = "Select Trial 3", command = browseFiles3)   
label_file_explorer3 = Label(window,  text = "", width = 80, height = 4,  fg = "blue")  
v3 = IntVar()
v3c = IntVar()  
v3c.set(1)
radioleft3 = Radiobutton(window,text="Left",variable=v3, value="1")
radioright3 = Radiobutton(window, text="Right",variable=v3, value="2")
radioboth3 = Radiobutton(window, text="Both",variable=v3, value="3")
radioneither3 = Radiobutton(window, text="Neither",variable=v3, value="4")
check3 = Checkbutton(window, text = "yes", variable = v3c)  


"""BLOCK 3: Details about Trial type and date as well as exit button"""

def close_window():
    window.destroy() 

button_exit = Button(window,  
                     text = "Exit", 
                     command = close_window)

label_date = Label(window, text = "Assessment Date: ")
vmonth = StringVar()
vyear = StringVar()
labelmonth = Label(window, text = "Month: ")
optionmonth = OptionMenu(window, vmonth, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
labelyear = Label(window, text = "Year: ")
vyear.set("(YYYY)")
entryyear = Entry(window, textvariable = vyear)

label_type = Label(window, text = "Patient Type: ")
vtype = StringVar()
limb = vlimb.get()

optiontype = OptionMenu(window, vtype, "pre-op", "post-op", "control" )


# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by specifying rows and columns
"""BLOCK 1"""
label_info.grid(column = 1, row = 1, columnspan = 11)

label_ID.grid(column = 1, row=3 )
entry_ID.grid(column = 2, row =3)

label_limb.grid(column = 1, row= 4)
radioleftlimb.grid(column =2, row = 4)
radiorightlimb.grid(column= 3, row =4)
radiocontlimb.grid(column = 4, row = 4)

label_dom.grid(column = 1, row= 5)
radioleftdom.grid(column = 2, row = 5)
radiorightdom.grid(column= 3, row =5)

"""BLOCK 2"""
cleanFP.grid(column = 8, row = 9, columnspan = 4)
cleanK.grid(column =12, row = 9,)
button_explore1.grid(column = 1, row = 10) 
label_file_explorer1.grid(column = 2, row = 10, columnspan = 5) 
radioleft1.grid(column = 8, row = 10)
radioright1.grid(column = 9, row =10)
radioboth1.grid(column = 10, row = 10)
radioneither1.grid(column = 11, row = 10)
check1.grid(column = 12, row = 10)

button_explore2.grid(column = 1, row = 11)
label_file_explorer2.grid(column = 2, row = 11,  columnspan = 5)
radioleft2.grid(column = 8, row = 11)
radioright2.grid(column = 9, row = 11)
radioboth2.grid(column = 10, row = 11)
radioneither2.grid(column = 11, row = 11)
check2.grid(column = 12, row = 11)

button_explore3.grid(column = 1, row = 12)  
label_file_explorer3.grid(column = 2, row = 12,  columnspan = 5)
radioleft3.grid(column = 8, row = 12)
radioright3.grid(column = 9, row = 12)
radioboth3.grid(column = 10, row = 12)
radioneither3.grid(column = 11, row = 12)  
check3.grid(column = 12, row = 12)







"""BLOCK 3"""

label_date.grid(column = 1, row= 16)
labelmonth.grid (column=2, row = 16)
optionmonth.grid(column = 3, row  = 16)
labelyear.grid(column = 4, row = 16)
entryyear.grid(column = 5, row = 16)


label_type.grid(column = 1, row= 17)
optiontype.grid(column = 2, row = 17)
button_exit.grid(column = 1,row = 20, columnspan = 11) 
# Let the window wait for any events 
window.mainloop() 



"""SAVE inputs into variables"""
#BLOCK 1
ID = vID.get()
AffectedLimb  = vlimb.get()
DomLimb = vdom.get()

#BLOCK 2
#filename1 = filename1
file1FP = v1.get()
file1K = v1c.get()

#filename2 = filename2
file2FP = v2.get()
file2K = v2c.get()

#filename3 = filename3
file3FP =  v3.get()
file3K = v3c.get()

#BLOCK3 
month = vmonth.get()
year = vyear.get()
pattype = vtype.get()
print(month, year)
