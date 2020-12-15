# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:21:46 2020

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


"""Tab 2: Gait"""

InfoFrameGait = Frame(tab2,bg = "DodgerBlue3", bd = 6)
InfoFrameGait.pack(fill = BOTH)
SelectFrameGait = Frame(tab2,bg = "DodgerBlue3", bd = 6)
SelectFrameGait.pack(fill = BOTH)
TrialFrameGait= Frame(tab2,bg = "DodgerBlue3")
TrialFrameGait.pack(fill = BOTH)

#Display filenames + whether clean or not    
FrameTrial1Gait = Frame(TrialFrameGait, bg = "ivory3", bd = 6)
FrameTrial1Gait.pack()
FrameTrial2Gait = Frame(TrialFrameGait, bg = "ghost white", bd = 6)
FrameTrial2Gait.pack()
FrameTrial3Gait = Frame(TrialFrameGait, bg = "ivory3", bd = 6)
FrameTrial3Gait.pack()
FrameTrial4Gait = Frame(TrialFrameGait, bg = "ghost white", bd = 6)
FrameTrial4Gait.pack()
FrameTrial5Gait = Frame(TrialFrameGait, bg = "ivory3", bd = 6)
FrameTrial5Gait.pack()
FrameTrial6Gait = Frame(TrialFrameGait, bg = "ghost white", bd = 6)
FrameTrial6Gait.pack()
Framebottom = Frame(TrialFrameGait, bg = "DodgerBlue3", bd = 6)
Framebottom.pack()


labelGait = Label(InfoFrameGait, text = "Gait")
labelGait["font"] = myFont
labelGait.pack()

labelbottom = Label(Framebottom, height = 1,  bg = "DodgerBlue3")
labelbottom.pack()

label_file_explorer1Gait = Label(FrameTrial1Gait,  text = "", width = 50, height = 3 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1Gait.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
label_clean1Gait = Label(FrameTrial1Gait, text="",  width = 25, bg = "ivory3")
label_clean1Gait.grid(column = 2, row = 1)
label_clean1rGait = Label(FrameTrial1Gait, text="",  width = 25, bg = "ivory3")
label_clean1rGait.grid(column = 2, row = 2)

label_file_explorer2Gait = Label(FrameTrial2Gait,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer2Gait.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
label_clean2Gait = Label(FrameTrial2Gait, text=" ",  width = 25, bg = "ghost white")
label_clean2Gait.grid(column = 2, row = 1)
label_clean2rGait = Label(FrameTrial2Gait, text="",  width = 25, bg = "ghost white")
label_clean2rGait.grid(column = 2, row = 2)

label_file_explorer3Gait = Label(FrameTrial3Gait,  text = "", width = 50, height = 3,  fg = "blue", bg = "ghost white") 
label_file_explorer3Gait.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
label_clean3Gait = Label(FrameTrial3Gait, text=" ",  width = 25, bg = "ivory3")
label_clean3Gait.grid(column = 2, row = 1)
label_clean3rGait = Label(FrameTrial3Gait, text="",  width = 25, bg = "ivory3")
label_clean3rGait.grid(column = 2, row = 2)

label_file_explorer4Gait = Label(FrameTrial4Gait,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer4Gait.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
label_clean4Gait = Label(FrameTrial4Gait, text=" ",  width = 25, bg = "ghost white")
label_clean4Gait.grid(column = 2, row = 1)
label_clean4rGait = Label(FrameTrial4Gait, text="",  width = 25, bg = "ghost white")
label_clean4rGait.grid(column = 2, row = 2)

label_file_explorer5Gait = Label(FrameTrial5Gait,  text = "", width = 50, height = 3,  fg = "blue", bg = "ghost white") 
label_file_explorer5Gait.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
label_clean5Gait = Label(FrameTrial5Gait, text=" ",  width = 25, bg = "ivory3")
label_clean5Gait.grid(column = 2, row = 1)
label_clean5rGait = Label(FrameTrial5Gait, text="",  width = 25, bg = "ivory3")
label_clean5rGait.grid(column = 2, row = 2)

label_file_explorer6Gait = Label(FrameTrial6Gait,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer6Gait.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
label_clean6Gait = Label(FrameTrial6Gait, text=" ",  width = 25, bg = "ghost white")
label_clean6Gait.grid(column = 2, row = 1)
label_clean6rGait = Label(FrameTrial6Gait, text="",  width = 25, bg = "ghost white")
label_clean6rGait.grid(column = 2, row = 2)



Gait = {}
def browseFilesGait(): 
    #gc.set(1)
    global filelistGait
    global TriallistGait
    TriallistGait = []
    filenames = (filedialog.askopenfilenames(
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                      ("all files", "*.*"))))
    #creates a tuple therefore must tur into a list
    filelistGait = list(filenames)
    length = len(filelistGait)
    for i in range(length):
        TriallistGait.append("Trial "+str(i+1))
        Gait[TriallistGait[i]]={}
        filelistGait[i]=os.path.basename(filelistGait[i])
        Gait[TriallistGait[i]].update({"Filename": filelistGait[i]})
        if i == 0:
            label_file_explorer1Gait.configure(text="File Opened: "+filelistGait[i])
        if i == 1:
            label_file_explorer2Gait.configure(text="File Opened: "+filelistGait[i])
        if i == 2:
            label_file_explorer3Gait.configure(text="File Opened: "+filelistGait[i])
        if i == 3:
            label_file_explorer4Gait.configure(text="File Opened: "+filelistGait[i])
        if i == 4:
            label_file_explorer5Gait.configure(text="File Opened: "+filelistGait[i])
        if i == 5:
            label_file_explorer6Gait.configure(text="File Opened: "+filelistGait[i])
    print(filelistGait)
    print(length)
    print(TriallistGait)
cleanlefttrials=[]
cleanrighttrials=[]
#EXCTRACT AND NORMALISE DATA
def cutcycle(footstrike, data):
    footstrike1 = footstrike[0]
    footstrike2 = footstrike[1]
    datacut = (data[footstrike1:footstrike2])
    return datacut
    
def extractintoDict(filename, TrialNum):     
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename) # set a filename to the reader
    reader.Update()
    trialacq = reader.GetOutput() # is the btk aquisition object
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
        try:
            x["GRF"] = (trial.GetPoint("LGroundReactionForce")).GetValues()
        except:
            pass
        try:    
            x["NGRF"] = (trial.GetPoint("LNormalisedGRF")).GetValues()
        except:
            pass
        return x
    Gait[TrialNum].update({"Left": extractvalues(trialacq)})
    Gait[TrialNum].update({"Right": extractvalues(trialacq)})
    Gait[TrialNum].update({"lfootstrikeFrame":[]})
    Gait[TrialNum].update({"rfootstrikeFrame":[]})
    Gait[TrialNum].update({"lfootoffFrame":[]})
    Gait[TrialNum].update({"rfootoffFrame":[]})
    Gait[TrialNum].update({"startframe":trialacq.GetFirstFrame()})#first frame of data
    # #instantiate the nested dict to input in the footstrike etc
    
    for i in range(trialacq.GetEventNumber()):
        eventnum = trialacq.GetEvent(i)
        if eventnum.GetLabel()=="Foot Strike":
            if eventnum.GetContext() == "Left":
                Gait[TrialNum]["lfootstrikeFrame"].append(eventnum.GetFrame()-Gait[TrialNum]["startframe"])
            else:
                Gait[TrialNum]["rfootstrikeFrame"].append(eventnum.GetFrame()-Gait[TrialNum]["startframe"])
        if eventnum.GetLabel()=="Foot Off":
            if eventnum.GetContext() == "Left":
                Gait[TrialNum]["lfootoffFrame"].append(eventnum.GetFrame()-Gait[TrialNum]["startframe"])
            else:
                Gait[TrialNum]["rfootoffFrame"].append(eventnum.GetFrame()-Gait[TrialNum]["startframe"])

    for event in ["lfootstrikeFrame", "rfootstrikeFrame", "lfootoffFrame", "rfootoffFrame"]:
        Gait[TrialNum][event].sort()   
    if TrialNum=="Trial 1":
        labelleft = label_clean1Gait
        labelright = label_clean1rGait
    if TrialNum=="Trial 2":
        labelleft = label_clean2Gait
        labelright = label_clean2rGait
    if TrialNum=="Trial 3":
        labelleft = label_clean3Gait
        labelright = label_clean3rGait
    if TrialNum=="Trial 4":
        labelleft = label_clean4Gait
        labelright = label_clean4rGait     
    if TrialNum=="Trial 5":
        labelleft = label_clean5Gait
        labelright = label_clean5rGait
    if TrialNum=="Trial 6":
        labelleft = label_clean6Gait
        labelright = label_clean6rGait
    
    if len(Gait[TrialNum]["lfootstrikeFrame"])>1:
        Gait[TrialNum].update({"Clean Left": "Yes"})
        cleanlefttrials.append(TrialNum)
        labelleft.configure(text = "Clean Left Gait Cycle")
        Gait[TrialNum]["Left"]["KneeAngle"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["KneeAngle"])
        Gait[TrialNum]["Left"]["KneeForce"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["KneeForce"])
        Gait[TrialNum]["Left"]["KneeMoment"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["KneeMoment"])
        Gait[TrialNum]["Left"]["KneePower"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["KneePower"])
        
        Gait[TrialNum]["Left"]["HipAngle"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["HipAngle"])
        Gait[TrialNum]["Left"]["HipForce"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["HipForce"])
        Gait[TrialNum]["Left"]["HipMoment"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["HipMoment"])
        Gait[TrialNum]["Left"]["HipPower"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["HipPower"])
        
        Gait[TrialNum]["Left"]["AnkleAngle"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["AnkleAngle"])
        Gait[TrialNum]["Left"]["AnkleForce"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["AnkleForce"])
        Gait[TrialNum]["Left"]["AnkleMoment"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["AnkleMoment"])
        Gait[TrialNum]["Left"]["AnklePower"] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["AnklePower"])
    
        Gait[TrialNum]["Left"]["FootProgressAngle"] =cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["FootProgressAngle"])
        try:
            Gait[TrialNum]["Left"]["GRF"] =cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["GRF"])
            Gait[TrialNum]["Left"]["NGRF"] =cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["NGRF"])
        except:
            pass
        Gait[TrialNum]["Left"]["pelvisAngle"] =cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["pelvisAngle"])  
        Gait[TrialNum]["Left"]["COM"] =cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["COM"])

        Gait[TrialNum]["lfootoffFrame"]=(np.array(Gait[TrialNum]["lfootoffFrame"])-(Gait[TrialNum]["lfootstrikeFrame"])[0]).tolist()
        Gait[TrialNum]["lfootstrikeFrame"]=(np.array(Gait[TrialNum]["lfootstrikeFrame"])-(Gait[TrialNum]["lfootstrikeFrame"])[0]).tolist()
    else:
        Gait[TrialNum].update({"Clean Left": "No"})
        labelleft.configure(text = "Incomplete Left Gait Cycle")
    for item in Gait[TrialNum]["lfootoffFrame"]:
        if item <0:
            Gait[TrialNum]["lfootoffFrame"].remove(item)
    if len(Gait[TrialNum]["rfootstrikeFrame"])>1:
        cleanrighttrials.append(TrialNum)
        Gait[TrialNum].update({"Clean Right": "Yes"})
        labelright.configure(text = "Clean Right Gait Cycle")
        Gait[TrialNum]["Right"]["KneeAngle"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["KneeAngle"])
        Gait[TrialNum]["Right"]["KneeForce"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["KneeForce"])
        Gait[TrialNum]["Right"]["KneeMoment"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["KneeMoment"])
        Gait[TrialNum]["Right"]["KneePower"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["KneePower"])
        
        Gait[TrialNum]["Right"]["HipAngle"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["HipAngle"])
        Gait[TrialNum]["Right"]["HipForce"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["HipForce"])
        Gait[TrialNum]["Right"]["HipMoment"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["HipMoment"])
        Gait[TrialNum]["Right"]["HipPower"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["HipPower"])
        
        Gait[TrialNum]["Right"]["AnkleAngle"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["AnkleAngle"])
        Gait[TrialNum]["Right"]["AnkleForce"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["AnkleForce"])
        Gait[TrialNum]["Right"]["AnkleMoment"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["AnkleMoment"])
        Gait[TrialNum]["Right"]["AnklePower"] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["AnklePower"])
        
        Gait[TrialNum]["Right"]["FootProgressAngle"] =cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["FootProgressAngle"])
        try:
            Gait[TrialNum]["Right"]["GRF"] =cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["GRF"])
            Gait[TrialNum]["Right"]["NGRF"] =cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["NGRF"])
        except:
            pass
        Gait[TrialNum]["Right"]["pelvisAngle"] =cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["pelvisAngle"])
        Gait[TrialNum]["Right"]["COM"] =cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["COM"])
        
        Gait[TrialNum]["rfootoffFrame"]=(np.array(Gait[TrialNum]["rfootoffFrame"])-(Gait[TrialNum]["rfootstrikeFrame"])[0]).tolist()
        Gait[TrialNum]["rfootstrikeFrame"]=(np.array(Gait[TrialNum]["rfootstrikeFrame"])-(Gait[TrialNum]["rfootstrikeFrame"])[0]).tolist()
    else:
        Gait[TrialNum].update({"Clean Right": "No"})
        labelright.configure(text = "Incomplete Right Gait Cycle")
    for item in Gait[TrialNum]["rfootoffFrame"]:
        if item <0:
            Gait[TrialNum]["rfootoffFrame"].remove(item)
    def footoff(cleantrials, footoff, footstrike):
        foot = []
        if len(cleantrials)== 3:
            foot = int((Gait[cleantrials[0]][footoff][0]/Gait[cleantrials[0]][footstrike][1]+
                       Gait[cleantrials[1]][footoff][0]/Gait[cleantrials[1]][footstrike][1]+
                       Gait[cleantrials[2]][footoff][0]/Gait[cleantrials[2]][footstrike][1])*100/3)
        if len(cleantrials)== 4:   
            foot = int((Gait[cleantrials[0]][footoff][0]/Gait[cleantrials[0]][footstrike][1]+
                       Gait[cleantrials[1]][footoff][0]/Gait[cleantrials[1]][footstrike][1]+
                       Gait[cleantrials[2]][footoff][0]/Gait[cleantrials[2]][footstrike][1]+
                       Gait[cleantrials[3]][footoff][0]/Gait[cleantrials[3]][footstrike][1])*100/4)
        if len(cleantrials)== 5:
            foot = int((Gait[cleantrials[0]][footoff][0]/Gait[cleantrials[0]][footstrike][1]+
                       Gait[cleantrials[1]][footoff][0]/Gait[cleantrials[1]][footstrike][1]+
                       Gait[cleantrials[2]][footoff][0]/Gait[cleantrials[2]][footstrike][1]+
                       Gait[cleantrials[3]][footoff][0]/Gait[cleantrials[3]][footstrike][1]+
                       Gait[cleantrials[4]][footoff][0]/Gait[cleantrials[4]][footstrike][1])*100/5)
        if len(cleantrials)== 6:
            foot = int((Gait[cleantrials[0]][footoff][0]/Gait[cleantrials[0]][footstrike][1]+
                       Gait[cleantrials[1]][footoff][0]/Gait[cleantrials[1]][footstrike][1]+
                       Gait[cleantrials[2]][footoff][0]/Gait[cleantrials[2]][footstrike][1]+
                       Gait[cleantrials[3]][footoff][0]/Gait[cleantrials[3]][footstrike][1]+
                       Gait[cleantrials[4]][footoff][0]/Gait[cleantrials[4]][footstrike][1]+
                       Gait[cleantrials[5]][footoff][0]/Gait[cleantrials[5]][footstrike][1])*100/6)
        return foot
    Gait["Left Average"] = {}
    Gait["Right Average"] = {}
    Gait["Left Average"].update({"FootOff": footoff(cleanlefttrials, "lfootoffFrame", "lfootstrikeFrame")})
    Gait["Right Average"].update({"FootOff": footoff(cleanrighttrials, "rfootoffFrame", "rfootstrikeFrame")})
    
    def interpolate(cutdata):
        increment = 100/len(cutdata)
        Timepercent = np.arange(0, 100, increment).tolist() 
        x = np.array(range(100))
        datainterp = np.interp(x, Timepercent, cutdata)
        return datainterp       

#make array into list for SQ:
    for key in Gait[TrialNum]["Left"].keys():
        arr = Gait[TrialNum]["Left"][key]
        if Gait[TrialNum]["Clean Left"]=="Yes":
            Gait[TrialNum]["Left"][key] = {
                    'x':(interpolate(arr[:,0])).tolist(),
                    'y':(interpolate(arr[:,1])).tolist(),
                    'z':(interpolate(arr[:,2])).tolist()
                    }
            
        else:
            Gait[TrialNum]["Left"][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
    for key in Gait[TrialNum]["Right"].keys():
        arr = Gait[TrialNum]["Right"][key]
        if Gait[TrialNum]["Clean Right"]=="Yes":
            Gait[TrialNum]["Right"][key] = {
                    'x':(interpolate(arr[:,0])).tolist(),
                    'y':(interpolate(arr[:,1])).tolist(),
                    'z':(interpolate(arr[:,2])).tolist()
                    }
        else:
            Gait[TrialNum]["Right"][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
    def meanvals(limb, cleantrials):
        o={}
        
        for move in ["KneeAngle", "KneeForce", "KneeMoment", "KneePower", 
                     "HipAngle", "HipForce", "HipMoment", "HipPower",
                     "AnkleAngle", "AnkleForce", "AnkleMoment", "AnklePower",
                     "FootProgressAngle", "pelvisAngle", "COM", "GRF", "NGRF"]:
            o[move]={}
            for axis in ["x","y","z"]:

                if len(cleantrials)== 3:
                    o[move][axis] = (np.mean((np.array(Gait[cleantrials[0]][limb][move][axis]),
                                                             np.array(Gait[cleantrials[1]][limb][move][axis]),
                                                             np.array(Gait[cleantrials[2]][limb][move][axis])), 
                                                             axis = 0)).tolist()
                    
                if len(cleantrials)== 4:
                    o[move][axis] = (np.mean((np.array(Gait[cleantrials[0]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[1]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[2]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[3]][limb][move][axis])),
                                                              axis = 0)).tolist()
                    
                if len(cleantrials)== 5:
                    o[move][axis] = (np.mean((np.array(Gait[cleantrials[0]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[1]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[2]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[3]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[4]][limb][move][axis])), 
                                                              axis = 0)).tolist()
                if len(cleantrials)== 6:
                    o[move][axis] = (np.mean((np.array(Gait[cleantrials[0]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[1]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[2]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[3]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[4]][limb][move][axis]),
                                                              np.array(Gait[cleantrials[5]][limb][move][axis])),
                                                              axis = 0)).tolist()

        return o


    Gait["Left Average"].update(meanvals("Left", cleanlefttrials))
    Gait["Right Average"].update(meanvals("Right", cleanrighttrials))
    
   


def extract_all_Gait_files():
    for i in range(len(TriallistGait)):
        extractintoDict(filelistGait[i], TriallistGait[i])
        
button_exploreGait = Button(SelectFrameGait, text = "Select up to 6 Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesGait(), extract_all_Gait_files()])  
button_exploreGait.pack(pady=10)




root.mainloop()






ID = str(123545)


def create_Mean_Gait_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Mean_Gait_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
               Sex TEXT, Month TEXT, Affected_Limb TEXT)""")            
def columns_Mean_Gait_Table():
     for LR in ["Left", "Right"]:
         for axis in ["x", "y", "z"]:
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Knee_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Knee_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Knee_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Knee_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Hip_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Hip_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Hip_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Hip_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Ankle_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Ankle_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Ankle_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Ankle_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Foot_Progression_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_GRF_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_NGRF_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_pelvis_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_COM_{axis} TEXT""")   

def enter_Mean_Gait_Table (limb_avl, limb_avr):
    c.execute("""INSERT INTO Mean_Gait_Table 
             (ID)VALUES (?)""", (ID,))
    for axis in ["x", "y", "z"]:
        c.execute(f"""UPDATE Mean_Gait_Table
                  SET 
                  Left_Knee_Angle_{axis} = ?,
                  Left_Knee_Moment_{axis} = ?,
                  Left_Knee_Force_{axis} = ?,
                  Left_Knee_Power_{axis} = ?,
                  Left_Hip_Angle_{axis} = ?,
                  Left_Hip_Moment_{axis} = ?,
                  Left_Hip_Force_{axis} = ?,
                  Left_Hip_Power_{axis} = ?,
                  Left_Ankle_Angle_{axis} = ?,
                  Left_Ankle_Moment_{axis} = ?,
                  Left_Ankle_Force_{axis} = ?,
                  Left_Ankle_Power_{axis} =  ?,
                  Left_Foot_Progression_Angle_{axis} = ?,
                  Left_GRF_{axis} =  ?,
                  Left_NGRF_{axis} =  ?,
                  Left_pelvis_Angle_{axis} =  ?,
                  Left_COM_{axis} =  ?,
                  Right_Knee_Angle_{axis} = ?,
                  Right_Knee_Moment_{axis} = ?,
                  Right_Knee_Force_{axis} = ?,
                  Right_Knee_Power_{axis} = ?,
                  Right_Hip_Angle_{axis} = ?,
                  Right_Hip_Moment_{axis} = ?,
                  Right_Hip_Force_{axis} = ?,
                  Right_Hip_Power_{axis} = ?,
                  Right_Ankle_Angle_{axis} = ?,
                  Right_Ankle_Moment_{axis} = ?,
                  Right_Ankle_Force_{axis} = ?,
                  Right_Ankle_Power_{axis} =  ?,
                  Right_Foot_Progression_Angle_{axis} = ?,
                  Right_GRF_{axis} =  ?,
                  Right_NGRF_{axis} =  ?,
                  Right_pelvis_Angle_{axis} =  ?,
                  Right_COM_{axis} =  ? 
                  WHERE ID = ?
                  """,(
                  (str(limb_avl["KneeAngle"][axis])[1:-1]),
                  (str(limb_avl["KneeMoment"][axis])[1:-1]),
                  (str(limb_avl["KneeForce"][axis])[1:-1]),
                  (str(limb_avl["KneePower"][axis])[1:-1]),
                  (str(limb_avl["HipAngle"][axis])[1:-1]),
                  (str(limb_avl["HipMoment"][axis])[1:-1]),
                  (str(limb_avl["HipForce"][axis])[1:-1]),
                  (str(limb_avl["HipPower"][axis])[1:-1]),
                  (str(limb_avl["AnkleAngle"][axis])[1:-1]),
                  (str(limb_avl["AnkleMoment"][axis])[1:-1]),
                  (str(limb_avl["AnkleForce"][axis])[1:-1]),
                  (str(limb_avl["AnklePower"][axis])[1:-1]),
                  (str(limb_avl["FootProgressAngle"][axis])[1:-1]),
                  (str(limb_avl["GRF"][axis])[1:-1]),
                  (str(limb_avl["NGRF"][axis])[1:-1]),
                  (str(limb_avl["pelvisAngle"][axis])[1:-1]),
                  (str(limb_avl["COM"][axis])[1:-1]),
                  (str(limb_avr["KneeAngle"][axis])[1:-1]),
                  (str(limb_avr["KneeMoment"][axis])[1:-1]),
                  (str(limb_avr["KneeForce"][axis])[1:-1]),
                  (str(limb_avr["KneePower"][axis])[1:-1]),
                  (str(limb_avr["HipAngle"][axis])[1:-1]),
                  (str(limb_avr["HipMoment"][axis])[1:-1]),
                  (str(limb_avr["HipForce"][axis])[1:-1]),
                  (str(limb_avr["HipPower"][axis])[1:-1]),
                  (str(limb_avr["AnkleAngle"][axis])[1:-1]),
                  (str(limb_avr["AnkleMoment"][axis])[1:-1]),
                  (str(limb_avr["AnkleForce"][axis])[1:-1]),
                  (str(limb_avr["AnklePower"][axis])[1:-1]),
                  (str(limb_avr["FootProgressAngle"][axis])[1:-1]),
                  (str(limb_avr["GRF"][axis])[1:-1]),
                  (str(limb_avr["NGRF"][axis])[1:-1]),
                  (str(limb_avr["pelvisAngle"][axis])[1:-1]),
                  (str(limb_avr["COM"][axis])[1:-1]),
                  ID
                  ))


#create_Mean_Gait_Table()
#columns_Mean_Gait_Table()
enter_Mean_Gait_Table(Gait["Left Average"],Gait["Right Average"])
# enter_Mean_Gait_Table(Gait["Right Average"])


def create_Gait_Max_Min_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Gait_Max_Min_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
               Sex TEXT, Month TEXT, Affected_Limb TEXT)""")            
def columns_Gait_Max_Min_Table():
    for phase in ["stance", "swing"]:
        for limb in ["Left", "Right"]:
            for axis in ["x", "y", "z"]:
                for function in ["max", "min"]:
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Angle_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Moment_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Force_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Power_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Angle_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Moment_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Force_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Power_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Angle_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Moment_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Force_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Power_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Foot_Progression_Angle_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_GRF_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_NGRF_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_pelvis_Angle_{axis}_{phase} REAL""")
                   c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_COM_{axis}_{phase} REAL""")   

def enter_Gait_extrema ():  
    c.execute("""INSERT INTO Gait_Max_Min_Table 
              (ID) 
              VALUES (?)""", (ID,))
    for phase in ["stance", "swing"]:
#does not include a row for inclmplete cycles                      
        if phase == "stance":
            startl = 0
            endl = Gait["Left Average"]["FootOff"]
            startr = 0
            endr = Gait["Right Average"]["FootOff"]
        if phase == "swing":
            startl = Gait["Left Average"]["FootOff"]
            endl = -1
            startr = Gait["Right Average"]["FootOff"]
            endr = -1
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
                if function=="max":
                    fun = max
                else:
                    fun = min
                c.execute(f"""UPDATE Gait_Max_Min_Table
                          SET 
                          {function}_Left_Knee_Angle_{axis}_{phase} = ?,
                          {function}_Left_Knee_Moment_{axis}_{phase} = ?,
                          {function}_Left_Knee_Force_{axis}_{phase} = ?,
                          {function}_Left_Knee_Power_{axis}_{phase} = ?,
                          {function}_Left_Hip_Angle_{axis}_{phase} = ?,
                          {function}_Left_Hip_Moment_{axis}_{phase} = ?,
                          {function}_Left_Hip_Force_{axis}_{phase} = ?,
                          {function}_Left_Hip_Power_{axis}_{phase} = ?,
                          {function}_Left_Ankle_Angle_{axis}_{phase} = ?,
                          {function}_Left_Ankle_Moment_{axis}_{phase} = ?,
                          {function}_Left_Ankle_Force_{axis}_{phase} = ?,
                          {function}_Left_Ankle_Power_{axis}_{phase} =  ?,
                          {function}_Left_Foot_Progression_Angle_{axis}_{phase} = ?,
                          {function}_Left_GRF_{axis}_{phase} =  ?,
                          {function}_Left_NGRF_{axis}_{phase} =  ?,
                          {function}_Left_pelvis_Angle_{axis}_{phase} =  ?,
                          {function}_Left_COM_{axis}_{phase} =  ?,
                          {function}_Right_Knee_Angle_{axis}_{phase} = ?,
                          {function}_Right_Knee_Moment_{axis}_{phase} = ?,
                          {function}_Right_Knee_Force_{axis}_{phase} = ?,
                          {function}_Right_Knee_Power_{axis}_{phase} = ?,
                          {function}_Right_Hip_Angle_{axis}_{phase} = ?,
                          {function}_Right_Hip_Moment_{axis}_{phase} = ?,
                          {function}_Right_Hip_Force_{axis}_{phase} = ?,
                          {function}_Right_Hip_Power_{axis}_{phase} = ?,
                          {function}_Right_Ankle_Angle_{axis}_{phase} = ?,
                          {function}_Right_Ankle_Moment_{axis}_{phase} = ?,
                          {function}_Right_Ankle_Force_{axis}_{phase} = ?,
                          {function}_Right_Ankle_Power_{axis}_{phase} =  ?,
                          {function}_Right_Foot_Progression_Angle_{axis}_{phase} = ?,
                          {function}_Right_GRF_{axis}_{phase} =  ?,
                          {function}_Right_NGRF_{axis}_{phase} =  ?,
                          {function}_Right_pelvis_Angle_{axis}_{phase} =  ?,
                          {function}_Right_COM_{axis}_{phase} =  ?
                          WHERE ID = ?
                          """,(
                          (fun((Gait["Left Average"]["KneeAngle"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["KneeMoment"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["KneeForce"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["KneePower"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["HipAngle"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["HipMoment"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["HipForce"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["HipPower"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["AnkleAngle"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["AnkleMoment"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["AnkleForce"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["AnklePower"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["FootProgressAngle"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["GRF"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["NGRF"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["pelvisAngle"][axis])[startl:endl])),
                          (fun((Gait["Left Average"]["COM"][axis])[startl:endl])),
                          (fun((Gait["Right Average"]["KneeAngle"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["KneeMoment"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["KneeForce"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["KneePower"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["HipAngle"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["HipMoment"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["HipForce"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["HipPower"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["AnkleAngle"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["AnkleMoment"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["AnkleForce"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["AnklePower"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["FootProgressAngle"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["GRF"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["NGRF"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["pelvisAngle"][axis])[startr:endr])),
                          (fun((Gait["Right Average"]["COM"][axis])[startr:endr])),
                          ID
                          ))

#create_Gait_Max_Min_Table()
#columns_Gait_Max_Min_Table()
enter_Gait_extrema()




def plot_tables():
    fig, axs = plt.subplots(4,3, sharex = True)
    x = np.array(range(100))
    #fig.subplots_adjust(wspace = 0.3, hspace = 0.4)
    fig.tight_layout()
    #axs.vlines(x=Gait["Left Average"]["FootOff"])
    
    axs[0,0].plot(x, Gait["Left Average"]["pelvisAngle"]["x"], "k", label = "mean")
    for Trials in cleanlefttrials:
        axs[0,0].plot(x, Gait[Trials]["Left"]["pelvisAngle"]["x"], label = str(Trials))
    #plt.ylabel("Angle (degree)")
    axs[0,0].set_title("Pelvic Tilt (x)", fontsize = 9)
    
    axs[0,1].plot(x, Gait["Left Average"]["pelvisAngle"]["y"], "k")
    for Trials in cleanlefttrials:
        axs[0,1].plot(x, Gait[Trials]["Left"]["pelvisAngle"]["y"])
    #plt.ylabel("Angle (degree)")
    axs[0,1].set_title("Pelvic Obliquity (y)", fontsize = 9)
    
    axs[0,2].plot(x, Gait["Left Average"]["pelvisAngle"]["z"], "k")
    for Trials in cleanlefttrials:
        axs[0,2].plot(x, Gait[Trials]["Left"]["pelvisAngle"]["z"])
    
    axs[0,2].set_title("Pelvic Rotation (z)", fontsize = 9)
    
    
    axs[1,0].plot(x, Gait["Left Average"]["HipAngle"]["x"], "k")
    for Trials in cleanlefttrials:
        axs[1,0].plot(x, Gait[Trials]["Left"]["HipAngle"]["x"])
    axs[1,0].set_title("Hip Flex/Extension (x)", fontsize = 9)
    
    
    axs[1,1].plot(x, Gait["Left Average"]["HipAngle"]["y"], "k")
    for Trials in cleanlefttrials:
        axs[1,1].plot(x, Gait[Trials]["Left"]["HipAngle"]["y"])
    axs[1,1].set_title("Hip Ab/Adduction (y)", fontsize = 9)
    
    axs[1,2].plot(x, Gait["Left Average"]["HipAngle"]["z"], "k")
    for Trials in cleanlefttrials:
        axs[1,2].plot(x, Gait[Trials]["Left"]["HipAngle"]["z"])
    axs[1,2].set_title("Hip Rotation (z)", fontsize = 9)
    
    
    
    axs[2,0].plot(x, Gait["Left Average"]["KneeAngle"]["x"], "k")
    for Trials in cleanlefttrials:
        axs[2,0].plot(x, Gait[Trials]["Left"]["KneeAngle"]["x"])
    axs[2,0].set_title("Knee Flex/Extension (x)", fontsize = 9)
    
    axs[2,1].plot(x, Gait["Left Average"]["KneeAngle"]["y"], "k")
    for Trials in cleanlefttrials:
        axs[2,1].plot(x, Gait[Trials]["Left"]["KneeAngle"]["y"])
    axs[2,1].set_title("Knee Valgus/Varus (y)", fontsize = 9)
    
    axs[2,2].plot(x, Gait["Left Average"]["KneeAngle"]["z"], "k")
    for Trials in cleanlefttrials:
        axs[2,2].plot(x, Gait[Trials]["Left"]["KneeAngle"]["z"])
    axs[2,2].set_title("Knee Rotation (z)", fontsize = 9)
    
    
    
    axs[3,0].plot(x, Gait["Left Average"]["AnkleAngle"]["x"], "k")
    for Trials in cleanlefttrials:
        axs[3,0].plot(x, Gait[Trials]["Left"]["AnkleAngle"]["x"])
    axs[3,0].set_title("Foot Dorsi/Plantar (x)", fontsize = 9)
    
    axs[3,1].plot(x, Gait["Left Average"]["AnkleAngle"]["y"], "k")
    for Trials in cleanlefttrials:
        axs[3,1].plot(x, Gait[Trials]["Left"]["AnkleAngle"]["y"])
    axs[3,1].set_title("Foot Eversion/Inversion (y)", fontsize = 9)
    
    axs[3,2].plot(x, Gait["Left Average"]["AnkleAngle"]["z"], "k")
    for Trials in cleanlefttrials:
        axs[3,2].plot(x, Gait[Trials]["Left"]["AnkleAngle"]["z"])
    axs[3,2].set_title("Foot Rotation (z)", fontsize = 9)
    
    
    plt.xlabel("Percent of Gait Cycle")
    
    plt.show() 
plot_tables()

def select_columns():
    c.execute("SELECT sql FROM sqlite_master WHERE name='Gait_Max_Min_Table'")
    rows = c.fetchall()
    for row in rows:
        print(row)
##select_columns()

def select_all():
    c.execute("SELECT * FROM 'Mean_Gait_Table'")
    rows = c.fetchall()
    for row in rows:
        print(row)
select_all()


"""Close SQLite Connection"""
conn.commit()
conn.close()     
