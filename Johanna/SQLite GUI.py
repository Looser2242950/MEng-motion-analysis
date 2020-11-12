# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:32:42 2020

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

filename1 = None
filename2 = None
filename3 = None
filename4 = None
filename5 = None
filename6 = None
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
              Filename_Gait_Trial_1 TEXT, Filename_Gait_Trial_2 TEXT, Filename_Gait_Trial_3 TEXT,
              Filename_Gait_Trial_4 TEXT,Filename_Gait_Trial_5 TEXT, Filename_Gait_Trial_6 TEXT
              )""")
              #add Filename_STS_Trial_1,.... for different movements             
def create_Gait_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Gait_Table
              (Filename TEXT, Complete_Left_Cycle TEXT, Complete_Right_Cycle TEXT,
              Left_Footstrike_Index TEXT, Left_FootOff_Index TEXT,
              Right_Footstrike_Index TEXT, Right_FootOff_Index TEXT)""")            
def columns_Gait_Table():
     for LR in ["Left", "Right"]:
         for axis in ["x", "y", "z"]:
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Knee_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Knee_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Knee_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Knee_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Hip_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Hip_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Hip_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Hip_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Ankle_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Ankle_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Ankle_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Ankle_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Foot_Progression_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_GRF_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_NGRF_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_pelvis_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_COM_{axis} TEXT""")             
              
create_patient_data_table()
create_Gait_Table()
columns_Gait_Table()







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

#FILE SELECTORS +Filename changes
def browseFiles1(): 
    global filename1
    filename1 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))
    label_file_explorer1.configure(text="File Opened: "+filename1)
    numTrialslist.append("Trial 1")


def browseFiles2(): 
    global filename2
    filename2 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
        ("all files", "*.*"))))  
    label_file_explorer2.configure(text="File Opened: "+filename2)
    numTrialslist.append("Trial 2")
    
def browseFiles3(): 
    global filename3
    filename3 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))  
    label_file_explorer3.configure(text="File Opened: "+filename3) 
    numTrialslist.append("Trial 3")
    
def browseFiles4(): 
    global filename4
    filename4 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))  
    label_file_explorer4.configure(text="File Opened: "+filename4) 
    numTrialslist.append("Trial 4")

def browseFiles5(): 
    global filename5
    filename5 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))  
    label_file_explorer5.configure(text="File Opened: "+filename5) 
    numTrialslist.append("Trial 5")

def browseFiles6(): 
    global filename6
    filename6 = os.path.basename(filedialog.askopenfilename(
        initialdir = "C:/Users/johan/Documents/MEng FYP/C3D_files", 
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                     ("all files", "*.*"))))  
    label_file_explorer6.configure(text="File Opened: "+filename6) 
    numTrialslist.append("Trial 6")



#EXCTRACT AND NORMALISE DATA
def cutcycle(footstrike, data):
    footstrike1 = footstrike[0]
    footstrike2 = footstrike[1]
    data1 = (data[footstrike1:footstrike2])
    return data1
    
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
    x["GRF"] = (trial.GetPoint("LGroundReactionForce")).GetValues()
    x["NGRF"] = (trial.GetPoint("LNormalisedGRF")).GetValues()
    x["pelvisAngle"] = (trial.GetPoint("LPelvisAngles")).GetValues() 
    x["COM"] = (trial.GetPoint("CentreOfMass")).GetValues()
    return x

def extractintoDict(filename, TrialNum):
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename) # set a filename to the reader
    reader.Update()
    trialacq = reader.GetOutput() # is the btk aquisition object
    patient["Gait"][TrialNum] ={}
    patient["Gait"][TrialNum].update({"Left": extractvalues(trialacq)})
    patient["Gait"][TrialNum].update({"Right": extractvalues(trialacq)})
    patient["Gait"][TrialNum].update({"lfootstrikeFrame":[]})
    patient["Gait"][TrialNum].update({"rfootstrikeFrame":[]})
    patient["Gait"][TrialNum].update({"lfootoffFrame":[]})
    patient["Gait"][TrialNum].update({"rfootoffFrame":[]})
    patient["Gait"][TrialNum].update({"startframe":trialacq.GetFirstFrame()})#first frame of data
    # #instantiate the nested dict to input in the footstrike etc

    
    for i in range(trialacq.GetEventNumber()):
        eventnum = trialacq.GetEvent(i)
        if eventnum.GetLabel()=="Foot Strike":
            if eventnum.GetContext() == "Left":
                patient["Gait"][TrialNum]["lfootstrikeFrame"].append(eventnum.GetFrame()-patient["Gait"][TrialNum]["startframe"])
            else:
                patient["Gait"][TrialNum]["rfootstrikeFrame"].append(eventnum.GetFrame()-patient["Gait"][TrialNum]["startframe"])
        if eventnum.GetLabel()=="Foot Off":
            if eventnum.GetContext() == "Left":
                patient["Gait"][TrialNum]["lfootoffFrame"].append(eventnum.GetFrame()-patient["Gait"][TrialNum]["startframe"])
            else:
                patient["Gait"][TrialNum]["rfootoffFrame"].append(eventnum.GetFrame()-patient["Gait"][TrialNum]["startframe"])

    for event in ["lfootstrikeFrame", "rfootstrikeFrame", "lfootoffFrame", "rfootoffFrame"]:
        patient["Gait"][TrialNum][event].sort()   
    
    if len(patient["Gait"][TrialNum]["lfootstrikeFrame"])>1:
        patient["Gait"][TrialNum]["Left"]["KneeAngle"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["KneeAngle"])
        patient["Gait"][TrialNum]["Left"]["KneeForce"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["KneeForce"])
        patient["Gait"][TrialNum]["Left"]["KneeMoment"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["KneeMoment"])
        patient["Gait"][TrialNum]["Left"]["KneePower"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["KneePower"])
        
        patient["Gait"][TrialNum]["Left"]["HipAngle"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["HipAngle"])
        patient["Gait"][TrialNum]["Left"]["HipForce"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["HipForce"])
        patient["Gait"][TrialNum]["Left"]["HipMoment"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["HipMoment"])
        patient["Gait"][TrialNum]["Left"]["HipPower"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["HipPower"])
        
        patient["Gait"][TrialNum]["Left"]["AnkleAngle"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["AnkleAngle"])
        patient["Gait"][TrialNum]["Left"]["AnkleForce"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["AnkleForce"])
        patient["Gait"][TrialNum]["Left"]["AnkleMoment"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["AnkleMoment"])
        patient["Gait"][TrialNum]["Left"]["AnklePower"] = cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["AnklePower"])
    
        patient["Gait"][TrialNum]["Left"]["FootProgressAngle"] =cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["FootProgressAngle"])
        patient["Gait"][TrialNum]["Left"]["GRF"] =cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["GRF"])
        patient["Gait"][TrialNum]["Left"]["NGRF"] =cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["NGRF"])
        patient["Gait"][TrialNum]["Left"]["pelvisAngle"] =cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["pelvisAngle"])  
        patient["Gait"][TrialNum]["Left"]["COM"] =cutcycle(patient["Gait"][TrialNum]["lfootstrikeFrame"], patient["Gait"][TrialNum]["Left"]["COM"])
    #else:
        #print("no full left limb gait cycle")
    if len(patient["Gait"][TrialNum]["rfootstrikeFrame"])>1:
        patient["Gait"][TrialNum]["Right"]["KneeAngle"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["KneeAngle"])
        patient["Gait"][TrialNum]["Right"]["KneeForce"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["KneeForce"])
        patient["Gait"][TrialNum]["Right"]["KneeMoment"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["KneeMoment"])
        patient["Gait"][TrialNum]["Right"]["KneePower"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["KneePower"])
        
        patient["Gait"][TrialNum]["Right"]["HipAngle"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["HipAngle"])
        patient["Gait"][TrialNum]["Right"]["HipForce"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["HipForce"])
        patient["Gait"][TrialNum]["Right"]["HipMoment"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["HipMoment"])
        patient["Gait"][TrialNum]["Right"]["HipPower"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["HipPower"])
        
        patient["Gait"][TrialNum]["Right"]["AnkleAngle"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["AnkleAngle"])
        patient["Gait"][TrialNum]["Right"]["AnkleForce"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["AnkleForce"])
        patient["Gait"][TrialNum]["Right"]["AnkleMoment"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["AnkleMoment"])
        patient["Gait"][TrialNum]["Right"]["AnklePower"] = cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["AnklePower"])
        
        patient["Gait"][TrialNum]["Right"]["FootProgressAngle"] =cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["FootProgressAngle"])
        patient["Gait"][TrialNum]["Right"]["GRF"] =cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["GRF"])
        patient["Gait"][TrialNum]["Right"]["NGRF"] =cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["NGRF"])
        patient["Gait"][TrialNum]["Right"]["pelvisAngle"] =cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["pelvisAngle"])
        patient["Gait"][TrialNum]["Right"]["COM"] =cutcycle(patient["Gait"][TrialNum]["rfootstrikeFrame"], patient["Gait"][TrialNum]["Right"]["COM"])
    # else:
    #     print("no full right limb gait cycle")
    
    for LR in ['Right','Left']:
        for key in patient["Gait"][TrialNum][LR].keys():
            arr = patient["Gait"][TrialNum][LR][key]
            patient["Gait"][TrialNum][LR][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
     
    #call other function"returnvalues" to extract rest of data
    #returnvalues(trialacq)
    global ID
    ID = trialacq.GetEvent(0).GetSubject()
    vID.set(ID)
    
    







def cleanvalues1():
    if len(patient["Gait"]["Trial 1"]["lfootstrikeFrame"])>1:
        label_clean1.configure(text = "Clean Left Gait Cycle")
        global cleanleft1
        cleanleft1 = "Yes"
    else:
        label_clean1.configure(text = "Incomplete Left Gait Cycle")
    if len(patient["Gait"]["Trial 1"]["rfootstrikeFrame"])>1:
        label_clean1r.configure(text = "Clean Right Gait Cycle")
        global cleanright1
        cleanright1 = "Yes"
    else:
        label_clean1r.configure(text = "Incomplete Right Gait Cycle")
        
def cleanvalues2():        
    if len(patient["Gait"]["Trial 2"]["lfootstrikeFrame"])>1:
        label_clean2.configure(text = "Clean Left Gait Cycle")
        global cleanleft2
        cleanleft2 = "Yes"
    else:
        label_clean2.configure(text = "Incomplete Left Gait Cycle")
    if len(patient["Gait"]["Trial 2"]["rfootstrikeFrame"])>1:
        label_clean2r.configure(text = "Clean Right Gait Cycle")
        global cleanright2
        cleanright2 = "Yes"
    else:
        label_clean2r.configure(text = "Incomplete Right Gait Cycle")
    
def cleanvalues3():        
    if len(patient["Gait"]["Trial 3"]["lfootstrikeFrame"])>1:
        label_clean3.configure(text = "Clean Left Gait Cycle")
        global cleanleft3
        cleanleft3 = "Yes"
    else:
        label_clean3.configure(text = "Incomplete Left Gait Cycle")
    if len(patient["Gait"]["Trial 3"]["rfootstrikeFrame"])>1:
        label_clean3r.configure(text = "Clean Right Gait Cycle")
        global cleanright3
        cleanright3 = "Yes"
    else:
        label_clean3r.configure(text = "Incomplete Right Gait Cycle")

def cleanvalues4():        
    if len(patient["Gait"]["Trial 4"]["lfootstrikeFrame"])>1:
        label_clean4.configure(text = "Clean Left Gait Cycle")
        global cleanleft4
        cleanleft4 = "Yes"
    else:
        label_clean4.configure(text = "Incomplete Left Gait Cycle")
    if len(patient["Gait"]["Trial 4"]["rfootstrikeFrame"])>1:
        label_clean4r.configure(text = "Clean Right Gait Cycle")
        global cleanright4
        cleanright4 = "Yes"
    else:
        label_clean4r.configure(text = "Incomplete Right Gait Cycle")

def cleanvalues5():        
    if len(patient["Gait"]["Trial 5"]["lfootstrikeFrame"])>1:
        label_clean5.configure(text = "Clean Left Gait Cycle")
        global cleanleft5
        cleanleft5 = "Yes"
    else:
        label_clean5.configure(text = "Incomplete Left Gait Cycle")
    if len(patient["Gait"]["Trial 5"]["rfootstrikeFrame"])>1:
        label_clean5r.configure(text = "Clean Right Gait Cycle")
        global cleanright5
        cleanright5 = "Yes"
    else:
        label_clean5r.configure(text = "Incomplete Right Gait Cycle")

def cleanvalues6():        
    if len(patient["Gait"]["Trial 6"]["lfootstrikeFrame"])>1:
        label_clean6.configure(text = "Clean Left Gait Cycle")
        global cleanleft6
        cleanleft6 = "Yes"
    else:
        label_clean6.configure(text = "Incomplete Left Gait Cycle")
    if len(patient["Gait"]["Trial 6"]["rfootstrikeFrame"])>1:
        label_clean6r.configure(text = "Clean Right Gait Cycle")
        global cleanright6
        cleanright6 = "Yes"
    else:
        label_clean6r.configure(text = "Incomplete Right Gait Cycle")



def new_index(filename, TrialNum):
    if len(patient["Gait"][TrialNum]["lfootstrikeFrame"])>1:
        patient["Gait"][TrialNum]["lfootoffFrame"]=(np.array(patient["Gait"][TrialNum]["lfootoffFrame"])- 
                                                    (patient["Gait"][TrialNum]["lfootstrikeFrame"])[0]).tolist()
        patient["Gait"][TrialNum]["lfootstrikeFrame"]=(np.array(patient["Gait"][TrialNum]["lfootstrikeFrame"])-
                                                       (patient["Gait"][TrialNum]["lfootstrikeFrame"])[0]).tolist()
    for item in patient["Gait"][TrialNum]["lfootoffFrame"]:
        if item <0:
            patient["Gait"][TrialNum]["lfootoffFrame"].remove(item)
 
    if len(patient["Gait"][TrialNum]["rfootstrikeFrame"])>1:
        patient["Gait"][TrialNum]["rfootoffFrame"]=(np.array(patient["Gait"][TrialNum]["rfootoffFrame"])-
          (patient["Gait"][TrialNum]["rfootstrikeFrame"])[0]).tolist()
        patient["Gait"][TrialNum]["rfootstrikeFrame"]=(np.array(patient["Gait"][TrialNum]["rfootstrikeFrame"])-
          (patient["Gait"][TrialNum]["rfootstrikeFrame"])[0]).tolist()
    for item in patient["Gait"][TrialNum]["rfootoffFrame"]:
        if item <0:
            patient["Gait"][TrialNum]["rfootoffFrame"].remove(item)       
 
    

def close_window():
    root.destroy()
    



"""Initialise the Dict"""
patient = {}
patient["Gait"] = {}




"""GUI Widgets"""
#FRAME 1: INFO
label_info1 = Label(FrameLabel, 
                    text = """Please select at least 3 Gait trials. 
                    Ensure a minimum of 3 complete gait cycles on each limb. """, 
                   bg = "ivory3", height = 2)
label_info1.grid()
label_info2 = Label(FrameLabel, 
                    text = "Input the patient data and select Accept to enter into the database.", 
                    bg = "ivory3", height = 2)
label_info2.grid()


#FRAMES 2-7: INDIVIDUAL TRIAL SELECTIONS
button_explore1 = Button(FrameTrial1, text = "Select Trial 1",  width = 12, bg = "ghost white",
                         command = lambda : [browseFiles1(), extractintoDict(filename1, "Trial 1"), 
                                             cleanvalues1(), new_index(filename1, "Trial 1")])  
label_file_explorer1 = Label(FrameTrial1,  text = "", width = 80, height = 3 ,  fg = "blue" , bg = "ghost white") 
button_explore1.grid(column = 1, row = 1, rowspan = 2) 
label_file_explorer1.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean1 = Label(FrameTrial1, text="",  width = 25, bg = "ivory3")
label_clean1.grid(column = 10, row = 1)
label_clean1r = Label(FrameTrial1, text="",  width = 25, bg = "ivory3")
label_clean1r.grid(column = 10, row = 2)



button_explore2 = Button(FrameTrial2, text = "Select Trial 2",   width = 12,
                         command = lambda : [browseFiles2(), extractintoDict(filename2, "Trial 2"), 
                                             cleanvalues2(), new_index(filename2, "Trial 2")])  
label_file_explorer2 = Label(FrameTrial2,  text = "", width = 80, height = 3,  fg = "blue", bg = "ivory2") 
button_explore2.grid(column = 1 , row = 1, rowspan = 2)
label_file_explorer2.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean2 = Label(FrameTrial2, text=" ",  width = 25, bg = "ghost white")
label_clean2.grid(column = 10, row = 1)
label_clean2r = Label(FrameTrial2, text="",  width = 25, bg = "ghost white")
label_clean2r.grid(column = 10, row = 2)



button_explore3 = Button(FrameTrial3, text = "Select Trial 3",  width = 12, bg = "ghost white",
                         command = lambda : [browseFiles3(), extractintoDict(filename3, "Trial 3"), 
                                             cleanvalues3(), new_index(filename3, "Trial 3") ])  
label_file_explorer3 = Label(FrameTrial3,  text = "", width = 80, height = 3,  fg = "blue", bg = "ghost white") 
button_explore3.grid(column = 1 , row = 1, rowspan = 2) 
label_file_explorer3.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean3 = Label(FrameTrial3, text=" ",  width = 25, bg = "ivory3")
label_clean3.grid(column = 10, row = 1)
label_clean3r = Label(FrameTrial3, text="",  width = 25, bg = "ivory3")
label_clean3r.grid(column = 10, row = 2)



button_explore4 = Button(FrameTrial4, text = "Select Trial 4",   width = 12,
                         command = lambda : [browseFiles4(), extractintoDict(filename4, "Trial 4"), 
                                             cleanvalues4(), new_index(filename4, "Trial 4")])  
label_file_explorer4 = Label(FrameTrial4,  text = "", width = 80, height = 3,  fg = "blue", bg = "ivory2") 
button_explore4.grid(column = 1 , row = 1, rowspan = 2) 
label_file_explorer4.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean4 = Label(FrameTrial4, text=" ",  width = 25, bg = "ghost white")
label_clean4.grid(column = 10, row = 1)
label_clean4r = Label(FrameTrial4, text="",  width = 25, bg = "ghost white")
label_clean4r.grid(column = 10, row = 2)


button_explore5 = Button(FrameTrial5, text = "Select Trial 5",   width = 12,bg = "ghost white",
                         command = lambda : [browseFiles5(), extractintoDict(filename5, "Trial 5"), 
                                             cleanvalues5(), new_index(filename4, "Trial 4")])  
label_file_explorer5 = Label(FrameTrial5,  text = "", width = 80, height = 3,  fg = "blue", bg = "ghost white") 
button_explore5.grid(column = 1 , row = 1, rowspan = 2) 
label_file_explorer5.grid(column = 2, row = 1, columnspan = 7, rowspan = 2) 
label_clean5 = Label(FrameTrial5, text=" ",  width = 25, bg = "ivory3")
label_clean5.grid(column = 10, row = 1)
label_clean5r = Label(FrameTrial5, text="",  width = 25, bg = "ivory3")
label_clean5r.grid(column = 10, row = 2)



button_explore6 = Button(FrameTrial6, text = "Select Trial 6",  width = 12,
                         command = lambda : [browseFiles6(), extractintoDict(filename6, "Trial 6"), 
                                             cleanvalues6(), new_index(filename4, "Trial 4")])  
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
              Filename_Gait_Trial_1, Filename_Gait_Trial_2, Filename_Gait_Trial_3,
              Filename_Gait_Trial_4, Filename_Gait_Trial_5, Filename_Gait_Trial_6)
              VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
              (vID.get(), vDom.get(), vtype.get(), vmonth.get(), vlimb.get(),
               filename1, filename2, filename3, filename4, filename5, filename6))

def enter_Gait_Table (numTrials):
    for TrialNum in numTrials:
        if TrialNum=="Trial 1":
            filename = filename1
            cleanleft = cleanleft1
            cleanright = cleanright1
        if TrialNum=="Trial 2":
            filename = filename2
            cleanleft = cleanleft2
            cleanright = cleanright2
        if TrialNum=="Trial 3":
            filename = filename3
            cleanleft = cleanleft3
            cleanright = cleanright3
        if TrialNum=="Trial 4":
            filename = filename4
            cleanleft = cleanleft4
            cleanright = cleanright4
        if TrialNum=="Trial 5":
            filename = filename5
            cleanleft = cleanleft5
            cleanright = cleanright5
        if TrialNum=="Trial 6":
            filename = filename6
            cleanleft = cleanleft6
            cleanright = cleanright6
         
        c.execute("""INSERT INTO Gait_Table 
                  (Filename, Complete_left_Cycle, Complete_Right_Cycle, 
                  Left_Footstrike_Index, Left_FootOff_Index, 
                  Right_Footstrike_Index, Right_FootOff_Index) 
                  VALUES (?,?,?,?,?,?,?)""", (filename, cleanleft, cleanright,
                  (str(patient["Gait"][TrialNum]["lfootstrikeFrame"])),
                  (str(patient["Gait"][TrialNum]["lfootoffFrame"])),
                  (str(patient["Gait"][TrialNum]["rfootstrikeFrame"])),
                  (str(patient["Gait"][TrialNum]["rfootoffFrame"]))))
        for LR in ["Left", "Right"]:
            for axis in ["x", "y", "z"]:
                c.execute(f"""UPDATE Gait_Table
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
                          {LR}_GRF_{axis} =  ?,
                          {LR}_NGRF_{axis} =  ?,
                          {LR}_pelvis_Angle_{axis} =  ?,
                          {LR}_COM_{axis} =  ?
                          WHERE Filename = ?
                          """,(
                          (str(patient["Gait"][TrialNum][LR]["KneeAngle"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["KneeMoment"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["KneeForce"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["KneePower"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["HipAngle"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["HipMoment"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["HipForce"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["HipPower"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["AnkleAngle"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["AnkleMoment"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["AnkleForce"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["AnklePower"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["FootProgressAngle"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["GRF"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["NGRF"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["pelvisAngle"][axis])[1:-1]),
                          (str(patient["Gait"][TrialNum][LR]["COM"][axis])[1:-1]),
                          filename
                          ))


                        

#FRAME 9: ACCEPT OR CANCEL
buttonaccept = Button(FrameClose, text = "Accept", 
                      command  = lambda: [enter_patient_data(), enter_Gait_Table(numTrialslist), close_window()])
buttonaccept.grid(column = 1, row = 1, padx = 10, pady = 20)
buttoncancel = Button(FrameClose, text = "Cancel", command = lambda: close_window())
buttoncancel.grid(column=2, row  = 1, padx = 10)






"""Close the GUI"""
root.mainloop()




"""Write Dict to JSON"""
name = str(vID.get()) + str(vtype.get()) + str(vmonth.get()) + ".json"
with open(name, 'w') as f:
      json.dump(patient, f, indent = 5)















"""Test if input into SQLite"""
def selectall():
    c.execute("""SELECT * FROM Gait_Table""")
    rows = c.fetchall()
    for row in rows:
        print(row)

def selectall2():
    c.execute("""SELECT * FROM Patient_Data""")
    lines = c.fetchall()
    for line in lines:
        print(line)
        
        
def selectall3():
    c.execute("""SELECT Filename, 
              Complete_Left_Cycle, Complete_Right_Cycle, 
              Left_Footstrike_Index, Left_FootOff_Index,
              Right_Footstrike_Index, Right_FootOff_Index 
              FROM Gait_Table""")
    lines = c.fetchall()
    for line in lines:
        print(line)
        #
#selectall()  
selectall2()
selectall3()







"""Close SQLite Connection"""
conn.commit()
conn.close()     




