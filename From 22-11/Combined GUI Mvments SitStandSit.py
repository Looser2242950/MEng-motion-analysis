# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:35:35 2020

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


"""Tab 3: STS"""



#Display filenames + whether clean or not    
InfoFrameSTS = Frame(tab4,bg = "DodgerBlue3", bd = 6)
InfoFrameSTS.pack(fill = BOTH)
SelectFrameSTS = Frame(tab4,bg = "DodgerBlue3", bd = 6)
SelectFrameSTS.pack(fill = BOTH)
TrialFrameSTS1= Frame(tab4,bg = "DodgerBlue3")
TrialFrameSTS1.pack(fill = BOTH)   
TrialFrameSTS2= Frame(tab4,bg = "DodgerBlue3")
TrialFrameSTS2.pack(fill = BOTH)

FrameTrial1STS = Frame(TrialFrameSTS1, bg = "ivory3", bd = 6)
FrameTrial1STS.pack()
FrameTrial2STS = Frame(TrialFrameSTS1, bg = "ghost white", bd = 6)
FrameTrial2STS.pack()
FrameTrial3STS = Frame(TrialFrameSTS1, bg = "ivory3", bd = 6)
FrameTrial3STS.pack()
FrameTrial4STS = Frame(TrialFrameSTS1, bg = "ghost white", bd = 6)
FrameTrial4STS.pack()
FrameTrial5STS = Frame(TrialFrameSTS1, bg = "ivory3", bd = 6)
FrameTrial5STS.pack()
FrameTrial6STS = Frame(TrialFrameSTS1, bg = "ghost white", bd = 6)
FrameTrial6STS.pack()
Framebottom = Frame(TrialFrameSTS2, bg = "DodgerBlue3", bd = 6)
Framebottom.pack()


labelSTS = Label(InfoFrameSTS, text = "STS")
labelSTS["font"] = myFont
labelSTS.pack()

labelbottom = Label(Framebottom, height = 1,  bg = "DodgerBlue3")
labelbottom.pack()

label_file_explorer1STS = Label(FrameTrial1STS,  text = "", width = 50, height = 3 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1STS.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer2STS = Label(FrameTrial2STS,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer2STS.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer3STS = Label(FrameTrial3STS,  text = "", width = 50, height = 3,  fg = "blue", bg = "ghost white") 
label_file_explorer3STS.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer4STS = Label(FrameTrial4STS,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer4STS.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 


label_file_explorer5STS = Label(FrameTrial5STS,  text = "", width = 50, height = 3,  fg = "blue", bg = "ghost white") 
label_file_explorer5STS.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 


label_file_explorer6STS = Label(FrameTrial6STS,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer6STS.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 



STS = {}
def browseFilesSTS(Limb): 
    ##sdc.set(1)
    global TriallistSTS 
    global filelistSTS
    TriallistSTS = []
    filelistSTS = []

    filenames = (filedialog.askopenfilenames(
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                      ("all files", "*.*"))))
    #creates a tuple therefore must turn into a list
    filelistSTS = list(filenames)
    length = len(filelistSTS)

    for i in range(length):
        TriallistSTS.append("Trial "+str(i+1))
        STS[TriallistSTS[i]]={}
        filelistSTS[i]=os.path.basename(filelistSTS[i])
        STS[TriallistSTS[i]].update({"Filename": filelistSTS[i]})
        if i == 0:
            label_file_explorer1STS.configure(text="File Opened: "+filelistSTS[i])
        if i == 1:
            label_file_explorer2STS.configure(text="File Opened: "+filelistSTS[i])
        if i == 2:
            label_file_explorer3STS.configure(text="File Opened: "+filelistSTS[i])
        if i == 3:
            label_file_explorer4STS.configure(text="File Opened: "+filelistSTS[i])
        if i == 4:
            label_file_explorer5STS.configure(text="File Opened: "+filelistSTS[i])
        if i == 5:
            label_file_explorer6STS.configure(text="File Opened: "+filelistSTS[i])

            
            
button_exploreSTS = Button(SelectFrameSTS, text = "Select Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesSTS("Left")])  
button_exploreSTS.pack(pady=10) 



root.mainloop()




def extractintoDictSTS(filename, TrialNum, Limb):     
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
        x["C7"] = (trial.GetPoint("C7")).GetValues()
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
        x["C7"] = (trial.GetPoint("C7")).GetValues()
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
    ##y.update({"C7 Velocity x": np.gradient(y["Left"]["C7"]["x"])*100})
    return y


def extract_all_STS_files():
    for i in range(len(TriallistSTS)): 
        STS[TriallistSTS[i]].update(extractintoDictSTS(filelistSTS[i], TriallistSTS[i], "Left"))
        STS[TriallistSTS[i]].update(extractintoDictSTS(filelistSTS[i], TriallistSTS[i], "Right"))
        STS[TriallistSTS[i]].update({"C7 Velocity x": ((np.gradient(STS[TriallistSTS[i]]["Left"]["C7"]["x"])*100).tolist())})
extract_all_STS_files() 


def split_STS():
    for i in range(len(TriallistSTS)): 
        Triallen = len(STS[TriallistSTS[i]]["Left"]["HipAngle"]["x"])
        thirdlen = int(Triallen/3)
        print(Triallen)
        print(Triallen/2)
        c7velx= np.array(STS[TriallistSTS[i]]["C7 Velocity x"])
        hipx = np.array(STS[TriallistSTS[i]]["Left"]["HipAngle"]["x"])
        c7z = np.array(STS[TriallistSTS[i]]["Left"]["C7"]["z"])
        
        #when the veloity of the C7 marker exceeds the threshold of 0.m/s (100mm/s)in the anterior (negative) direction
        StartStanding = (np.where(c7velx[thirdlen:Triallen]<=-100))[0][0]+thirdlen
        
        #maxC7SitStand is the maximum value in the second half of the full trial (from len/2 to len)
        maxC7SitStand=np.max(c7z[thirdlen:Triallen])
        StopStanding = (np.where(c7z==maxC7SitStand))[0][0]
        
        #Stand to Sit Initiation Index where the hip angle first breaks 10 degrees
        StartSitting = (np.where(hipx>10))[0][0]
        
        #Stand to Sit completion index where the c7 velocity is about 0 for at least 0.25s
        stableindices = np.where((c7velx<50)&(c7velx >-50))[0]
        indices_in_row =[f for f in np.split(stableindices, np.where(np.diff(stableindices)>1)[0]) if len(f)>=25][0]
        StopSitting = indices_in_row[1]
        
        
        STS[TriallistSTS[i]].update({"SitStandCompletion":StopStanding})
        STS[TriallistSTS[i]].update({"SitStandInitiation":StartStanding})
        STS[TriallistSTS[i]].update({"StandSitInitiation":StartSitting})
        STS[TriallistSTS[i]].update({"StandSitCompletion":StopSitting})

split_STS()

STS["StandtoSit"]={}
for i in range(len(TriallistSTS)):
    STS["StandtoSit"][TriallistSTS[i]]={}
    for LR in ["Left", "Right"]:
        STS["StandtoSit"][TriallistSTS[i]][LR]={}
        for key in STS[TriallistSTS[i]]["Left"].keys():
            STS["StandtoSit"][TriallistSTS[i]][LR][key]={}
            for axis in ["x", "y", "z"]:
                STS["StandtoSit"][TriallistSTS[i]][LR][key][axis]={}
                
            # y["Left"][key] = {
            #         'x':arr[:,0].tolist(),
            #         'y':arr[:,1].tolist(),
            #         'z':arr[:,2].tolist()
            #         }
        

# STS["max"]= {}
# STS["min"] = {}

# TriallistSTSl = []
# TriallistSTSr = []
# for i in range(len(TriallistSTS)):
#     if (va[i]).get()=="Left":
#         TriallistSTSl.append(TriallistSTS[i])
#     if (va[i]).get()=="Right":
#         TriallistSTSr.append(TriallistSTS[i])
#     if (va[i]).get()=="Both":
#         TriallistSTSr.append(TriallistSTS[i])
#         TriallistSTSl.append(TriallistSTS[i])
        
# def meanmaxminvals(limb, cleantrials, function):
#         o={}
#         if function == "max":
#             fun = max
#         if function == "min":
#             fun = min
#         for move in ["KneeAngle", "KneeForce", "KneeMoment", "KneePower", 
#                      "HipAngle", "HipForce", "HipMoment", "HipPower",
#                      "AnkleAngle", "AnkleForce", "AnkleMoment", "AnklePower",
#                      "FootProgressAngle", "pelvisAngle", "COM"]:
#             o[move]={}
#             for axis in ["x","y","z"]:
#                 if len(cleantrials)== 3:
#                     o[move][axis] = (((fun(STS[cleantrials[0]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[1]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[2]][limb][move][axis])))/3)                    
#                 if len(cleantrials)== 4:
#                     o[move][axis] = (((fun(STS[cleantrials[0]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[1]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[2]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[3]][limb][move][axis])))/4)
                    
#                 if len(cleantrials)== 5:
#                     o[move][axis] = (((fun(STS[cleantrials[0]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[1]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[2]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[3]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[4]][limb][move][axis])))/5)
#                 if len(cleantrials)== 6:
#                     o[move][axis] = (((fun(STS[cleantrials[0]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[1]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[2]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[3]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[4]][limb][move][axis]))+
#                                                              (fun(STS[cleantrials[5]][limb][move][axis])))/6)

#         return o


# STS["max"].update({"Left":  meanmaxminvals("Left", TriallistSTSl, "max")})
# STS["max"].update({"Right":  meanmaxminvals("Right", TriallistSTSr, "max")})
# STS["min"].update({"Left":  meanmaxminvals("Left", TriallistSTSl, "min")})
# STS["min"].update({"Right":  meanmaxminvals("Right", TriallistSTSr, "min")})
 






# ID = str(123545)
# dom_limb = "left"
# aff_limb = "left"
# tpe = "con"
# mon = "4"
# sex = "f"



# def create_STS_Max_Min_Table():
#         c.execute("""CREATE TABLE IF NOT EXISTS STS_Max_Min_Table
#               (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
#                Sex TEXT, Month TEXT, Affected_Limb TEXT)""")            
# def columns_STS_Max_Min_Table():
#     for limb in ["Left", "Right"]:
#         for axis in ["x", "y", "z"]:
#             for function in ["max", "min"]:
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Angle_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Moment_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Force_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Power_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Angle_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Moment_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Force_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Power_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Angle_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Moment_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Force_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Power_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_Foot_Progression_Angle_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_pelvis_Angle_{axis} REAL""")
#                c.execute(f"""ALTER TABLE STS_Max_Min_Table ADD COLUMN {function}_{limb}_COM_{axis} REAL""")   

# def enter_STS_extrema ():  
#     c.execute("""INSERT INTO STS_Max_Min_Table 
#               (ID, Dominant_Limb, Patient_Type, 
#               Sex, Month, Affected_Limb)VALUES (?,?,?,?,?,?)""", 
#              (ID, dom_limb, tpe, sex, mon, aff_limb))
#     for limb in ["Left", "Right"]:
#         for axis in ["x", "y", "z"]:
#             for function in ["max", "min"]:
#                 c.execute(f"""UPDATE STS_Max_Min_Table
#                           SET 
#                           {function}_{limb}_Knee_Angle_{axis} = ?,
#                           {function}_{limb}_Knee_Moment_{axis} = ?,
#                           {function}_{limb}_Knee_Force_{axis} = ?,
#                           {function}_{limb}_Knee_Power_{axis} = ?,
#                           {function}_{limb}_Hip_Angle_{axis} = ?,
#                           {function}_{limb}_Hip_Moment_{axis} = ?,
#                           {function}_{limb}_Hip_Force_{axis} = ?,
#                           {function}_{limb}_Hip_Power_{axis} = ?,
#                           {function}_{limb}_Ankle_Angle_{axis} = ?,
#                           {function}_{limb}_Ankle_Moment_{axis} = ?,
#                           {function}_{limb}_Ankle_Force_{axis} = ?,
#                           {function}_{limb}_Ankle_Power_{axis} =  ?,
#                           {function}_{limb}_Foot_Progression_Angle_{axis} = ?,
#                           {function}_{limb}_pelvis_Angle_{axis} =  ?,
#                           {function}_{limb}_COM_{axis} =  ?
#                           WHERE ID = ?
#                           """,(
#                           (STS[function][limb]["KneeAngle"][axis]),
#                           (STS[function][limb]["KneeMoment"][axis]),
#                           (STS[function][limb]["KneeForce"][axis]),
#                           (STS[function][limb]["KneePower"][axis]),
#                           (STS[function][limb]["HipAngle"][axis]),
#                           (STS[function][limb]["HipMoment"][axis]),
#                           (STS[function][limb]["HipForce"][axis]),
#                           (STS[function][limb]["HipPower"][axis]),
#                           (STS[function][limb]["AnkleAngle"][axis]),
#                           (STS[function][limb]["AnkleMoment"][axis]),
#                           (STS[function][limb]["AnkleForce"][axis]),
#                           (STS[function][limb]["AnklePower"][axis]),
#                           (STS[function][limb]["FootProgressAngle"][axis]),
#                           (STS[function][limb]["pelvisAngle"][axis]),
#                           (STS[function][limb]["COM"][axis]),
#                           ID
#                           ))

# create_STS_Max_Min_Table()
# columns_STS_Max_Min_Table()
# enter_STS_extrema()

              
# def create_STS_Table():
#         c.execute("""CREATE TABLE IF NOT EXISTS STS_Table
#               (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
#               Sex TEXT, Month TEXT, Affected_Limb TEXT,
#               Filename TEXT, Complete_Left_Cycle TEXT, Complete_Right_Cycle TEXT,
#               Left_Footstrike_Index TEXT, Left_FootOff_Index TEXT,
#               Right_Footstrike_Index TEXT, Right_FootOff_Index TEXT)""")            
# def columns_STS_Table():
#      for LR in ["Left", "Right"]:
#          for axis in ["x", "y", "z"]:
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Knee_Angle_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Knee_Moment_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Knee_Force_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Knee_Power_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Hip_Angle_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Hip_Moment_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Hip_Force_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Hip_Power_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Ankle_Angle_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Ankle_Moment_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Ankle_Force_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Ankle_Power_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_Foot_Progression_Angle_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_pelvis_Angle_{axis} TEXT""")
#              c.execute(f"""ALTER TABLE STS_Table ADD COLUMN {LR}_COM_{axis} TEXT""")             


# def enter_STS_Table (numTrials):
#     for TrialNum in numTrials:
#         filename = STS[TrialNum]["Filename"] 
#         c.execute("""INSERT INTO STS_Table 
#                   (ID, Dominant_Limb, Patient_Type, 
#                   Sex, Month, Affected_Limb, Filename) 
#                   VALUES (?,?,?,?,?,?,?)""", 
#                   (ID, dom_limb, tpe, sex, mon, aff_limb, 
#                    filename))
#         for LR in ["Left", "Right"]:
#             try:
#                 for axis in ["x", "y", "z"]:
#                     c.execute(f"""UPDATE STS_Table
#                               SET 
#                               {LR}_Knee_Angle_{axis} = ?,
#                               {LR}_Hip_Angle_{axis} = ?,
#                               {LR}_Ankle_Angle_{axis} = ?,
#                               {LR}_Foot_Progression_Angle_{axis} = ?,
#                               {LR}_pelvis_Angle_{axis} =  ?,
#                               {LR}_COM_{axis} =  ?,
#                               {LR}_Knee_Moment_{axis} = ?,
#                               {LR}_Knee_Force_{axis} = ?,
#                               {LR}_Knee_Power_{axis} = ?,
#                               {LR}_Hip_Moment_{axis} = ?,
#                               {LR}_Hip_Force_{axis} = ?,
#                               {LR}_Hip_Power_{axis} = ?,
#                               {LR}_Ankle_Moment_{axis} = ?,
#                               {LR}_Ankle_Force_{axis} = ?,
#                               {LR}_Ankle_Power_{axis} =  ?
#                               WHERE Filename = ?
#                               """,(
#                               (str(STS[TrialNum][LR]["KneeAngle"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["HipAngle"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["AnkleAngle"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["FootProgressAngle"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["pelvisAngle"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["COM"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["KneeMoment"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["KneeForce"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["KneePower"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["HipMoment"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["HipForce"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["HipPower"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["AnkleMoment"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["AnkleForce"][axis])[1:-1]),
#                               (str(STS[TrialNum][LR]["AnklePower"][axis])[1:-1]),
#                               filename
#                               ))
#             except:
#                 pass


# create_STS_Table()
# columns_STS_Table()
# enter_STS_Table(TriallistSTS)

# def select_all():
#     c.execute("SELECT * FROM 'STS_Table'")
#     rows = c.fetchall()
#     for row in rows:
#         print(row)
# #select_all()

# def select_all2():
#     c.execute("SELECT Left_Knee_Angle_x[0] FROM 'STS_Table'")
#     rows = c.fetchall()
#     for row in rows:
#         print(row)
# #select_all2()

# def select_all3():
#     c.execute("SELECT * FROM 'STS_Max_Min_Table'")
#     rows = c.fetchall()
#     for row in rows:
#         print(row)
# select_all3()

"""Close SQLite Connection"""
conn.commit()
conn.close()     
hi = STS
# plt.plot(STS["Right"]["Trial 1"]["KneeAngle"]["x"], "r")
# plt.plot(STS["Right"]["Trial 2"]["KneeAngle"]["x"], "b")
# plt.plot(STS["Right"]["Trial 3"]["KneeAngle"]["x"], "g")
# plt.show()
# plt.plot(STS["Left"]["Trial 1"]["KneeAngle"]["x"], "r")
# plt.plot(STS["Left"]["Trial 2"]["KneeAngle"]["x"], "b")
# plt.plot(STS["Left"]["Trial 3"]["KneeAngle"]["x"], "g")
# plt.show()