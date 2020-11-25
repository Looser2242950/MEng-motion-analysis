# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:30:27 2020

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

filename_StepUp1 = None
filename_StepUp2 = None
filename_StepUp3 = None
filename_StepUp4 = None
filename_StepUp5 = None
filename_StepUp6 = None
cleanleft1 = "No"
cleanright1 = "No"
cleanleft2 = "No"
cleanright2 = "No"
cleanleft3 = "No"
cleanright3 = "No"
cleanleft4 = "No"
cleanright4 = "No"
cleanleft5 = "No"
cleanright5 = "No"
cleanleft6 = "No"
cleanright6 = "No"
numTrialslist = []






"""Start SQLite Connection""" 
conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('MotionAnalysis14.db')
c=conn.cursor()

def create_patient_data_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Patient_Data
              (ID TEXT PRIMARY KEY, Dominant_Limb TEXT, Patient_Type TEXT, 
              Month TEXT, Affected_Limb TEXT,
              filename_StepUp_Trial_1 TEXT, filename_StepUp_Trial_2 TEXT, filename_StepUp_Trial_3 TEXT,
              filename_StepUp_Trial_4 TEXT,filename_StepUp_Trial_5 TEXT, filename_StepUp_Trial_6 TEXT
              )""")
              #add filename_StepUp_STS_Trial_1,.... for different movements             
def create_StepUp_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepUp_Table
              (filename_StepUp TEXT)""")            
def columns_StepUp_Table():
     for LR in ["Left", "Right"]:
         for axis in ["x", "y", "z"]:
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Knee_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Knee_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Knee_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Knee_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Hip_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Hip_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Hip_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Hip_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Ankle_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Ankle_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Ankle_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Ankle_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Foot_Progression_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_pelvis_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_COM_{axis} TEXT""")             

def create_StepUp_Max_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepUp_Max_Table
              (filename_StepUp TEXT, Limb TEXT)""")            
def columns_StepUp_Max_Table():
    for axis in ["x", "y", "z"]:
        for function in ["max", "min"]:
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Knee_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Knee_Moment_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Knee_Force_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Knee_Power_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Hip_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Hip_Moment_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Hip_Force_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Hip_Power_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Ankle_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Ankle_Moment_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Ankle_Force_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Ankle_Power_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_Foot_Progression_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_pelvis_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE StepUp_Max_Table ADD COLUMN {function}_COM_{axis} TEXT""")      

create_StepUp_Max_Table()
columns_StepUp_Max_Table()              
create_patient_data_table()
create_StepUp_Table()
columns_StepUp_Table()







"""Setup GUI and Frames"""
root = Tk()
MainFrame = Frame(root, bg = "blue")
MainFrame.pack(fill = BOTH) 

mycanvas = Canvas(MainFrame)
mycanvas.pack(side = LEFT, fill = BOTH, expand =True)
scroll_y = Scrollbar(MainFrame, orient = "vertical", command = mycanvas.yview)
scroll_y.pack(side = RIGHT, fill = BOTH)
mycanvas.configure(width = 860, height = 500)
mycanvas.configure(yscrollcommand = scroll_y.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")) )
ScrollFrame = Frame(mycanvas, bg = "DodgerBlue4")
ScrollFrame.pack(fill = BOTH)
mycanvas.create_window((0,0), window = ScrollFrame, anchor = "nw")

FrameLabel = Frame(ScrollFrame, bg = "DodgerBlue3", bd = 6)
FrameLabel.pack()
FrameTrial1 = Frame(ScrollFrame, bg = "ivory3", bd = 6)
FrameTrial1.pack()
FrameTrial2 = Frame(ScrollFrame, bg = "ghost white", bd = 6)
FrameTrial2.pack()
FrameTrial3 = Frame(ScrollFrame, bg = "ivory3", bd = 6)
FrameTrial3.pack()
FrameTrial4 = Frame(ScrollFrame, bg = "ghost white", bd = 6)
FrameTrial4.pack()
FrameTrial5 = Frame(ScrollFrame, bg = "ivory3", bd = 6)
FrameTrial5.pack()
FrameTrial6 = Frame(ScrollFrame, bg = "ghost white", bd = 6)
FrameTrial6.pack()
FrameInfo = Frame(ScrollFrame, bg = "DodgerBlue3", bd = 6)
FrameInfo.pack()
FrameClose = Frame(ScrollFrame, bg = "DeepSkyBlue2")
FrameClose.pack()



"""Define Functions"""

#FILE SELECTORS +filename_StepUp changes
def browseFiles1(): 
    global filename_StepUp1
    filename_StepUp1 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))
    label_file_explorer1.configure(text="File Opened: "+filename_StepUp1)
    numTrialslist.append("Trial 1")


def browseFiles2(): 
    global filename_StepUp2
    filename_StepUp2 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
        ("all files", "*.*"))))  
    label_file_explorer2.configure(text="File Opened: "+filename_StepUp2)
    numTrialslist.append("Trial 2")
    
def browseFiles3(): 
    global filename_StepUp3
    filename_StepUp3 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))  
    label_file_explorer3.configure(text="File Opened: "+filename_StepUp3) 
    numTrialslist.append("Trial 3")
    
def browseFiles4(): 
    global filename_StepUp4
    filename_StepUp4 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))  
    label_file_explorer4.configure(text="File Opened: "+filename_StepUp4) 
    numTrialslist.append("Trial 4")

def browseFiles5(): 
    global filename_StepUp5
    filename_StepUp5 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))  
    label_file_explorer5.configure(text="File Opened: "+filename_StepUp5) 
    numTrialslist.append("Trial 5")

def browseFiles6(): 
    global filename_StepUp6
    filename_StepUp6 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))  
    label_file_explorer6.configure(text="File Opened: "+filename_StepUp6) 
    numTrialslist.append("Trial 6")



#EXCTRACT AND NORMALISE DATA
# def cutcycle(footstrike, data):
#     footstrike1 = footstrike[0]
#     footstrike2 = footstrike[1]
#     data1 = (data[footstrike1:footstrike2])
#     return data1
    
def extractvalues(trial):
    #extracts al the arrays
    #can be used for all trials, just needs to be instantiated with the correct trial
    x = dict();  
    x["KneeAngle"]= (trial.GetPoint("LKneeAngles")).GetValues()
    x["KneeForce"]= (trial.GetPoint("LKneeForce")).GetValues()
    x["KneeMoment"]= (trial.GetPoint("LKneeMoment")).GetValues()
    x["KneePower"]= (trial.GetPoint("LKneePower")).GetValues() 
    x["HipAngle"]= ((trial.GetPoint("LHipAngles")).GetValues())
    x["HipForce"]= (trial.GetPoint("LHipForce")).GetValues()
    x["HipMoment"]= (trial.GetPoint("LHipMoment")).GetValues()
    x["HipPower"]= (trial.GetPoint("LHipPower")).GetValues() 
    x["AnkleAngle"]= (trial.GetPoint("LAnkleAngles")).GetValues()
    x["AnkleForce"]= (trial.GetPoint("LAnkleForce")).GetValues()
    x["AnkleMoment"]= (trial.GetPoint("LAnkleMoment")).GetValues()
    x["AnklePower"]= (trial.GetPoint("LAnklePower")).GetValues()    
    x["FootProgressAngle"] = (trial.GetPoint("LFootProgressAngles")).GetValues()
    x["pelvisAngle"] = (trial.GetPoint("LPelvisAngles")).GetValues() 
    x["COM"] = (trial.GetPoint("CentreOfMass")).GetValues()
    return x

def extractintoDict(filename, TrialNum):
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename) # set a filename to the reader
    reader.Update()
    trialacq = reader.GetOutput() # is the btk aquisition object
    patient["StepUp"][TrialNum] ={}
    patient["StepUp"][TrialNum].update({"Left": extractvalues(trialacq)})
    patient["StepUp"][TrialNum].update({"Right": extractvalues(trialacq)})
    patient["StepUp"][TrialNum].update({"startframe":trialacq.GetFirstFrame()})#first frame of data
    patient["StepUp"][TrialNum].update({"Filename":filename})
    # #instantiate the nested dict to input in the footstrike etc
      
    for LR in ['Right','Left']:
        for key in patient["StepUp"][TrialNum][LR].keys():
            arr = patient["StepUp"][TrialNum][LR][key]
            patient["StepUp"][TrialNum][LR][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
     
    #call other function"returnvalues" to extract rest of data
    #returnvalues(trialacq)
    global ID
    try:
        ID = trialacq.GetEvent().GetSubject()
        vID.set(ID)
    except:
        pass
    

def close_window():
    root.destroy()
    



"""Initialise the Dict"""
patient = {}
patient["StepUp"] = {}




"""GUI Widgets"""
#FRAME 1: INFO
label_info1 = Label(FrameLabel, 
                    text = """Please select at least 3 StepUp trials. 
                    Ensure a minimum of 3 complete StepUp cycles on each limb. """, 
                   bg = "ivory3", height = 2)
label_info1.grid()
label_info2 = Label(FrameLabel, 
                    text = "Input the patient data and select Accept to enter into the database.", 
                    bg = "ivory3", height = 2)
label_info2.grid()


#FRAMES 2-7: INDIVIDUAL TRIAL SELECTIONS
button_explore1 = Button(FrameTrial1, text = "Select Trial 1",  width = 12, bg = "ghost white",
                         command = lambda : [browseFiles1(), extractintoDict(filename_StepUp1, "Trial 1")])  
label_file_explorer1 = Label(FrameTrial1,  text = "", width = 80, height = 3 ,  fg = "blue" , bg = "ghost white") 
button_explore1.grid(column = 1, row = 1, rowspan = 2) 
label_file_explorer1.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean1 = Label(FrameTrial1, text="",  width = 25, bg = "ivory3")
label_clean1.grid(column = 10, row = 1)
label_clean1r = Label(FrameTrial1, text="",  width = 25, bg = "ivory3")
label_clean1r.grid(column = 10, row = 2)



button_explore2 = Button(FrameTrial2, text = "Select Trial 2",   width = 12,
                         command = lambda : [browseFiles2(), extractintoDict(filename_StepUp2, "Trial 2")])  
label_file_explorer2 = Label(FrameTrial2,  text = "", width = 80, height = 3,  fg = "blue", bg = "ivory2") 
button_explore2.grid(column = 1 , row = 1, rowspan = 2)
label_file_explorer2.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean2 = Label(FrameTrial2, text=" ",  width = 25, bg = "ghost white")
label_clean2.grid(column = 10, row = 1)
label_clean2r = Label(FrameTrial2, text="",  width = 25, bg = "ghost white")
label_clean2r.grid(column = 10, row = 2)



button_explore3 = Button(FrameTrial3, text = "Select Trial 3",  width = 12, bg = "ghost white",
                         command = lambda : [browseFiles3(), extractintoDict(filename_StepUp3, "Trial 3")])  
label_file_explorer3 = Label(FrameTrial3,  text = "", width = 80, height = 3,  fg = "blue", bg = "ghost white") 
button_explore3.grid(column = 1 , row = 1, rowspan = 2) 
label_file_explorer3.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean3 = Label(FrameTrial3, text=" ",  width = 25, bg = "ivory3")
label_clean3.grid(column = 10, row = 1)
label_clean3r = Label(FrameTrial3, text="",  width = 25, bg = "ivory3")
label_clean3r.grid(column = 10, row = 2)



button_explore4 = Button(FrameTrial4, text = "Select Trial 4",   width = 12,
                         command = lambda : [browseFiles4(), extractintoDict(filename_StepUp4, "Trial 4")])  
label_file_explorer4 = Label(FrameTrial4,  text = "", width = 80, height = 3,  fg = "blue", bg = "ivory2") 
button_explore4.grid(column = 1 , row = 1, rowspan = 2) 
label_file_explorer4.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean4 = Label(FrameTrial4, text=" ",  width = 25, bg = "ghost white")
label_clean4.grid(column = 10, row = 1)
label_clean4r = Label(FrameTrial4, text="",  width = 25, bg = "ghost white")
label_clean4r.grid(column = 10, row = 2)


button_explore5 = Button(FrameTrial5, text = "Select Trial 5",   width = 12,bg = "ghost white",
                         command = lambda : [browseFiles5(), extractintoDict(filename_StepUp5, "Trial 5")])  
label_file_explorer5 = Label(FrameTrial5,  text = "", width = 80, height = 3,  fg = "blue", bg = "ghost white") 
button_explore5.grid(column = 1 , row = 1, rowspan = 2) 
label_file_explorer5.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean5 = Label(FrameTrial5, text=" ",  width = 25, bg = "ivory3")
label_clean5.grid(column = 10, row = 1)
label_clean5r = Label(FrameTrial5, text="",  width = 25, bg = "ivory3")
label_clean5r.grid(column = 10, row = 2)



button_explore6 = Button(FrameTrial6, text = "Select Trial 6",  width = 12,
                         command = lambda : [browseFiles6(), extractintoDict(filename_StepUp6, "Trial 6")])  
label_file_explorer6 = Label(FrameTrial6,  text = "", width = 80, height = 3,  fg = "blue", bg = "ivory2") 
button_explore6.grid(column = 1 , row = 1, rowspan = 2) 
label_file_explorer6.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean6 = Label(FrameTrial6, text=" ",  width = 25, bg = "ghost white")
label_clean6.grid(column = 10, row = 1)
label_clean6r = Label(FrameTrial6, text="",  width = 25, bg = "ghost white")
label_clean6r.grid(column = 10, row = 2)



#FRAME 8: INPuT PATIENT DATA
labelID = Label(FrameInfo,  text = "Patient ID: ", bg = "ivory3") 
labelID.grid(column = 1, row = 1)
vID = StringVar()
entryID = Entry(FrameInfo,  textvariable = vID,   fg = "purple4", width = 20) 
entryID.grid(column = 2, row = 1, columnspan = 3)
labelDom = Label(FrameInfo,  text = "Dominant Limb: ", bg = "ivory3") 
labelDom.grid(column = 1, row = 2)
vDom = StringVar()
vDom.set(0)
radioleftdom = Radiobutton(FrameInfo, text="Left",variable= vDom, value="Left")
radioleftdom.grid(column = 2, row = 2)
radiorightdom = Radiobutton(FrameInfo, text="Right",variable =vDom, value="Right")
radiorightdom.grid(column = 3, row = 2)
radiorightdom = Radiobutton(FrameInfo, text="N/A",variable =vDom, value="N/A")
radiorightdom.grid(column = 4, row = 2)

class Pattype:
    def disable(self, master):
        if vtype.get() == "Post-op":
            self.month_entry.configure(state = "normal")
            self.date_label.configure(state = "normal")
            self.limb_label.configure(state = "normal")
            self.radioleft.configure(state = "normal")
            self.radioright.configure(state = "normal")
            self.radioboth.configure(state = "normal")
        if vtype.get() == "Control":
            self.month_entry.configure(state = "disabled")
            self.date_label.configure(state = "disabled")
            self.limb_label.configure(state = "disabled")
            self.radioleft.configure(state = "disabled")
            self.radioright.configure(state = "disabled")
            self.radioboth.configure(state = "disabled")
        if vtype.get() == "Pre-op":
            self.month_entry.configure(state = "disabled")
            self.date_label.configure(state = "disabled")    
            self.limb_label.configure(state = "normal")
            self.radioleft.configure(state = "normal")
            self.radioright.configure(state = "normal")
            self.radioboth.configure(state = "normal")
            
    def __init__(self, master):
        self.label_type = Label(FrameInfo, text = "Patient Type: ", bg = "ivory3")
        self.label_type.grid(column = 1, row = 3)
        global vtype
        vtype = StringVar()
        self.optiontype = OptionMenu(FrameInfo, vtype, "Pre-op", "Post-op", "Control", 
                                     command = self.disable)
        self.optiontype.config(width = 20)
        self.optiontype.grid(column = 2, row = 3, columnspan  =3)
        
        self.date_label = Label(FrameInfo, text = "Number of months Post - Op: ", bg = "ivory3")
        self.date_label.grid(column = 1, row  = 4)
        global vmonth
        vmonth = IntVar() 
        self.month_entry = Entry(FrameInfo, textvariable = vmonth, width = 20, fg = "purple4")
        self.month_entry.grid(column = 2, row = 4, columnspan  = 3)
        
        self.limb_label = Label(FrameInfo, text = "Affected Limb: ", bg = "ivory3")
        self.limb_label.grid(column = 1, row  = 5)
        global vlimb
        vlimb = StringVar()
        vlimb.set(0)
        self.radioleft = Radiobutton(FrameInfo, text="Left",variable= vlimb, value="Left")
        self.radioleft.grid(column = 2, row = 5)
        self.radioright = Radiobutton(FrameInfo, text="Right",variable=vlimb, value="Right")
        self.radioright.grid(column = 3, row = 5)
        self.radioboth = Radiobutton(FrameInfo, text="Both",variable=vlimb, value="Both")
        self.radioboth.grid(column = 4, row = 5)     
Pattype(FrameInfo)




def enter_patient_data():
    c.execute("""INSERT INTO Patient_Data
              (ID, Dominant_Limb, Patient_Type, Month, Affected_Limb,
              filename_StepUp_Trial_1, filename_StepUp_Trial_2, filename_StepUp_Trial_3,
              filename_StepUp_Trial_4, filename_StepUp_Trial_5, filename_StepUp_Trial_6)
              VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
              (vID.get(), vDom.get(), vtype.get(), vmonth.get(), vlimb.get(),
               filename_StepUp1, filename_StepUp2, filename_StepUp3, filename_StepUp4, filename_StepUp5, filename_StepUp6))

def enter_StepUp_Table (numTrials):
    for TrialNum in numTrials:
        filename = patient["StepUp"][TrialNum]["Filename"]
        print(filename)
         
        c.execute("""INSERT INTO StepUp_Table 
                  (filename_StepUp) 
                  VALUES (?)""", ((filename,)))
        for LR in ["Left", "Right"]:
            for axis in ["x", "y", "z"]:
                c.execute(f"""UPDATE StepUp_Table
                          SET 
                          {LR}_Knee_Angle_{axis} = ?,
                          {LR}_Knee_Moment_{axis} = ?,
                          {LR}_Knee_Force_{axis} = ?,
                          {LR}_Knee_Power_{axis} = ?,
                          {LR}_Hip_Angle_{axis} = ?,
                          {LR}_Hip_Moment_{axis} = ?,
                          {LR}_Hip_Force_{axis} = ?,
                          {LR}_Hip_Power_{axis} = ?,
                          {LR}_Ankle_Angle_{axis} = ?,
                          {LR}_Ankle_Moment_{axis} = ?,
                          {LR}_Ankle_Force_{axis} = ?,
                          {LR}_Ankle_Power_{axis} =  ?,
                          {LR}_Foot_Progression_Angle_{axis} = ?,
                          {LR}_pelvis_Angle_{axis} =  ?,
                          {LR}_COM_{axis} =  ?
                          WHERE filename_StepUp = ?
                          """,(
                          (str(patient["StepUp"][TrialNum][LR]["KneeAngle"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["KneeMoment"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["KneeForce"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["KneePower"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["HipAngle"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["HipMoment"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["HipForce"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["HipPower"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["AnkleAngle"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["AnkleMoment"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["AnkleForce"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["AnklePower"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["FootProgressAngle"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["pelvisAngle"][axis])[1:-1]),
                          (str(patient["StepUp"][TrialNum][LR]["COM"][axis])[1:-1]),
                          filename
                          ))

def enter_StepUp_extrema (numTrials):
    #Trial 1: left clean right clean
    #Trial 2: right clean
    #trial 3: left clean
    for TrialNum in numTrials:
        filename = patient["StepUp"][TrialNum]["Filename"]
        for LR in ["Left", "Right"]:
            c.execute("""INSERT INTO StepUp_Max_Table 
                      (filename_StepUp, Limb) 
                      VALUES (?,?)""", (filename, LR))
#does not include a row for inclmplete cycles                      
            for axis in ["x", "y", "z"]:
                for function in ["max", "min"]:
                    if function=="max":
                        fun = max
                    else:
                        fun = min
                    c.execute(f"""UPDATE StepUp_Max_Table
                              SET 
                              {function}_Knee_Angle_{axis} = ?,
                              {function}_Knee_Moment_{axis} = ?,
                              {function}_Knee_Force_{axis} = ?,
                              {function}_Knee_Power_{axis} = ?,
                              {function}_Hip_Angle_{axis} = ?,
                              {function}_Hip_Moment_{axis} = ?,
                              {function}_Hip_Force_{axis} = ?,
                              {function}_Hip_Power_{axis} = ?,
                              {function}_Ankle_Angle_{axis} = ?,
                              {function}_Ankle_Moment_{axis} = ?,
                              {function}_Ankle_Force_{axis} = ?,
                              {function}_Ankle_Power_{axis} =  ?,
                              {function}_Foot_Progression_Angle_{axis} = ?,
                              {function}_pelvis_Angle_{axis} =  ?,
                              {function}_COM_{axis} =  ?
                              WHERE filename_StepUp = ? and Limb = ?
                              """,(
                              (fun(((patient["StepUp"][TrialNum][LR]["KneeAngle"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["KneeMoment"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["KneeForce"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["KneePower"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["HipAngle"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["HipMoment"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["HipForce"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["HipPower"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["AnkleAngle"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["AnkleMoment"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["AnkleForce"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["AnklePower"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["FootProgressAngle"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["pelvisAngle"][axis])[1:-1]))),
                              (fun(((patient["StepUp"][TrialNum][LR]["COM"][axis])[1:-1]))),
                              filename, LR
                              ))

def writetodict():
    name = str(vID.get()) + str(vtype.get()) + str(vmonth.get()) + ".json"
    with open(name, 'w') as f:
        json.dump(patient, f, indent = 5)                        

#FRAME 9: ACCEPT OR CANCEL
buttonaccept = Button(FrameClose, text = "Accept",
                      command = lambda: [enter_patient_data(), 
                                         enter_StepUp_Table(numTrialslist), 
                                         close_window(), writetodict(), 
                                         enter_StepUp_extrema(numTrialslist)])
buttonaccept.grid(column = 1, row = 1, padx = 10, pady = 20)
buttoncancel = Button(FrameClose, text = "Cancel", command = lambda: close_window())
buttoncancel.grid(column=2, row = 1, padx = 10)






"""Close the GUI"""
root.mainloop()


 















"""Test if input into SQLite"""
def selectall():
    c.execute("""SELECT * FROM StepUp_Table""")
    rows = c.fetchall()
    for row in rows:
        print(row)

def selectall2():
    c.execute("""SELECT * FROM Patient_Data""")
    lines = c.fetchall()
    for line in lines:
        print(line)
        
        
def selectall3():
    c.execute("""SELECT filename_StepUp, 
              Complete_Left_Cycle, Complete_Right_Cycle, 
              Left_Footstrike_Index, Left_FootOff_Index,
              Right_Footstrike_Index, Right_FootOff_Index 
              FROM StepUp_Table""")
    lines = c.fetchall()
    for line in lines:
        print(line)
        #
def selectall4():
    c.execute("""SELECT * FROM StepUp_Max_Table """)
    rows = c.fetchall()
    for row in rows:
        print(row)

def selectall5():
    c.execute("""SELECT max_Ankle_Angle_x, min_Ankle_Angle_x, 
              max_Ankle_Angle_x, min_Ankle_Angle_x FROM StepUp_Max_Table """)
    rows = c.fetchall()
    for row in rows:
        print(row)
#selectall()  
#selectall2()
#selectall3()
selectall5()







"""Close SQLite Connection"""
conn.commit()
conn.close()     
