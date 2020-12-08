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
from tkinter import ttk
import tkinter.font as font

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

"""TAB 1"""
FrameTop = Frame(tab1, bg = "DodgerBlue3", bd = 6)
FrameTop.pack(expand = 1, fill = BOTH, side = TOP)
FrameInfo = Frame(FrameTop, bg = "DodgerBlue3", bd = 6)
FrameInfo.pack( side = LEFT,fill = BOTH, anchor = NW)
FrameMovement = Frame(FrameTop, bg = "DodgerBlue2", bd = 6)
FrameMovement.pack( side = RIGHT, anchor = NE)
FrameClose = Frame(tab1, bg = "DeepSkyBlue2")
FrameClose.pack(expand = 1, fill = BOTH, side = BOTTOM, anchor = SE)

def close_window():
    root.destroy()


#FRAME 1: INPuT PATIENT DATA
labelID = Label(FrameInfo,  text = "Patient ID: ", bg = "ivory3") 
labelID.grid(column = 1, row = 1, pady = 5)
vID = StringVar()
entryID = Entry(FrameInfo,  textvariable = vID,   fg = "purple4", width = 20) 
entryID.grid(column = 2, row = 1, columnspan = 3)
labelSex = Label(FrameInfo,  text = "Sex: ", bg = "ivory3") 
labelSex.grid(column = 1, row = 2, pady = 5)
vSex = StringVar()
vSex.set(0)
radiomale = Radiobutton(FrameInfo, text="Male",variable= vSex, value="Male")
radiomale.grid(column = 2, row = 2)
radiofemale = Radiobutton(FrameInfo, text="Female",variable= vSex, value="Female")
radiofemale.grid(column = 3, row = 2)
labelDom = Label(FrameInfo,  text = "Dominant Limb: ", bg = "ivory3") 
labelDom.grid(column = 1, row = 3, pady = 5)
vDom = StringVar()
vDom.set(0)
radioleftdom = Radiobutton(FrameInfo, text="Left",variable= vDom, value="Left")
radioleftdom.grid(column = 2, row = 3)
radiorightdom = Radiobutton(FrameInfo, text="Right",variable =vDom, value="Right")
radiorightdom.grid(column = 3, row = 3)
radiorightdom = Radiobutton(FrameInfo, text="N/A",variable =vDom, value="N/A")
radiorightdom.grid(column = 4, row = 3)
class Pattype:
    def disable(self, master):
        if vType.get() == "Post-op":
            self.month_entry.configure(state = "normal")
            self.date_label.configure(state = "normal")
            self.limb_label.configure(state = "normal")
            self.radioleft.configure(state = "normal")
            self.radioright.configure(state = "normal")
            self.radioboth.configure(state = "normal")
        if vType.get() == "Control":
            self.month_entry.configure(state = "disabled")
            self.date_label.configure(state = "disabled")
            self.limb_label.configure(state = "disabled")
            self.radioleft.configure(state = "disabled")
            self.radioright.configure(state = "disabled")
            self.radioboth.configure(state = "disabled")
        if vType.get() == "Pre-op":
            self.month_entry.configure(state = "disabled")
            self.date_label.configure(state = "disabled")    
            self.limb_label.configure(state = "normal")
            self.radioleft.configure(state = "normal")
            self.radioright.configure(state = "normal")
            self.radioboth.configure(state = "normal")
           
    def __init__(self, master):
        self.label_type = Label(FrameInfo, text = "Patient Type: ", bg = "ivory3")
        self.label_type.grid(column = 1, row = 4, pady = 5)
        global vType
        vType = StringVar()
        self.optiontype = OptionMenu(FrameInfo, vType, "Pre-op", "Post-op", "Control", 
                                      command = self.disable)
        self.optiontype.config(width = 20)
        self.optiontype.grid(column = 2, row = 4, columnspan  =3)
        
        self.date_label = Label(FrameInfo, text = "Number of months Post - Op: ", bg = "ivory3")
        self.date_label.grid(column = 1, row  = 5, pady = 5)
        global vMonth
        vMonth = IntVar() 
        self.month_entry = Entry(FrameInfo, textvariable = vMonth, width = 20, fg = "purple4")
        self.month_entry.grid(column = 2, row = 5, columnspan  = 3)
        self.limb_label = Label(FrameInfo, text = "Affected Limb: ", bg = "ivory3")
        self.limb_label.grid(column = 1, row  = 6, pady = 5)
        global vAffect
        vAffect = StringVar()
        vAffect.set(0)
        self.radioleft = Radiobutton(FrameInfo, text="Left",variable= vAffect, value="Left")
        self.radioleft.grid(column = 2, row = 6)
        self.radioright = Radiobutton(FrameInfo, text="Right",variable=vAffect, value="Right")
        self.radioright.grid(column = 3, row = 6)
        self.radioboth = Radiobutton(FrameInfo, text="Both",variable=vAffect, value="Both")
        self.radioboth.grid(column = 4, row = 6)             
Pattype(FrameInfo)

#FRAME 2: CHECKBOXES
gc = IntVar()
Gaitlabel = Label(FrameMovement, text = "Gait")
Gaitlabel.grid(column = 10, row  = 2, padx = 5, pady = 7)
Gaitcheck = Checkbutton(FrameMovement, variable = gc)
Gaitcheck.grid(column  = 11, row  = 2)

suc = IntVar()
StepUplabel = Label(FrameMovement, text = "StepUp")
StepUplabel.grid(column = 10, row  = 3,padx = 5, pady = 7)
StepUpcheck = Checkbutton(FrameMovement, variable = suc)
StepUpcheck.grid(column  = 11, row  = 3)

sdc = IntVar()
StepDownlabel = Label(FrameMovement, text = "StepDown")
StepDownlabel.grid(column = 10, row  = 4, padx = 5,pady = 7)
StepDowncheck = Checkbutton(FrameMovement, variable = sdc)
StepDowncheck.grid(column  = 11, row  = 4)

stsc = IntVar()
SitStandSitlabel = Label(FrameMovement, text = "SitStandSit")
SitStandSitlabel.grid(column = 10, row  = 5, padx = 5,pady = 7)
SitStandSitcheck = Checkbutton(FrameMovement, variable = stsc)
SitStandSitcheck.grid(column  = 11, row  = 5)


#FRAME 3: CANCEL/ACCEPT
buttoncancel = Button(FrameClose, text = "Cancel", command = lambda: close_window())
buttoncancel.pack(side = RIGHT, anchor = CENTER, padx = 10)
buttonaccept = Button(FrameClose, text = "Accept", command = lambda: [close_window()])
buttonaccept.pack(side = RIGHT, anchor = CENTER, padx = 10, pady = 20)



"""Tab 2: Gait"""
InfoFrameGait = Frame(tab2,bg = "DodgerBlue3", bd = 6)
InfoFrameGait.pack(fill = BOTH)
SelectFrameGait = Frame(tab2,bg = "DodgerBlue3", bd = 6)
SelectFrameGait.pack(fill = BOTH)
TrialFrameGait= Frame(tab2,bg = "DodgerBlue3")
TrialFrameGait.pack(fill = BOTH)

labelGait = Label(InfoFrameGait, text = "Gait")
labelGait["font"] = myFont
labelGait.pack()

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

#SELECT TRIALS GAIT

Gait = {}
# TriallistGait=[]
# filelistGait=[]
def browseFilesGait(): 
    #TriallistGait.clear()
    gc.set(1)
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

#EXCTRACT AND NORMALISE DATA
def cutcycle(footstrike, data):
    footstrike1 = footstrike[0]
    footstrike2 = footstrike[1]
    data1 = (data[footstrike1:footstrike2])
    return data1
    
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
    for LR in ['Right','Left']:
        for key in Gait[TrialNum][LR].keys():
            arr = Gait[TrialNum][LR][key]
            Gait[TrialNum][LR][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }

def extract_all_Gait_files():
    for i in range(len(TriallistGait)):
        extractintoDict(filelistGait[i], TriallistGait[i])
        
button_exploreGait = Button(SelectFrameGait, text = "Select up to 6 Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesGait(), extract_all_Gait_files()])  
button_exploreGait.pack(pady=10)
 

"""Tab 3: Stepup"""

InfoFrameStepUp = Frame(tab3,bg = "DodgerBlue3", bd = 6)
InfoFrameStepUp.grid(column = 1, row = 2, columnspan = 2, sticky = NSEW)
TrialFrameStepUp= Frame(tab3,bg = "DodgerBlue3")
TrialFrameStepUp.grid(column = 1, row = 3, columnspan = 2, sticky = NSEW)

FrameStepUpLeft = Frame(TrialFrameStepUp, bg = "DeepSkyBlue2")
FrameStepUpLeft.pack(side = LEFT, expand =True, fill = BOTH)
FrameStepUpRight = Frame(TrialFrameStepUp, bg = "DeepSkyBlue2")
FrameStepUpRight.pack(side = RIGHT, expand =True, fill = BOTH)

InfoFrameSteppingUp = Frame(tab3,bg = "DodgerBlue3", bd = 6)
InfoFrameSteppingUp.grid(column = 1, row = 4, columnspan = 2, sticky = NSEW)
FrameMainSteppingUp= Frame(tab3,bg = "DodgerBlue3")
FrameMainSteppingUp.grid(column = 1, row = 6, columnspan = 2)


SelectFrameSteppingUp = Frame(FrameMainSteppingUp, bg = "DodgerBlue3", bd = 6)
SelectFrameSteppingUp.grid(column =1, row = 1, columnspan = 2)
FrameTrial1SteppingUp = Frame(FrameMainSteppingUp, bg = "ivory3", bd = 6)
FrameTrial1SteppingUp.grid (column =  1, row  =2)
FrameTrial2SteppingUp = Frame(FrameMainSteppingUp, bg = "ghost white", bd = 6)
FrameTrial2SteppingUp.grid (column =  1, row  =3)
FrameTrial3SteppingUp = Frame(FrameMainSteppingUp, bg = "ivory3", bd = 6)
FrameTrial3SteppingUp.grid (column =  1, row  =4)
FrameTrial4SteppingUp = Frame(FrameMainSteppingUp, bg = "ghost white", bd = 6)
FrameTrial4SteppingUp.grid (column =  2, row  =2)
FrameTrial5SteppingUp = Frame(FrameMainSteppingUp, bg = "ivory3", bd = 6)
FrameTrial5SteppingUp.grid (column =  2, row  =3)
FrameTrial6SteppingUp = Frame(FrameMainSteppingUp, bg = "ghost white", bd = 6)
FrameTrial6SteppingUp.grid (column =  2, row  =4)
Framebottom2 = Frame(FrameMainSteppingUp, bg = "DodgerBlue3", bd = 6)
Framebottom2.grid(row  =5, column = 1, columnspan = 2)
labelbottom2 = Label(Framebottom2, height = 1,  bg = "DodgerBlue3")
labelbottom2.pack()

labelStepUp = Label(InfoFrameStepUp, text = "StepUp")
labelStepUp["font"] = myFont
labelStepUp.pack()

#Display filenames + whether clean or not    
SelectFrameStepUpLeft = Frame(FrameStepUpLeft, bg = "DodgerBlue3", bd = 6)
SelectFrameStepUpLeft.pack(expand =True, fill = BOTH)
FrameTrial1StepUp = Frame(FrameStepUpLeft, bg = "ivory3", bd = 6)
FrameTrial1StepUp.pack()
FrameTrial2StepUp = Frame(FrameStepUpLeft, bg = "ghost white", bd = 6)
FrameTrial2StepUp.pack()
FrameTrial3StepUp = Frame(FrameStepUpLeft, bg = "ivory3", bd = 6)
FrameTrial3StepUp.pack()


SelectFrameStepUpRight = Frame(FrameStepUpRight, bg = "DodgerBlue3", bd = 6)
SelectFrameStepUpRight.pack(expand =True, fill = BOTH)
FrameTrial4StepUp = Frame(FrameStepUpRight, bg = "ghost white", bd = 6)
FrameTrial4StepUp.pack()
FrameTrial5StepUp = Frame(FrameStepUpRight, bg = "ivory3", bd = 6)
FrameTrial5StepUp.pack()
FrameTrial6StepUp = Frame(FrameStepUpRight, bg = "ghost white", bd = 6)
FrameTrial6StepUp.pack()

label_file_explorer1StepUp = Label(FrameTrial1StepUp,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer2StepUp = Label(FrameTrial2StepUp,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer2StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer3StepUp = Label(FrameTrial3StepUp,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer3StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer4StepUp = Label(FrameTrial4StepUp,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer4StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer5StepUp = Label(FrameTrial5StepUp,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer5StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer6StepUp = Label(FrameTrial6StepUp,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer6StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

"""STRAHTCLYDE STYLE STEPPING"""

labelSteppingUp = Label(InfoFrameSteppingUp, text = "OR Select Strathclyde Stepping Trials")
labelSteppingUp.pack()

label_file_explorer1SteppingUp = Label(FrameTrial1SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1SteppingUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
VUp1 = StringVar()
VUp1.set(0)
radioleft1 = Radiobutton(FrameTrial1SteppingUp, text="Left",variable= VUp1, value="Left")
radioleft1.grid(column = 2, row = 1)
radioright1 = Radiobutton(FrameTrial1SteppingUp, text="Right",variable =VUp1, value="Right")
radioright1.grid(column = 3, row = 1)
radioboth1= Radiobutton(FrameTrial1SteppingUp, text="Both",variable =VUp1, value="Noth")
radioboth1.grid(column = 4, row = 1)

label_file_explorer2SteppingUp = Label(FrameTrial2SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer2SteppingUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
VUp2 = StringVar()
VUp2.set(0)
radioleft2 = Radiobutton(FrameTrial2SteppingUp, text="Left",variable= VUp2, value="Left")
radioleft2.grid(column = 2, row = 1)
radioright2 = Radiobutton(FrameTrial2SteppingUp, text="Right",variable =VUp2, value="Right")
radioright2.grid(column = 3, row = 1)
radioboth2= Radiobutton(FrameTrial2SteppingUp, text="Both",variable =VUp2, value="Noth")
radioboth2.grid(column = 4, row = 1)

label_file_explorer3SteppingUp = Label(FrameTrial3SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer3SteppingUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
VUp3 = StringVar()
VUp3.set(0)
radioleft3 = Radiobutton(FrameTrial3SteppingUp, text="Left",variable= VUp3, value="Left")
radioleft3.grid(column = 2, row = 1)
radioright3 = Radiobutton(FrameTrial3SteppingUp, text="Right",variable =VUp3, value="Right")
radioright3.grid(column = 3, row = 1)
radioboth3= Radiobutton(FrameTrial3SteppingUp, text="Both",variable =VUp3, value="Noth")
radioboth3.grid(column = 4, row = 1)

label_file_explorer4SteppingUp = Label(FrameTrial4SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer4SteppingUp.grid(column = 5, row = 1, columnspan = 1, rowspan = 2) 
VUp4 = StringVar()
VUp4.set(0)
radioleft4 = Radiobutton(FrameTrial4SteppingUp, text="Left",variable= VUp4, value="Left")
radioleft4.grid(column = 6, row = 1)
radioright4 = Radiobutton(FrameTrial4SteppingUp, text="Right",variable =VUp4, value="Right")
radioright4.grid(column = 7, row = 1)
radioboth4= Radiobutton(FrameTrial4SteppingUp, text="Both",variable =VUp4, value="Noth")
radioboth4.grid(column = 8, row = 1)

label_file_explorer5SteppingUp = Label(FrameTrial5SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer5SteppingUp.grid(column = 5, row = 1, columnspan = 1, rowspan = 2) 
VUp5 = StringVar()
VUp5.set(0)
radioleft5 = Radiobutton(FrameTrial5SteppingUp, text="Left",variable= VUp5, value="Left")
radioleft5.grid(column = 6, row = 1)
radioright5 = Radiobutton(FrameTrial5SteppingUp, text="Right",variable =VUp5, value="Right")
radioright5.grid(column = 7, row = 1)
radioboth5= Radiobutton(FrameTrial5SteppingUp, text="Both",variable =VUp5, value="Noth")
radioboth5.grid(column = 8, row = 1)

label_file_explorer6SteppingUp = Label(FrameTrial6SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer6SteppingUp.grid(column = 5, row = 1, columnspan = 1, rowspan = 2) 
VUp6 = StringVar()
VUp6.set(0)
radioleft6 = Radiobutton(FrameTrial6SteppingUp, text="Left",variable= VUp6, value="Left")
radioleft6.grid(column = 6, row = 1)
radioright6 = Radiobutton(FrameTrial6SteppingUp, text="Right",variable =VUp6, value="Right")
radioright6.grid(column = 7, row = 1)
radioboth6= Radiobutton(FrameTrial6SteppingUp, text="Both",variable =VUp6, value="Noth")
radioboth6.grid(column = 8, row = 1)


StepUp= {}
StepUp["Left"] = {}
StepUp["Right"] = {}
def browseFilesStepUp(Limb): 
    #TriallistStepUp.clear()
    sdc.set(1)
    global TriallistStepUp
    global filelistStepUp
    TriallistStepUp = []
    filelistStepUp = []

    filenames = (filedialog.askopenfilenames(
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                      ("all files", "*.*"))))
    #creates a tuple therefore must tur into a list
    filelistStepUp = list(filenames)
    length = len(filelistStepUp)
    print(filelistStepUp)
    print (length)
    for i in range(length):
        filelistStepUp[i]=os.path.basename(filelistStepUp[i])
        if Limb == "Left":
            TriallistStepUp.append("Trial "+str(i+1))
            StepUp["Left"][TriallistStepUp[i]]={}
            if i == 0:
                label_file_explorer1StepUp.configure(text="File Opened: "+filelistStepUp[i])
            if i == 1:
                label_file_explorer2StepUp.configure(text="File Opened: "+filelistStepUp[i])
            if i == 2:
                label_file_explorer3StepUp.configure(text="File Opened: "+filelistStepUp[i])

            global filelistStepUpLeft
            filelistStepUpLeft = filelistStepUp
        if Limb == "Right":
            TriallistStepUp.append("Trial "+str(i+1))
            StepUp["Right"][TriallistStepUp[i]]={}
            if i == 0:
                label_file_explorer4StepUp.configure(text="File Opened: "+filelistStepUp[i])
            if i == 1:
                label_file_explorer5StepUp.configure(text="File Opened: "+filelistStepUp[i])
            if i == 2:
                label_file_explorer6StepUp.configure(text="File Opened: "+filelistStepUp[i])
            
            global filelistStepUpRight
            filelistStepUpRight = filelistStepUp
    print(filelistStepUp)
    print(length)
    print(TriallistStepUp)

    
def extractintoDictStepUp(filename, TrialNum, Limb):     
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
    if Limb == "Left":
        StepUp["Left"].update({TrialNum:extractvalues(trialacq)})
        for key in StepUp["Left"][TrialNum].keys():
            arr = StepUp["Left"][TrialNum][key]
            StepUp["Left"][TrialNum][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
        StepUp["Left"][TrialNum].update({"Filename": filename})
        
    if Limb== "Right":
        StepUp["Right"].update({TrialNum:extractvalues(trialacq)})
        for key in StepUp["Right"][TrialNum].keys():
            arr = StepUp["Right"][TrialNum][key]
            StepUp["Right"][TrialNum][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
        StepUp["Right"][TrialNum].update({"Filename": filename})

def extract_all_StepUp_files(Limb):
    for i in range(len(TriallistStepUp)):
        extractintoDictStepUp(filelistStepUp[i], TriallistStepUp[i], Limb)

button_exploreStepUpLeft = Button(SelectFrameStepUpLeft, text = "Select up to 3 LEFT Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesStepUp("Left"), extract_all_StepUp_files("Left")])  
button_exploreStepUpLeft.pack(pady=10)
button_exploreStepUpRight = Button(SelectFrameStepUpRight, text = "Select up to 3 RIGHT Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesStepUp("Right"),extract_all_StepUp_files("Right")])  
button_exploreStepUpRight.pack(pady=10)

button_exploreSteppingUp = Button(SelectFrameSteppingUp, text = "Select up to 6 Trials",  width = 40, bg = "ghost white",
                          command = lambda : [])  
button_exploreSteppingUp.pack(pady=10)

"""Tab 4: StepDown"""

InfoFrameStepDown = Frame(tab4,bg = "DodgerBlue3", bd = 6)
InfoFrameStepDown.grid(column = 1, row = 2, columnspan = 2, sticky = NSEW)
TrialFrameStepDown= Frame(tab4,bg = "DodgerBlue3")
TrialFrameStepDown.grid(column = 1, row = 3, columnspan = 2, sticky = NSEW)

FrameStepDownLeft = Frame(TrialFrameStepDown, bg = "DeepSkyBlue2")
FrameStepDownLeft.pack(side = LEFT, expand =True, fill = BOTH)
FrameStepDownRight = Frame(TrialFrameStepDown, bg = "DeepSkyBlue2")
FrameStepDownRight.pack(side = RIGHT, expand =True, fill = BOTH)

InfoFrameSteppingDown = Frame(tab4,bg = "DodgerBlue3", bd = 6)
InfoFrameSteppingDown.grid(column = 1, row = 4, columnspan = 2, sticky = NSEW)
FrameMainSteppingDown= Frame(tab4,bg = "DodgerBlue3")
FrameMainSteppingDown.grid(column = 1, row = 6, columnspan = 2)


SelectFrameSteppingDown = Frame(FrameMainSteppingDown, bg = "DodgerBlue3", bd = 6)
SelectFrameSteppingDown.grid(column =1, row = 1, columnspan = 2)
FrameTrial1SteppingDown = Frame(FrameMainSteppingDown, bg = "ivory3", bd = 6)
FrameTrial1SteppingDown.grid (column =  1, row  =2)
FrameTrial2SteppingDown = Frame(FrameMainSteppingDown, bg = "ghost white", bd = 6)
FrameTrial2SteppingDown.grid (column =  1, row  =3)
FrameTrial3SteppingDown = Frame(FrameMainSteppingDown, bg = "ivory3", bd = 6)
FrameTrial3SteppingDown.grid (column =  1, row  =4)
FrameTrial4SteppingDown = Frame(FrameMainSteppingDown, bg = "ghost white", bd = 6)
FrameTrial4SteppingDown.grid (column =  2, row  =2)
FrameTrial5SteppingDown = Frame(FrameMainSteppingDown, bg = "ivory3", bd = 6)
FrameTrial5SteppingDown.grid (column =  2, row  =3)
FrameTrial6SteppingDown = Frame(FrameMainSteppingDown, bg = "ghost white", bd = 6)
FrameTrial6SteppingDown.grid (column =  2, row  =4)
Framebottom3 = Frame(FrameMainSteppingDown, bg = "DodgerBlue3", bd = 6)
Framebottom3.grid(row  =5, column = 1, columnspan = 2)
labelbottom3 = Label(Framebottom3, height = 1,  bg = "DodgerBlue3")
labelbottom3.pack()


labelStepDown = Label(InfoFrameStepDown, text = "StepDown")
labelStepDown["font"] = myFont
labelStepDown.pack()

#Display filenames + whether clean or not    
SelectFrameStepDownLeft = Frame(FrameStepDownLeft, bg = "DodgerBlue3", bd = 6)
SelectFrameStepDownLeft.pack(expand =True, fill = BOTH)
FrameTrial1StepDown = Frame(FrameStepDownLeft, bg = "ivory3", bd = 6)
FrameTrial1StepDown.pack()
FrameTrial2StepDown = Frame(FrameStepDownLeft, bg = "ghost white", bd = 6)
FrameTrial2StepDown.pack()
FrameTrial3StepDown = Frame(FrameStepDownLeft, bg = "ivory3", bd = 6)
FrameTrial3StepDown.pack()


SelectFrameStepDownRight = Frame(FrameStepDownRight, bg = "DodgerBlue3", bd = 6)
SelectFrameStepDownRight.pack(expand =True, fill = BOTH)
FrameTrial4StepDown = Frame(FrameStepDownRight, bg = "ghost white", bd = 6)
FrameTrial4StepDown.pack()
FrameTrial5StepDown = Frame(FrameStepDownRight, bg = "ivory3", bd = 6)
FrameTrial5StepDown.pack()
FrameTrial6StepDown = Frame(FrameStepDownRight, bg = "ghost white", bd = 6)
FrameTrial6StepDown.pack()

label_file_explorer1StepDown = Label(FrameTrial1StepDown,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer2StepDown = Label(FrameTrial2StepDown,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer2StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer3StepDown = Label(FrameTrial3StepDown,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer3StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer4StepDown = Label(FrameTrial4StepDown,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer4StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer5StepDown = Label(FrameTrial5StepDown,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer5StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer6StepDown = Label(FrameTrial6StepDown,  text = "", width = 60, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer6StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

"""STRAHTCLYDE STYLE STEPPING"""

labelSteppingDown = Label(InfoFrameSteppingDown, text = "OR Select Strathclyde Stepping Trials")
labelSteppingDown.pack()

label_file_explorer1SteppingDown = Label(FrameTrial1SteppingDown,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1SteppingDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vDown1 = StringVar()
vDown1.set(0)
radioleft1 = Radiobutton(FrameTrial1SteppingDown, text="Left",variable= vDown1, value="Left")
radioleft1.grid(column = 2, row = 1)
radioright1 = Radiobutton(FrameTrial1SteppingDown, text="Right",variable =vDown1, value="Right")
radioright1.grid(column = 3, row = 1)
radioboth1= Radiobutton(FrameTrial1SteppingDown, text="Both",variable =vDown1, value="Noth")
radioboth1.grid(column = 4, row = 1)

label_file_explorer2SteppingDown = Label(FrameTrial2SteppingDown,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer2SteppingDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vDown2 = StringVar()
vDown2.set(0)
radioleft2 = Radiobutton(FrameTrial2SteppingDown, text="Left",variable= vDown2, value="Left")
radioleft2.grid(column = 2, row = 1)
radioright2 = Radiobutton(FrameTrial2SteppingDown, text="Right",variable =vDown2, value="Right")
radioright2.grid(column = 3, row = 1)
radioboth2= Radiobutton(FrameTrial2SteppingDown, text="Both",variable =vDown2, value="Noth")
radioboth2.grid(column = 4, row = 1)

label_file_explorer3SteppingDown = Label(FrameTrial3SteppingDown,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer3SteppingDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vDown3 = StringVar()
vDown3.set(0)
radioleft3 = Radiobutton(FrameTrial3SteppingDown, text="Left",variable= vDown3, value="Left")
radioleft3.grid(column = 2, row = 1)
radioright3 = Radiobutton(FrameTrial3SteppingDown, text="Right",variable =vDown3, value="Right")
radioright3.grid(column = 3, row = 1)
radioboth3= Radiobutton(FrameTrial3SteppingDown, text="Both",variable =vDown3, value="Noth")
radioboth3.grid(column = 4, row = 1)

label_file_explorer4SteppingDown = Label(FrameTrial4SteppingDown,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer4SteppingDown.grid(column = 5, row = 1, columnspan = 1, rowspan = 2) 
vDown4 = StringVar()
vDown4.set(0)
radioleft4 = Radiobutton(FrameTrial4SteppingDown, text="Left",variable= vDown4, value="Left")
radioleft4.grid(column = 6, row = 1)
radioright4 = Radiobutton(FrameTrial4SteppingDown, text="Right",variable =vDown4, value="Right")
radioright4.grid(column = 7, row = 1)
radioboth4= Radiobutton(FrameTrial4SteppingDown, text="Both",variable =vDown4, value="Noth")
radioboth4.grid(column = 8, row = 1)

label_file_explorer5SteppingDown = Label(FrameTrial5SteppingDown,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer5SteppingDown.grid(column = 5, row = 1, columnspan = 1, rowspan = 2) 
vDown5 = StringVar()
vDown5.set(0)
radioleft5 = Radiobutton(FrameTrial5SteppingDown, text="Left",variable= vDown5, value="Left")
radioleft5.grid(column = 6, row = 1)
radioright5 = Radiobutton(FrameTrial5SteppingDown, text="Right",variable =vDown5, value="Right")
radioright5.grid(column = 7, row = 1)
radioboth5= Radiobutton(FrameTrial5SteppingDown, text="Both",variable =vDown5, value="Noth")
radioboth5.grid(column = 8, row = 1)

label_file_explorer6SteppingDown = Label(FrameTrial6SteppingDown,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer6SteppingDown.grid(column = 5, row = 1, columnspan = 1, rowspan = 2) 
vDown6 = StringVar()
vDown6.set(0)
radioleft6 = Radiobutton(FrameTrial6SteppingDown, text="Left",variable= vDown6, value="Left")
radioleft6.grid(column = 6, row = 1)
radioright6 = Radiobutton(FrameTrial6SteppingDown, text="Right",variable =vDown6, value="Right")
radioright6.grid(column = 7, row = 1)
radioboth6= Radiobutton(FrameTrial6SteppingDown, text="Both",variable =vDown6, value="Noth")
radioboth6.grid(column = 8, row = 1)


StepDown= {}
StepDown["Left"] = {}
StepDown["Right"] = {}
def browseFilesStepDown(Limb): 
    #TriallistStepDown.clear()
    sdc.set(1)
    global TriallistStepDown
    global filelistStepDown
    TriallistStepDown = []
    filelistStepDown = []

    filenames = (filedialog.askopenfilenames(
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                      ("all files", "*.*"))))
    #creates a tuple therefore must tur into a list
    filelistStepDown = list(filenames)
    length = len(filelistStepDown)
    print(filelistStepDown)
    print (length)
    for i in range(length):
        filelistStepDown[i]=os.path.basename(filelistStepDown[i])
        if Limb == "Left":
            TriallistStepDown.append("Trial "+str(i+1))
            StepDown["Left"][TriallistStepDown[i]]={}
            if i == 0:
                label_file_explorer1StepDown.configure(text="File Opened: "+filelistStepDown[i])
            if i == 1:
                label_file_explorer2StepDown.configure(text="File Opened: "+filelistStepDown[i])
            if i == 2:
                label_file_explorer3StepDown.configure(text="File Opened: "+filelistStepDown[i])

            global filelistStepDownLeft
            filelistStepDownLeft = filelistStepDown
        if Limb == "Right":
            TriallistStepDown.append("Trial "+str(i+1))
            StepDown["Right"][TriallistStepDown[i]]={}
            if i == 0:
                label_file_explorer4StepDown.configure(text="File Opened: "+filelistStepDown[i])
            if i == 1:
                label_file_explorer5StepDown.configure(text="File Opened: "+filelistStepDown[i])
            if i == 2:
                label_file_explorer6StepDown.configure(text="File Opened: "+filelistStepDown[i])
            
            global filelistStepDownRight
            filelistStepDownRight = filelistStepDown
    print(filelistStepDown)
    print(length)
    print(TriallistStepDown)

    
def extractintoDictStepDown(filename, TrialNum, Limb):     
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
    if Limb == "Left":
        StepDown["Left"].update({TrialNum:extractvalues(trialacq)})
        for key in StepDown["Left"][TrialNum].keys():
            arr = StepDown["Left"][TrialNum][key]
            StepDown["Left"][TrialNum][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
        StepDown["Left"][TrialNum].update({"Filename": filename})
        
    if Limb== "Right":
        StepDown["Right"].update({TrialNum:extractvalues(trialacq)})
        for key in StepDown["Right"][TrialNum].keys():
            arr = StepDown["Right"][TrialNum][key]
            StepDown["Right"][TrialNum][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }
        StepDown["Right"][TrialNum].update({"Filename": filename})

def extract_all_StepDown_files(Limb):
    for i in range(len(TriallistStepDown)):
        extractintoDictStepDown(filelistStepDown[i], TriallistStepDown[i], Limb)

button_exploreStepDownLeft = Button(SelectFrameStepDownLeft, text = "Select up to 3 LEFT Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesStepDown("Left"), extract_all_StepDown_files("Left")])  
button_exploreStepDownLeft.pack(pady=10)
button_exploreStepDownRight = Button(SelectFrameStepDownRight, text = "Select up to 3 RIGHT Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesStepDown("Right"),extract_all_StepDown_files("Right")])  
button_exploreStepDownRight.pack(pady=10)

button_exploreSteppingDown = Button(SelectFrameSteppingDown, text = "Select up to 6 Trials",  width = 40, bg = "ghost white",
                          command = lambda : [])  
button_exploreSteppingDown.pack(pady=10)
#, extract_all_StepUp_files()





















root.mainloop()

ID = vID.get()
Type = vType.get()
Month = str(vMonth.get()) + " Month(s)"

patient = {}
patient["ID"] = vID.get()
patient["Sex"]= vSex.get()
patient["Dominant Limb"] = vDom.get()
patient["Affected Limb"] = vAffect.get()
patient["Type"] = Type
patient[Type]= {}

# patient["Type"] = vType.get()
if Type == "Post-op":
    patient[Type][Month]={}
    patient[Type][Month].update({"Month Post-op": vMonth.get()})
    patient[Type][Month].update({"Gait":Gait})
    patient[Type][Month].update({"StepUp":StepUp})
    patient[Type][Month].update({"StepDown":StepDown})
else:
    patient[Type].update({"Gait":Gait})
    patient[Type].update({"StepUp":StepUp})
    patient[Type].update({"StepDown":StepDown})


def writetodict():
    name = ID + Type + str(vMonth.get()) + ".json"
    with open(name, 'w') as f:
        json.dump(patient, f, indent = 5)    
writetodict()


