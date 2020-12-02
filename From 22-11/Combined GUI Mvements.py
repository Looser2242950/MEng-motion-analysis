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


root = Tk()

#SetUp Tabs
tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)
tab4 = ttk.Frame(tab_parent)
tab5 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text = "Patient Data")
tab_parent.add(tab2, text = "Gait")
tab_parent.add(tab3, text = "Step Up")
tab_parent.add(tab4, text = "Step Down")
tab_parent.add(tab5, text = "Sit Stand Sit")
tab_parent.pack(expand=1, fill="both")



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
radioother = Radiobutton(FrameInfo, text="Other",variable= vSex, value="Other")
radioother.grid(column = 4, row = 2)
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
        Gait[TrialNum]["Left"]["GRF"] =cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["GRF"])
        Gait[TrialNum]["Left"]["NGRF"] =cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"]["NGRF"])
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
        Gait[TrialNum]["Right"]["GRF"] =cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["GRF"])
        Gait[TrialNum]["Right"]["NGRF"] =cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"]["NGRF"])
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
button_exploreGait.pack(pady=20)
 

"""Tab 3: Stepup"""

InfoFrameStepUp = Frame(tab3,bg = "DodgerBlue3", bd = 6)
InfoFrameStepUp.grid(column = 1, row = 2)
TrialFrameMainStepUp= Frame(tab3,bg = "DodgerBlue3")
TrialFrameMainStepUp.grid(column = 1, row = 3, columnspan = 2)

# mycanvas = Canvas(TrialFrameMainStepUp, bg = "DodgerBlue3")
# mycanvas.pack(side = LEFT, fill = BOTH, expand =True)
# scroll_y = Scrollbar(TrialFrameMainStepUp, orient = "vertical", command = mycanvas.yview)
# scroll_y.pack(side = RIGHT, fill = BOTH)
# # mycanvas.configure(width = 300, height = 500)
# mycanvas.configure(yscrollcommand = scroll_y.set)
# mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox("all")) )

# TrialFrameStepUp = Frame(mycanvas, bg = "red")
# TrialFrameStepUp.pack(expand =True, fill = BOTH)
# mycanvas.create_window((0,0), window = TrialFrameStepUp,anchor = "nw")

TrialFrameStepUp=TrialFrameMainStepUp
FrameStepUpLeft = Frame(TrialFrameStepUp)
FrameStepUpLeft.pack(side = LEFT, expand =True, fill = BOTH)
FrameStepUpRight = Frame(TrialFrameStepUp)
FrameStepUpRight.pack(side = RIGHT, expand =True, fill = BOTH)

#Display filenames + whether clean or not    
SelectFrameStepUpLeft = Frame(FrameStepUpLeft, bg = "DodgerBlue3", bd = 6)
SelectFrameStepUpLeft.pack(expand =True, fill = BOTH)
FrameTrial1StepUp = Frame(FrameStepUpLeft, bg = "ivory3", bd = 6)
FrameTrial1StepUp.pack()
FrameTrial2StepUp = Frame(FrameStepUpLeft, bg = "ghost white", bd = 6)
FrameTrial2StepUp.pack()
FrameTrial3StepUp = Frame(FrameStepUpLeft, bg = "ivory3", bd = 6)
FrameTrial3StepUp.pack()
FrameTrial4StepUp = Frame(FrameStepUpLeft, bg = "ghost white", bd = 6)
FrameTrial4StepUp.pack()
FrameTrial5StepUp = Frame(FrameStepUpLeft, bg = "ivory3", bd = 6)
FrameTrial5StepUp.pack()
FrameTrial6StepUp = Frame(FrameStepUpLeft, bg = "ghost white", bd = 6)
FrameTrial6StepUp.pack()

SelectFrameStepUpRight = Frame(FrameStepUpRight, bg = "DodgerBlue3", bd = 6)
SelectFrameStepUpRight.pack(expand =True, fill = BOTH)
FrameTrial7StepUp = Frame(FrameStepUpRight, bg = "ivory3", bd = 6)
FrameTrial7StepUp.pack()
FrameTrial8StepUp = Frame(FrameStepUpRight, bg = "ghost white", bd = 6)
FrameTrial8StepUp.pack()
FrameTrial9StepUp = Frame(FrameStepUpRight, bg = "ivory3", bd = 6)
FrameTrial9StepUp.pack()
FrameTrial10StepUp = Frame(FrameStepUpRight, bg = "ghost white", bd = 6)
FrameTrial10StepUp.pack()
FrameTrial11StepUp = Frame(FrameStepUpRight, bg = "ivory3", bd = 6)
FrameTrial11StepUp.pack()
FrameTrial12StepUp = Frame(FrameStepUpRight, bg = "ghost white", bd = 6)
FrameTrial12StepUp.pack()

label_file_explorer1StepUp = Label(FrameTrial1StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer2StepUp = Label(FrameTrial2StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer2StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer3StepUp = Label(FrameTrial3StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer3StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer4StepUp = Label(FrameTrial4StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer4StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer5StepUp = Label(FrameTrial5StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer5StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer6StepUp = Label(FrameTrial6StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer6StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer7StepUp = Label(FrameTrial7StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer7StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer8StepUp = Label(FrameTrial8StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer8StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer9StepUp = Label(FrameTrial9StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer9StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer10StepUp = Label(FrameTrial10StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer10StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer11StepUp = Label(FrameTrial11StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer11StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer12StepUp = Label(FrameTrial12StepUp,  text = "", width = 50, height = 2 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer12StepUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

StepUp= {}
def browseFilesStepUp(): 
    #TriallistStepUp.clear()
    suc.set(1)
    global filelistStepUp
    global TriallistStepUp
    TriallistStepUp = []
    filenames = (filedialog.askopenfilenames(
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                      ("all files", "*.*"))))
    #creates a tuple therefore must tur into a list
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
        if i == 6:
            label_file_explorer7StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 7:
            label_file_explorer8StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 8:
            label_file_explorer9StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 9:
            label_file_explorer10StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 10:
            label_file_explorer11StepUp.configure(text="File Opened: "+filelistStepUp[i])
        if i == 11:
            label_file_explorer12StepUp.configure(text="File Opened: "+filelistStepUp[i])
    print(filelistStepUp)
    print(length)
    print(TriallistStepUp)

#EXCTRACT AND NORMALISE DATA
# def cutcycle(footstrike, data):
#     footstrike1 = footstrike[0]
#     footstrike2 = footstrike[1]
#     data1 = (data[footstrike1:footstrike2])
#     return data1
    
def extractintoDictStepUp(filename, TrialNum):     
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
    StepUp[TrialNum].update({"Left": extractvalues(trialacq)})
    StepUp[TrialNum].update({"Right": extractvalues(trialacq)})
    StepUp[TrialNum].update({"lfootstrikeFrame":[]})
    StepUp[TrialNum].update({"rfootstrikeFrame":[]})
    StepUp[TrialNum].update({"lfootoffFrame":[]})
    StepUp[TrialNum].update({"rfootoffFrame":[]})
    StepUp[TrialNum].update({"startframe":trialacq.GetFirstFrame()})#first frame of data
    # #instantiate the nested dict to input in the footstrike etc
  
    for LR in ['Right','Left']:
        for key in StepUp[TrialNum][LR].keys():
            arr = StepUp[TrialNum][LR][key]
            StepUp[TrialNum][LR][key] = {
                    'x':arr[:,0].tolist(),
                    'y':arr[:,1].tolist(),
                    'z':arr[:,2].tolist()
                    }

def extract_all_StepUp_files():
    for i in range(len(TriallistStepUp)):
        extractintoDictStepUp(filelistStepUp[i], TriallistStepUp[i])

button_exploreStepUpLeft = Button(SelectFrameStepUpLeft, text = "Select up to 6 LEFT Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesStepUp(), extract_all_StepUp_files()])  
button_exploreStepUpLeft.pack(pady=20)
button_exploreStepUpRight = Button(SelectFrameStepUpRight, text = "Select up to 6 Right Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesStepUp(), extract_all_StepUp_files()])  
button_exploreStepUpRight.pack(pady=20)
































root.mainloop()
ID = vID.get()
Type = vType.get()
Month = str(vMonth.get()) + " Month(s)"

patient = {}
patient["ID"] = vID.get()
patient["Sex"]= vSex.get()
patient["Dominant Limb"] = vDom.get()
patient["Affected Limb"] = vAffect.get()
patient[Type]= {}
# patient["Type"] = vType.get()
if Type == "Post-op":
    patient[Type][Month]={}
    patient[Type][Month].update({"Month Post-op": vMonth.get()})
    patient[Type][Month].update({"Gait":Gait})
    patient[Type][Month].update({"StepUp":StepUp})
else:
    patient[Type].update({"Gait":Gait})
    patient[Type].update({"StepUp":StepUp})

