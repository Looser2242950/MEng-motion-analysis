# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:00:47 2020

@author: JLooser
"""


import numpy as np
import sys
import btk
import sqlite3
import json
from tkinter import *
from tkinter import filedialog 
import os.path 
from tkinter import ttk
import tkinter.font as font
import matplotlib.pyplot as plt
import statistics
plt.style.use('ggplot')
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.constrained_layout.use'] = False

"""Start SQLite Connection""" 
conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('MotionAnalysis106.db')
c=conn.cursor()
root = Tk()

#SetUp Tabs
tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)
tab6 = ttk.Frame(tab_parent)
tab7 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text = "Patient Data")
tab_parent.add(tab2, text = "Gait")
tab_parent.add(tab3, text = "Step Up")
tab_parent.add(tab4, text = "Step Down")
tab_parent.add(tab5, text = "Sit Stand Sit")
tab_parent.add(tab6, text = "Single Leg Balance")
tab_parent.add(tab7, text = "Ramp Walk")
tab_parent.pack(expand=1, fill="both")

myFont = font.Font(family = "Helvetica", size=20)


"""Tab 3: Stepup"""



#Display filenames + whether clean or not    
InfoFrameStepUp = Frame(tab3,bg = "DodgerBlue3", bd = 6)
InfoFrameStepUp.pack(fill = BOTH)
SelectFrameStepUp = Frame(tab3,bg = "DodgerBlue3", bd = 6)
SelectFrameStepUp.pack(fill = BOTH)
TrialFrameStepUp1= Frame(tab3,bg = "DodgerBlue3")
TrialFrameStepUp1.pack(fill = BOTH)   
TrialFrameStepUp2= Frame(tab3,bg = "DodgerBlue3")
TrialFrameStepUp2.pack(fill = BOTH)

FrameTrial1StepUp = Frame(TrialFrameStepUp1, bg = "ivory3", bd = 6)
FrameTrial1StepUp.pack()
FrameTrial2StepUp = Frame(TrialFrameStepUp1, bg = "ghost white", bd = 6)
FrameTrial2StepUp.pack()
FrameTrial3StepUp = Frame(TrialFrameStepUp1, bg = "ivory3", bd = 6)
FrameTrial3StepUp.pack()
FrameTrial4StepUp = Frame(TrialFrameStepUp1, bg = "ghost white", bd = 6)
FrameTrial4StepUp.pack()
FrameTrial5StepUp = Frame(TrialFrameStepUp1, bg = "ivory3", bd = 6)
FrameTrial5StepUp.pack()
FrameTrial6StepUp = Frame(TrialFrameStepUp1, bg = "ghost white", bd = 6)
FrameTrial6StepUp.pack()
# Framebottom = Frame(TrialFrameStepUp, bg = "DodgerBlue3", bd = 6)
# Framebottom.pack()


labelStepUp = Label(InfoFrameStepUp, text = "StepUp")
labelStepUp["font"] = myFont
labelStepUp.pack()

# labelbottom = Label(Framebottom, height = 1,  bg = "DodgerBlue3")
# labelbottom.pack()

label_file_explorer1StepUp = Label(FrameTrial1StepUp,  text = "", width = 50, height = 3 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSU1=StringVar()
vSU1.set(0)
radio_left_1StepUp = Radiobutton(FrameTrial1StepUp, text = "Left", variable = vSU1, value="Left")
radio_right_1StepUp = Radiobutton(FrameTrial1StepUp, text ="Right", variable = vSU1, value = "Right")
radio_both_1StepUp = Radiobutton(FrameTrial1StepUp, text ="Both", variable = vSU1, value = "Both")
radio_left_1StepUp.grid(column = 2,row = 1)
radio_right_1StepUp.grid(column = 3,row = 1)
radio_both_1StepUp.grid(column = 4,row = 1)

label_file_explorer2StepUp = Label(FrameTrial2StepUp,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer2StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSU2=StringVar()
vSU2.set(0)
radio_left_2StepUp = Radiobutton(FrameTrial2StepUp, text = "Left", variable = vSU2, value="Left")
radio_right_2StepUp = Radiobutton(FrameTrial2StepUp, text ="Right", variable = vSU2, value = "Right")
radio_both_2StepUp = Radiobutton(FrameTrial2StepUp, text ="Both", variable = vSU2, value = "Both")
radio_left_2StepUp.grid(column = 2,row = 1)
radio_right_2StepUp.grid(column = 3,row = 1)
radio_both_2StepUp.grid(column = 4,row = 1)

label_file_explorer3StepUp = Label(FrameTrial3StepUp,  text = "", width = 50, height = 3,  fg = "blue", bg = "ghost white") 
label_file_explorer3StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSU3=StringVar()
vSU3.set(0)
radio_left_3StepUp = Radiobutton(FrameTrial3StepUp, text = "Left", variable = vSU3, value="Left")
radio_right_3StepUp = Radiobutton(FrameTrial3StepUp, text ="Right", variable = vSU3, value = "Right")
radio_both_3StepUp = Radiobutton(FrameTrial3StepUp, text ="Both", variable = vSU3, value = "Both")
radio_left_3StepUp.grid(column = 2,row = 1)
radio_right_3StepUp.grid(column = 3,row = 1)
radio_both_3StepUp.grid(column = 4,row = 1)

label_file_explorer4StepUp = Label(FrameTrial4StepUp,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer4StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSU4=StringVar()
vSU4.set(0)
radio_left_4StepUp = Radiobutton(FrameTrial4StepUp, text = "Left", variable = vSU4, value="Left")
radio_right_4StepUp = Radiobutton(FrameTrial4StepUp, text ="Right", variable = vSU4, value = "Right")
radio_both_4StepUp = Radiobutton(FrameTrial4StepUp, text ="Both", variable = vSU4, value = "Both")
radio_left_4StepUp.grid(column = 2,row = 1)
radio_right_4StepUp.grid(column = 3,row = 1)
radio_both_4StepUp.grid(column = 4,row = 1)

label_file_explorer5StepUp = Label(FrameTrial5StepUp,  text = "", width = 50, height = 3,  fg = "blue", bg = "ghost white") 
label_file_explorer5StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSU5=StringVar()
vSU5.set(0)
radio_left_5StepUp = Radiobutton(FrameTrial5StepUp, text = "Left", variable = vSU5, value="Left")
radio_right_5StepUp = Radiobutton(FrameTrial5StepUp, text ="Right", variable = vSU5, value = "Right")
radio_both_5StepUp = Radiobutton(FrameTrial5StepUp, text ="Both", variable = vSU5, value = "Both")
radio_left_5StepUp.grid(column = 2,row = 1)
radio_right_5StepUp.grid(column = 3,row = 1)
radio_both_5StepUp.grid(column = 4,row = 1)

label_file_explorer6StepUp = Label(FrameTrial6StepUp,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer6StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSU6=StringVar()
vSU6.set(0)
radio_left_6StepUp = Radiobutton(FrameTrial6StepUp, text = "Left", variable = vSU6, value="Left")
radio_right_6StepUp = Radiobutton(FrameTrial6StepUp, text ="Right", variable = vSU6, value = "Right")
radio_both_6StepUp = Radiobutton(FrameTrial6StepUp, text ="Both", variable = vSU6, value = "Both")
radio_left_6StepUp.grid(column = 2,row = 1)
radio_right_6StepUp.grid(column = 3,row = 1)
radio_both_6StepUp.grid(column = 4,row = 1)


StepUp = {}
def browseFilesStepUp(Limb): 
    ##sdc.set(1)
    global TriallistStepUp 
    global filelistStepUp
    TriallistStepUp = []
    filelistStepUp = []

    filenames = (filedialog.askopenfilenames(
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                      ("all files", "*.*"))))
    #creates a tuple therefore must turn into a list
    filelistStepUp = list(filenames)
    length = len(filelistStepUp)

    for i in range(length):
        TriallistStepUp.append("Trial "+str(i+1))
        StepUp[TriallistStepUp[i]]={}
        filelistStepUp[i]=os.path.basename(filelistStepUp[i])
        StepUp[TriallistStepUp[i]].update({"Filename": filelistStepUp[i]})
        if i == 0:
            label_file_explorer1StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 1:
            label_file_explorer2StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 2:
            label_file_explorer3StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 3:
            label_file_explorer4StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 4:
            label_file_explorer5StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 5:
            label_file_explorer6StepUp.configure(text="File Opened: "+filelistStepUp[i])

            
            
button_exploreStepUp = Button(SelectFrameStepUp, text = "Select up to 3 LEFT Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesStepUp("Left")])  
button_exploreStepUp.pack(pady=10)
vStrath = IntVar()
vStrath.set(0)
check_strath = Checkbutton(SelectFrameStepUp, text ="Check if Strathclyde Stepping Trial", variable = vStrath)
check_strath.pack()

  



root.mainloop()




def extractintoDictStepUp(filename, TrialNum, Limb):     
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename) # set a filename to the reader
    reader.Update()
    trialacq = reader.GetOutput() # is the btk aquisition object
    def extractvaluesl(trial):
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
    def extractvaluesr(trial):
        #extracts al the arrays
        #can be used for all trials, just needs to be instantiated with the correct trial
        x = dict();  
        x["KneeAngle"]= (trial.GetPoint("RKneeAngles")).GetValues()
        x["KneeForce"]= (trial.GetPoint("RKneeForce")).GetValues()
        x["KneeMoment"]= (trial.GetPoint("RKneeMoment")).GetValues()
        x["KneePower"]= (trial.GetPoint("RKneePower")).GetValues() 
        x["HipAngle"]= ((trial.GetPoint("RHipAngles")).GetValues())
        x["HipForce"]= (trial.GetPoint("RHipForce")).GetValues()
        x["HipMoment"]= (trial.GetPoint("RHipMoment")).GetValues()
        x["HipPower"]= (trial.GetPoint("RHipPower")).GetValues() 
        x["AnkleAngle"]= (trial.GetPoint("RAnkleAngles")).GetValues()
        x["AnkleForce"]= (trial.GetPoint("RAnkleForce")).GetValues()
        x["AnkleMoment"]= (trial.GetPoint("RAnkleMoment")).GetValues()
        x["AnklePower"]= (trial.GetPoint("RAnklePower")).GetValues()    
        x["FootProgressAngle"] = (trial.GetPoint("RFootProgressAngles")).GetValues()
        x["pelvisAngle"] = (trial.GetPoint("RPelvisAngles")).GetValues() 
        x["COM"] = (trial.GetPoint("CentreOfMass")).GetValues()
        return x
    y = {}
    
    
    if Limb == "Left":
        y["Left"] = {}
        y["Left"].update(extractvaluesl(trialacq))
        for key in y["Left"].keys():
            arr = y["Left"][key]
            y["Left"][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
        
    if Limb== "Right":
        y["Right"] = {}
        y["Right"].update(extractvaluesr(trialacq))
        for key in y["Right"].keys():
            arr = y["Right"][key]
            y["Right"][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
    return y


def extract_all_StepUp_files():
    def cleanextract(v, trialnum, filename):
        z={}
        if v.get() == "Left":
            z.update(extractintoDictStepUp(filename, trialnum, "Left"))
        if v.get() =="Right":
            z.update(extractintoDictStepUp(filename, trialnum, "Right"))
        if v.get() =="Both":
            z.update(extractintoDictStepUp(filename, trialnum, "Left"))
            z.update(extractintoDictStepUp(filename, trialnum, "Right"))
        return z
    for i in range(len(TriallistStepUp)):           
        if vStrath.get()==0:
            StepUp[TriallistStepUp[i]].update(cleanextract(va[i], TriallistStepUp[i], filelistStepUp[i]))
            StepUp[TriallistStepUp[i]].update({"Testing Type": "Single Step"})
        if vStrath.get()==1:
            StepUp[TriallistStepUp[i]].update(cleanextract(va[i], TriallistStepUp[i], filelistStepUp[i]))
            StepUp[TriallistStepUp[i]].update({"Testing Type": "Strathclyde Steps"})
va= [vSU1, vSU2, vSU3, vSU4, vSU5, vSU6]
extract_all_StepUp_files() 


StepUp["max"]= {}
StepUp["min"] = {}

TriallistStepUpl = []
TriallistStepUpr = []
for i in range(len(TriallistStepUp)):
    if (va[i]).get()=="Left":
        TriallistStepUpl.append(TriallistStepUp[i])
    if (va[i]).get()=="Right":
        TriallistStepUpr.append(TriallistStepUp[i])
    if (va[i]).get()=="Both":
        TriallistStepUpr.append(TriallistStepUp[i])
        TriallistStepUpl.append(TriallistStepUp[i])
        
def meanmaxminvals(limb, cleantrials, function):
        o={}
        if function == "max":
            fun = max
        if function == "min":
            fun = min
        for move in ["KneeAngle", "KneeForce", "KneeMoment", "KneePower", 
                     "HipAngle", "HipForce", "HipMoment", "HipPower",
                     "AnkleAngle", "AnkleForce", "AnkleMoment", "AnklePower",
                     "FootProgressAngle", "pelvisAngle", "COM"]:
            o[move]={}
            for axis in ["x","y","z"]:
                if len(cleantrials)== 3:
                    o[move][axis] = (((fun(StepUp[cleantrials[0]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[1]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[2]][limb][move][axis])))/3)                    
                if len(cleantrials)== 4:
                    o[move][axis] = (((fun(StepUp[cleantrials[0]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[1]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[2]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[3]][limb][move][axis])))/4)
                    
                if len(cleantrials)== 5:
                    o[move][axis] = (((fun(StepUp[cleantrials[0]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[1]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[2]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[3]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[4]][limb][move][axis])))/5)
                if len(cleantrials)== 6:
                    o[move][axis] = (((fun(StepUp[cleantrials[0]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[1]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[2]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[3]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[4]][limb][move][axis]))+
                                                             (fun(StepUp[cleantrials[5]][limb][move][axis])))/6)

        return o


StepUp["max"].update({"Left":  meanmaxminvals("Left", TriallistStepUpl, "max")})
StepUp["max"].update({"Right":  meanmaxminvals("Right", TriallistStepUpr, "max")})
StepUp["min"].update({"Left":  meanmaxminvals("Left", TriallistStepUpl, "min")})
StepUp["min"].update({"Right":  meanmaxminvals("Right", TriallistStepUpr, "min")})
 






ID = str(123545)
dom_limb = "left"
aff_limb = "left"
tpe = "con"
mon = "4"
sex = "f"



def create_StepUp_Max_Min_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepUp_Max_Min_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
               Sex TEXT, Month TEXT, Affected_Limb TEXT)""")            
def columns_StepUp_Max_Min_Table():
    for limb in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Moment_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Force_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Power_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Moment_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Force_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Power_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Moment_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Force_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Power_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Foot_Progression_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_pelvis_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_COM_{axis} REAL""")   

def enter_StepUp_extrema ():  
    c.execute("""INSERT INTO StepUp_Max_Min_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb)VALUES (?,?,?,?,?,?)""", 
             (ID, dom_limb, tpe, sex, mon, aff_limb))
    for limb in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
                c.execute(f"""UPDATE StepUp_Max_Min_Table
                          SET 
                          {function}_{limb}_Knee_Angle_{axis} = ?,
                          {function}_{limb}_Knee_Moment_{axis} = ?,
                          {function}_{limb}_Knee_Force_{axis} = ?,
                          {function}_{limb}_Knee_Power_{axis} = ?,
                          {function}_{limb}_Hip_Angle_{axis} = ?,
                          {function}_{limb}_Hip_Moment_{axis} = ?,
                          {function}_{limb}_Hip_Force_{axis} = ?,
                          {function}_{limb}_Hip_Power_{axis} = ?,
                          {function}_{limb}_Ankle_Angle_{axis} = ?,
                          {function}_{limb}_Ankle_Moment_{axis} = ?,
                          {function}_{limb}_Ankle_Force_{axis} = ?,
                          {function}_{limb}_Ankle_Power_{axis} =  ?,
                          {function}_{limb}_Foot_Progression_Angle_{axis} = ?,
                          {function}_{limb}_pelvis_Angle_{axis} =  ?,
                          {function}_{limb}_COM_{axis} =  ?
                          WHERE ID = ?
                          """,(
                          (StepUp[function][limb]["KneeAngle"][axis]),
                          (StepUp[function][limb]["KneeMoment"][axis]),
                          (StepUp[function][limb]["KneeForce"][axis]),
                          (StepUp[function][limb]["KneePower"][axis]),
                          (StepUp[function][limb]["HipAngle"][axis]),
                          (StepUp[function][limb]["HipMoment"][axis]),
                          (StepUp[function][limb]["HipForce"][axis]),
                          (StepUp[function][limb]["HipPower"][axis]),
                          (StepUp[function][limb]["AnkleAngle"][axis]),
                          (StepUp[function][limb]["AnkleMoment"][axis]),
                          (StepUp[function][limb]["AnkleForce"][axis]),
                          (StepUp[function][limb]["AnklePower"][axis]),
                          (StepUp[function][limb]["FootProgressAngle"][axis]),
                          (StepUp[function][limb]["pelvisAngle"][axis]),
                          (StepUp[function][limb]["COM"][axis]),
                          ID
                          ))

create_StepUp_Max_Min_Table()
columns_StepUp_Max_Min_Table()
enter_StepUp_extrema()

              
def create_StepUp_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepUp_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
              Sex TEXT, Month TEXT, Affected_Limb TEXT,
              Filename TEXT, Complete_Left_Cycle TEXT, Complete_Right_Cycle TEXT,
              Left_Footstrike_Index TEXT, Left_FootOff_Index TEXT,
              Right_Footstrike_Index TEXT, Right_FootOff_Index TEXT)""")            
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


def enter_StepUp_Table (numTrials):
    for TrialNum in numTrials:
        filename = StepUp[TrialNum]["Filename"] 
        c.execute("""INSERT INTO StepUp_Table 
                  (ID, Dominant_Limb, Patient_Type, 
                  Sex, Month, Affected_Limb, Filename) 
                  VALUES (?,?,?,?,?,?,?)""", 
                  (ID, dom_limb, tpe, sex, mon, aff_limb, 
                   filename))
        for LR in ["Left", "Right"]:
            try:
                for axis in ["x", "y", "z"]:
                    c.execute(f"""UPDATE StepUp_Table
                              SET 
                              {LR}_Knee_Angle_{axis} = ?,
                              {LR}_Hip_Angle_{axis} = ?,
                              {LR}_Ankle_Angle_{axis} = ?,
                              {LR}_Foot_Progression_Angle_{axis} = ?,
                              {LR}_pelvis_Angle_{axis} =  ?,
                              {LR}_COM_{axis} =  ?,
                              {LR}_Knee_Moment_{axis} = ?,
                              {LR}_Knee_Force_{axis} = ?,
                              {LR}_Knee_Power_{axis} = ?,
                              {LR}_Hip_Moment_{axis} = ?,
                              {LR}_Hip_Force_{axis} = ?,
                              {LR}_Hip_Power_{axis} = ?,
                              {LR}_Ankle_Moment_{axis} = ?,
                              {LR}_Ankle_Force_{axis} = ?,
                              {LR}_Ankle_Power_{axis} =  ?
                              WHERE Filename = ?
                              """,(
                              (str(StepUp[TrialNum][LR]["KneeAngle"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["HipAngle"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["AnkleAngle"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["FootProgressAngle"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["pelvisAngle"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["COM"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["KneeMoment"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["KneeForce"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["KneePower"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["HipMoment"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["HipForce"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["HipPower"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["AnkleMoment"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["AnkleForce"][axis])[1:-1]),
                              (str(StepUp[TrialNum][LR]["AnklePower"][axis])[1:-1]),
                              filename
                              ))
            except:
                pass


create_StepUp_Table()
columns_StepUp_Table()
enter_StepUp_Table(TriallistStepUp)

def select_all():
    c.execute("SELECT * FROM 'StepUp_Table'")
    rows = c.fetchall()
    for row in rows:
        print(row)
#select_all()

def select_all2():
    c.execute("SELECT Left_Knee_Angle_x[0] FROM 'StepUp_Table'")
    rows = c.fetchall()
    for row in rows:
        print(row)
#select_all2()

def select_all3():
    c.execute("SELECT * FROM 'StepUp_Max_Min_Table'")
    rows = c.fetchall()
    for row in rows:
        print(row)
select_all3()

"""Close SQLite Connection"""
conn.commit()
conn.close()     

# plt.plot(StepUp["Right"]["Trial 1"]["KneeAngle"]["x"], "r")
# plt.plot(StepUp["Right"]["Trial 2"]["KneeAngle"]["x"], "b")
# plt.plot(StepUp["Right"]["Trial 3"]["KneeAngle"]["x"], "g")
# plt.show()
# plt.plot(StepUp["Left"]["Trial 1"]["KneeAngle"]["x"], "r")
# plt.plot(StepUp["Left"]["Trial 2"]["KneeAngle"]["x"], "b")
# plt.plot(StepUp["Left"]["Trial 3"]["KneeAngle"]["x"], "g")
# plt.show()