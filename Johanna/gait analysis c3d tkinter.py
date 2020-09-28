# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:01:47 2020

@author: johan
"""
import tkinter as tk
import sqlite3

conn = sqlite3.connect('MotionAnalysis.db')
# #conn = sqlite3.connect(':memory:')
c=conn.cursor()
ID=[]
def update_ID():
    ID = entry_1.get()
    return ID

window = tk.Tk()
label_1 = tk.Label(window,text = "Enter Patient ID")
entry_1 = tk.Entry(window)
button_1 = tk.Button(window, text = "Enter", command = update_ID)
ID= 1112
print(ID)

variable = tk.StringVar(window)
variable.set("select") # default value
options = tk.OptionMenu(window, variable, "pre-op", "post-op", "control")
options.grid(row = 1, column = 0)


label_2 = tk.Label(window,text = "Trial 1")
label_3 = tk.Label(window,text = "Trial 2")
label_4 = tk.Label(window,text = "Trial 3")
label_5 = tk.Label(window,text = "Average")

label_Left = tk.Label(window,text = "Left Limb")

label_6 = tk.Label(window,text = "Max Knee Angle")
label_7 = tk.Label(window,text = "Min Knee Angle")
label_8 = tk.Label(window,text = "Max Hip Angle")
label_9 = tk.Label(window,text = "Min Hip Angle")
label_10 = tk.Label(window,text = "Max Ankle Angle")
label_11 = tk.Label(window,text = "Min Ankle Angle")

label_Right = tk.Label(window,text = "Right Limb")

label_12 = tk.Label(window,text = "Max Knee Angle")
label_13 = tk.Label(window,text = "Min Knee Angle")
label_14 = tk.Label(window,text = "Max Hip Angle")
label_15 = tk.Label(window,text = "Min Hip Angle")
label_16 = tk.Label(window,text = "Max Ankle Angle")
label_17 = tk.Label(window,text = "Min Ankle Angle")


label_1.grid(row = 0, column= 0)
entry_1.grid(row = 0,column = 1)
button_1.grid(row =0, column = 2)

label_2.grid(row = 3, column= 1)
label_3.grid(row = 3, column= 2)
label_4.grid(row = 3, column= 3)
label_5.grid(row = 3, column= 4)

"""Left Limb from label 6-11, Right limb from 12-17"""
label_Left.grid(row = 4, column = 0)
label_6.grid(row = 5, column= 0)
label_7.grid(row = 6, column= 0)
label_8.grid(row = 7, column= 0)
label_9.grid(row = 8, column= 0)
label_10.grid(row = 9, column= 0)
label_11.grid(row = 10, column= 0)

label_Right.grid(row = 12, column = 0)
label_12.grid(row = 13, column= 0)
label_13.grid(row = 14, column= 0)
label_14.grid(row = 15, column= 0)
label_15.grid(row = 16, column= 0)
label_16.grid(row = 17, column= 0)
label_17.grid(row = 18, column= 0)


def max_left_knee(ID):
    c.execute("SELECT max_knee_left FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    maxlk1 = c.fetchone()
    maxlk2 = c.fetchone()
    maxlk3 = c.fetchone()
    return maxlk1, maxlk2,maxlk3
def min_left_knee():
    c.execute("SELECT min_knee_left FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    minlk1 = c.fetchone()
    minlk2 = c.fetchone()
    minlk3 = c.fetchone()
    return minlk1, minlk2,minlk3

def max_left_hip():
    c.execute("SELECT max_hip_left FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    maxlh1 = c.fetchone()
    maxlh2 = c.fetchone()
    maxlh3 = c.fetchone()
    return maxlh1, maxlh2,maxlh3
def min_left_hip():
    c.execute("SELECT min_hip_left FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    minlh1 = c.fetchone()
    minlh2 = c.fetchone()
    minlh3 = c.fetchone()
    return minlh1, minlh2,minlh3

def max_left_ankle():
    c.execute("SELECT max_ankle_left FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    maxla1 = c.fetchone()
    maxla2 = c.fetchone()
    maxla3 = c.fetchone()
    return maxla1, maxla2,maxla3
def min_left_ankle():
    c.execute("SELECT min_ankle_left FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    minla1 = c.fetchone()
    minla2 = c.fetchone()
    minla3 = c.fetchone()
    return minla1, minla2,minla3


maxlk1, maxlk2,maxlk3 = max_left_knee(ID)
maxlh1, maxlh2,maxlh3 = max_left_hip()
maxla1, maxla2,maxla3 = max_left_ankle()
minlk1, minlk2,minlk3 = min_left_knee()
minlh1, minlh2,minlh3 = min_left_hip()
minla1, minla2,minla3 = min_left_ankle()

label_1a = tk.Label(window,text = maxlk1)
label_1b = tk.Label(window,text = maxlk2)
label_1c = tk.Label(window,text = maxlk3)

label_2a = tk.Label(window,text = minlk1)
label_2b = tk.Label(window,text = minlk2)
label_2c = tk.Label(window,text = minlk3)

label_3a = tk.Label(window,text = maxlh1)
label_3b = tk.Label(window,text = maxlh2)
label_3c = tk.Label(window,text = maxlh3)

label_4a = tk.Label(window,text = minlh1)
label_4b = tk.Label(window,text = minlh2)
label_4c = tk.Label(window,text = minlh3)

label_5a = tk.Label(window,text = maxla1)
label_5b = tk.Label(window,text = maxla2)
label_5c = tk.Label(window,text = maxla3)

label_6a = tk.Label(window,text = minla1)
label_6b = tk.Label(window,text = minla2)
label_6c = tk.Label(window,text = minla3)

label_1a.grid(row = 5, column= 1)
label_1b.grid(row = 5, column= 2)
label_1c.grid(row = 5, column= 3)

label_2a.grid(row = 6, column= 1)
label_2b.grid(row = 6, column= 2)
label_2c.grid(row = 6, column= 3)

label_3a.grid(row = 7, column= 1)
label_3b.grid(row = 7, column= 2)
label_3c.grid(row = 7, column= 3)

label_4a.grid(row = 8, column= 1)
label_4b.grid(row = 8, column= 2)
label_4c.grid(row = 8, column= 3)

label_5a.grid(row = 9, column= 1)
label_5b.grid(row = 9, column= 2)
label_5c.grid(row = 9, column= 3)

label_6a.grid(row = 10, column= 1)
label_6b.grid(row = 10, column= 2)
label_6c.grid(row = 10, column= 3)

def max_right_knee():
    c.execute("SELECT max_knee_right FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    maxrk1 = c.fetchone()
    maxrk2 = c.fetchone()
    maxrk3 = c.fetchone()
    return maxrk1, maxrk2,maxrk3
def min_right_knee():
    c.execute("SELECT min_knee_right FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    minrk1 = c.fetchone()
    minrk2 = c.fetchone()
    minrk3 = c.fetchone()
    return minrk1, minrk2,minrk3

def max_right_hip():
    c.execute("SELECT max_hip_right FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    maxrh1 = c.fetchone()
    maxrh2 = c.fetchone()
    maxrh3 = c.fetchone()
    return maxrh1, maxrh2,maxrh3
def min_right_hip():
    c.execute("SELECT min_hip_right FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    minrh1 = c.fetchone()
    minrh2 = c.fetchone()
    minrh3 = c.fetchone()
    return minrh1, minrh2,minrh3

def max_right_ankle():
    c.execute("SELECT max_ankle_right FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    maxra1 = c.fetchone()
    maxra2 = c.fetchone()
    maxra3 = c.fetchone()
    return maxra1, maxra2,maxra3
def min_right_ankle():
    c.execute("SELECT min_ankle_right FROM GaitAnalysis_Max_Min WHERE Patient_ID = ?",(ID,))
    minra1 = c.fetchone()
    minra2 = c.fetchone()
    minra3 = c.fetchone()
    return minra1, minra2,minra3


maxrk1, maxrk2,maxrk3 = max_right_knee()
maxrh1, maxrh2,maxrh3 = max_right_hip()
maxra1, maxra2,maxra3 = max_right_ankle()
minrk1, minrk2,minrk3 = min_right_knee()
minrh1, minrh2,minrh3 = min_right_hip()
minra1, minra2,minra3 = min_right_ankle()

label_7a = tk.Label(window,text = maxlk1)
label_7b = tk.Label(window,text = maxlk2)
label_7c = tk.Label(window,text = maxlk3)

label_8a = tk.Label(window,text = minlk1)
label_8b = tk.Label(window,text = minlk2)
label_8c = tk.Label(window,text = minlk3)

label_9a = tk.Label(window,text = maxlh1)
label_9b = tk.Label(window,text = maxlh2)
label_9c = tk.Label(window,text = maxlh3)

label_10a = tk.Label(window,text = minlh1)
label_10b = tk.Label(window,text = minlh2)
label_10c = tk.Label(window,text = minlh3)

label_11a = tk.Label(window,text = maxla1)
label_11b = tk.Label(window,text = maxla2)
label_11c = tk.Label(window,text = maxla3)

label_12a = tk.Label(window,text = minla1)
label_12b = tk.Label(window,text = minla2)
label_12c = tk.Label(window,text = minla3)

label_7a.grid(row = 13, column= 1)
label_7b.grid(row = 13, column= 2)
label_7c.grid(row = 13, column= 3)

label_8a.grid(row = 14, column= 1)
label_8b.grid(row = 14, column= 2)
label_8c.grid(row = 14, column= 3)

label_9a.grid(row = 15, column= 1)
label_9b.grid(row = 15, column= 2)
label_9c.grid(row = 15, column= 3)

label_10a.grid(row = 16, column= 1)
label_10b.grid(row = 16, column= 2)
label_10c.grid(row = 16, column= 3)

label_11a.grid(row = 17, column= 1)
label_11b.grid(row = 17, column= 2)
label_11c.grid(row = 17, column= 3)

label_12a.grid(row = 18, column= 1)
label_12b.grid(row = 18, column= 2)
label_12c.grid(row = 18, column= 3) 

def select_all_from_table():
    c.execute("SELECT * FROM GaitAnalysis_Max_Min")
    rows = c.fetchall()
    for row in rows:
        print(row)
    return rows

window.mainloop()
select_all_from_table()



c.close()
conn.close()

