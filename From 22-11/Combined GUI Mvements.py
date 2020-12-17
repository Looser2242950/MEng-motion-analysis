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
import matplotlib.pyplot as plt
import statistics
plt.style.use('ggplot')
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.constrained_layout.use'] = False

"""Start SQLite Connection""" 
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('MotionAnalysis109.db')
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

"""TAB 1"""
FrameTop = Frame(tab1, bg = "DodgerBlue3", bd = 6)
FrameTop.pack(expand = 1, fill = BOTH)
FrameInfo = Frame(FrameTop, bg = "DodgerBlue3", bd = 6)
FrameInfo.pack()
FrameMovement = Frame(FrameTop, bg = "DodgerBlue2", bd = 6)
FrameMovement.pack(anchor = NE)
FrameClose = Frame(tab1, bg = "DeepSkyBlue2")
FrameClose.pack(expand = 1, fill = BOTH, side = BOTTOM)

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
labelvisit = Label(FrameInfo,  text = "Patient Visit: ", bg = "ivory3") 
labelvisit.grid(column = 1, row = 7, pady = 5)
vVisit = StringVar()
entryVisit = Entry(FrameInfo,  textvariable = vVisit,   fg = "purple4", width = 20) 
entryVisit.grid(column = 2, row = 7, columnspan = 3)

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
        try:
            x["GRF"] = (trial.GetPoint("LGroundReactionForce")).GetValues()
        except:
            pass
        try:    
            x["NGRF"] = (trial.GetPoint("LNormalisedGRF")).GetValues()
        except:
            pass
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
        try:
            x["GRF"] = (trial.GetPoint("RGroundReactionForce")).GetValues()
        except:
            pass
        try:    
            x["NGRF"] = (trial.GetPoint("RNormalisedGRF")).GetValues()
        except:
            pass
        return x
    Gait[TrialNum].update({"Left": extractvaluesl(trialacq)})
    Gait[TrialNum].update({"Right": extractvaluesr(trialacq)})
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
Framebottom = Frame(TrialFrameStepUp2, bg = "DodgerBlue3", bd = 6)
Framebottom.pack()


labelStepUp = Label(InfoFrameStepUp, text = "StepUp")
labelStepUp["font"] = myFont
labelStepUp.pack()

labelbottom = Label(Framebottom, height = 1,  bg = "DodgerBlue3")
labelbottom.pack()

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
    sdc.set(1)
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


"""Tab 4: StepDown"""

#Display filenames + whether clean or not    
InfoFrameStepDown = Frame(tab4,bg = "DodgerBlue3", bd = 6)
InfoFrameStepDown.pack(fill = BOTH)
SelectFrameStepDown = Frame(tab4,bg = "DodgerBlue3", bd = 6)
SelectFrameStepDown.pack(fill = BOTH)
TrialFrameStepDown1= Frame(tab4,bg = "DodgerBlue3")
TrialFrameStepDown1.pack(fill = BOTH)   
TrialFrameStepDown2= Frame(tab4,bg = "DodgerBlue3")
TrialFrameStepDown2.pack(fill = BOTH)

FrameTrial1StepDown = Frame(TrialFrameStepDown1, bg = "ivory3", bd = 6)
FrameTrial1StepDown.pack()
FrameTrial2StepDown = Frame(TrialFrameStepDown1, bg = "ghost white", bd = 6)
FrameTrial2StepDown.pack()
FrameTrial3StepDown = Frame(TrialFrameStepDown1, bg = "ivory3", bd = 6)
FrameTrial3StepDown.pack()
FrameTrial4StepDown = Frame(TrialFrameStepDown1, bg = "ghost white", bd = 6)
FrameTrial4StepDown.pack()
FrameTrial5StepDown = Frame(TrialFrameStepDown1, bg = "ivory3", bd = 6)
FrameTrial5StepDown.pack()
FrameTrial6StepDown = Frame(TrialFrameStepDown1, bg = "ghost white", bd = 6)
FrameTrial6StepDown.pack()
Framebottom = Frame(TrialFrameStepDown2  , bg = "DodgerBlue3", bd = 6)
Framebottom.pack()


labelStepDown = Label(InfoFrameStepDown, text = "StepDown")
labelStepDown["font"] = myFont
labelStepDown.pack()

labelbottom = Label(Framebottom, height = 1,  bg = "DodgerBlue3")
labelbottom.pack()

label_file_explorer1StepDown = Label(FrameTrial1StepDown,  text = "", width = 50, height = 3 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSD1=StringVar()
vSD1.set(0)
radio_left_1StepDown = Radiobutton(FrameTrial1StepDown, text = "Left", variable = vSD1, value="Left")
radio_right_1StepDown = Radiobutton(FrameTrial1StepDown, text ="Right", variable = vSD1, value = "Right")
radio_both_1StepDown = Radiobutton(FrameTrial1StepDown, text ="Both", variable = vSD1, value = "Both")
radio_left_1StepDown.grid(column = 2,row = 1)
radio_right_1StepDown.grid(column = 3,row = 1)
radio_both_1StepDown.grid(column = 4,row = 1)

label_file_explorer2StepDown = Label(FrameTrial2StepDown,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer2StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSD2=StringVar()
vSD2.set(0)
radio_left_2StepDown = Radiobutton(FrameTrial2StepDown, text = "Left", variable = vSD2, value="Left")
radio_right_2StepDown = Radiobutton(FrameTrial2StepDown, text ="Right", variable = vSD2, value = "Right")
radio_both_2StepDown = Radiobutton(FrameTrial2StepDown, text ="Both", variable = vSD2, value = "Both")
radio_left_2StepDown.grid(column = 2,row = 1)
radio_right_2StepDown.grid(column = 3,row = 1)
radio_both_2StepDown.grid(column = 4,row = 1)

label_file_explorer3StepDown = Label(FrameTrial3StepDown,  text = "", width = 50, height = 3,  fg = "blue", bg = "ghost white") 
label_file_explorer3StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSD3=StringVar()
vSD3.set(0)
radio_left_3StepDown = Radiobutton(FrameTrial3StepDown, text = "Left", variable = vSD3, value="Left")
radio_right_3StepDown = Radiobutton(FrameTrial3StepDown, text ="Right", variable = vSD3, value = "Right")
radio_both_3StepDown = Radiobutton(FrameTrial3StepDown, text ="Both", variable = vSD3, value = "Both")
radio_left_3StepDown.grid(column = 2,row = 1)
radio_right_3StepDown.grid(column = 3,row = 1)
radio_both_3StepDown.grid(column = 4,row = 1)

label_file_explorer4StepDown = Label(FrameTrial4StepDown,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer4StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSD4=StringVar()
vSD4.set(0)
radio_left_4StepDown = Radiobutton(FrameTrial4StepDown, text = "Left", variable = vSD4, value="Left")
radio_right_4StepDown = Radiobutton(FrameTrial4StepDown, text ="Right", variable = vSD4, value = "Right")
radio_both_4StepDown = Radiobutton(FrameTrial4StepDown, text ="Both", variable = vSD4, value = "Both")
radio_left_4StepDown.grid(column = 2,row = 1)
radio_right_4StepDown.grid(column = 3,row = 1)
radio_both_4StepDown.grid(column = 4,row = 1)

label_file_explorer5StepDown = Label(FrameTrial5StepDown,  text = "", width = 50, height = 3,  fg = "blue", bg = "ghost white") 
label_file_explorer5StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSD5=StringVar()
vSD5.set(0)
radio_left_5StepDown = Radiobutton(FrameTrial5StepDown, text = "Left", variable = vSD5, value="Left")
radio_right_5StepDown = Radiobutton(FrameTrial5StepDown, text ="Right", variable = vSD5, value = "Right")
radio_both_5StepDown = Radiobutton(FrameTrial5StepDown, text ="Both", variable = vSD5, value = "Both")
radio_left_5StepDown.grid(column = 2,row = 1)
radio_right_5StepDown.grid(column = 3,row = 1)
radio_both_5StepDown.grid(column = 4,row = 1)

label_file_explorer6StepDown = Label(FrameTrial6StepDown,  text = "", width = 50, height = 3,  fg = "blue", bg = "ivory2") 
label_file_explorer6StepDown.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
vSD6=StringVar()
vSD6.set(0)
radio_left_6StepDown = Radiobutton(FrameTrial6StepDown, text = "Left", variable = vSD6, value="Left")
radio_right_6StepDown = Radiobutton(FrameTrial6StepDown, text ="Right", variable = vSD6, value = "Right")
radio_both_6StepDown = Radiobutton(FrameTrial6StepDown, text ="Both", variable = vSD6, value = "Both")
radio_left_6StepDown.grid(column = 2,row = 1)
radio_right_6StepDown.grid(column = 3,row = 1)
radio_both_6StepDown.grid(column = 4,row = 1)


StepDown = {}
def browseFilesStepDown(Limb): 
    sdc.set(1)
    global TriallistStepDown 
    global filelistStepDown
    TriallistStepDown = []
    filelistStepDown = []

    filenames = (filedialog.askopenfilenames(
        title = "Select a File", 
        filetypes = (("C3D files","*.c3d*"),
                      ("all files", "*.*"))))
    #creates a tuple therefore must turn into a list
    filelistStepDown = list(filenames)
    length = len(filelistStepDown)

    for i in range(length):
        TriallistStepDown.append("Trial "+str(i+1))
        StepDown[TriallistStepDown[i]]={}
        filelistStepDown[i]=os.path.basename(filelistStepDown[i])
        StepDown[TriallistStepDown[i]].update({"Filename": filelistStepDown[i]})
        if i == 0:
            label_file_explorer1StepDown.configure(text="File Opened: "+filelistStepDown[i])
        if i == 1:
            label_file_explorer2StepDown.configure(text="File Opened: "+filelistStepDown[i])
        if i == 2:
            label_file_explorer3StepDown.configure(text="File Opened: "+filelistStepDown[i])
        if i == 3:
            label_file_explorer4StepDown.configure(text="File Opened: "+filelistStepDown[i])
        if i == 4:
            label_file_explorer5StepDown.configure(text="File Opened: "+filelistStepDown[i])
        if i == 5:
            label_file_explorer6StepDown.configure(text="File Opened: "+filelistStepDown[i])

            
            
button_exploreStepDown = Button(SelectFrameStepDown, text = "Select up to 3 LEFT Trials",  width = 40, bg = "ghost white",
                          command = lambda : [browseFilesStepDown("Left")])  
button_exploreStepDown.pack(pady=10)
vStrath2 = IntVar()
vStrath2.set(0)
check_strath2 = Checkbutton(SelectFrameStepDown, text ="Check if Strathclyde Stepping Trial", variable = vStrath2)
check_strath2.pack()









def close_window():
    root.destroy()
#FRAME 3: CANCEL/ACCEPT
buttoncancel = Button(FrameClose, text = "Cancel", command = lambda: close_window())
buttoncancel.pack(side = RIGHT, anchor = CENTER, padx = 10)
buttonaccept = Button(FrameClose, text = "Accept", command = lambda: [close_window()])
buttonaccept.pack(side = RIGHT, anchor = CENTER, padx = 10, pady = 20)
root.mainloop()




























"""SQL GAIT"""



ID = str(123545)
dom_limb = "left"
aff_limb = "left"
tpe = "con"
mon = "4"
sex = "f"

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
             (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb)VALUES (?,?,?,?,?,?)""", 
             (ID, dom_limb, tpe, sex, mon, aff_limb))
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


create_Mean_Gait_Table()
columns_Mean_Gait_Table()
enter_Mean_Gait_Table(Gait["Left Average"],Gait["Right Average"])


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
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb)VALUES (?,?,?,?,?,?)""", 
             (ID, dom_limb, tpe, sex, mon, aff_limb))
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

create_Gait_Max_Min_Table()
columns_Gait_Max_Min_Table()
enter_Gait_extrema()

              
def create_Gait_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Gait_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
              Sex TEXT, Month TEXT, Affected_Limb TEXT,
              Filename TEXT, Complete_Left_Cycle TEXT, Complete_Right_Cycle TEXT,
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


def enter_Gait_Table (numTrials):
    for TrialNum in numTrials:
        filename = Gait[TrialNum]["Filename"] 
        if len(Gait[TrialNum]["lfootstrikeFrame"])>1:
            cleanleft = "Yes"
        else:
            cleanleft = "No"
        if len(Gait[TrialNum]["rfootstrikeFrame"])>1:
            cleanright = "Yes"
        else:
            cleanright = "No"

        c.execute("""INSERT INTO Gait_Table 
                  (ID, Dominant_Limb, Patient_Type, 
                  Sex, Month, Affected_Limb, Filename, 
                  Complete_left_Cycle, Complete_Right_Cycle, 
                  Left_Footstrike_Index, Left_FootOff_Index, 
                  Right_Footstrike_Index, Right_FootOff_Index) 
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""", 
                  (ID, dom_limb, tpe, sex, mon, aff_limb, 
                   filename, cleanleft, cleanright,
                  (str(Gait[TrialNum]["lfootstrikeFrame"])),
                  (str(Gait[TrialNum]["lfootoffFrame"])),
                  (str(Gait[TrialNum]["rfootstrikeFrame"])),
                  (str(Gait[TrialNum]["rfootoffFrame"]))))
        for LR in ["Left", "Right"]:
            for axis in ["x", "y", "z"]:
                c.execute(f"""UPDATE Gait_Table
                          SET 
                          {LR}_Knee_Angle_{axis} = ?,
                          {LR}_Hip_Angle_{axis} = ?,
                          {LR}_Ankle_Angle_{axis} = ?,
                          {LR}_Foot_Progression_Angle_{axis} = ?,
                          {LR}_pelvis_Angle_{axis} =  ?,
                          {LR}_COM_{axis} =  ?
                          WHERE Filename = ?
                          """,(
                          (str(Gait[TrialNum][LR]["KneeAngle"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["HipAngle"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["AnkleAngle"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["FootProgressAngle"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["pelvisAngle"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["COM"][axis])[1:-1]),
                          filename
                          ))
                try:
                    c.execute(f"""UPDATE Gait_Table
                          SET 
                          {LR}_Knee_Moment_{axis} = ?,
                          {LR}_Knee_Force_{axis} = ?,
                          {LR}_Knee_Power_{axis} = ?,
                          {LR}_Hip_Moment_{axis} = ?,
                          {LR}_Hip_Force_{axis} = ?,
                          {LR}_Hip_Power_{axis} = ?,
                          {LR}_Ankle_Moment_{axis} = ?,
                          {LR}_Ankle_Force_{axis} = ?,
                          {LR}_Ankle_Power_{axis} =  ?,
                          {LR}_GRF_{axis} =  ?,
                          {LR}_NGRF_{axis} =  ?,
                          WHERE Filename = ?
                          """,(
                          (str(Gait[TrialNum][LR]["KneeMoment"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["KneeForce"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["KneePower"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["HipMoment"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["HipForce"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["HipPower"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["AnkleMoment"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["AnkleForce"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["AnklePower"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["GRF"][axis])[1:-1]),
                          (str(Gait[TrialNum][LR]["NGRF"][axis])[1:-1]),
                          filename
                          ))
                except:
                    pass

create_Gait_Table()
columns_Gait_Table()
enter_Gait_Table(TriallistGait)















"""STEP UP SQL"""
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
 









def create_StepUp_Max_Min_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepUp_Max_Min_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
               Sex TEXT, Month TEXT, Affected_Limb TEXT, Trial_Type TEXT)""")            
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
              Sex, Month, Affected_Limb, Trial_Type)VALUES (?,?,?,?,?,?,?)""", 
             (ID, dom_limb, tpe, sex, mon, aff_limb, str(StepUp["Trial 1"]["Testing Type"])))
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
              Sex TEXT, Month TEXT, Affected_Limb TEXT, Trial_Type TEXT,
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
                  Sex, Month, Affected_Limb, Filename, Trial_Type) 
                  VALUES (?,?,?,?,?,?,?,?)""", 
                  (ID, dom_limb, tpe, sex, mon, aff_limb, 
                   filename, str(StepUp["Trial 1"]["Testing Type"])))
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




"""STEPDOWN SQL"""

def extractintoDictStepDown(filename, TrialNum, Limb):     
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


def extract_all_StepDown_files():
    def cleanextract(v, trialnum, filename):
        z={}
        if v.get() == "Left":
            z.update(extractintoDictStepDown(filename, trialnum, "Left"))
        if v.get() =="Right":
            z.update(extractintoDictStepDown(filename, trialnum, "Right"))
        if v.get() =="Both":
            z.update(extractintoDictStepDown(filename, trialnum, "Left"))
            z.update(extractintoDictStepDown(filename, trialnum, "Right"))
        return z
    for i in range(len(TriallistStepDown)):           
        if vStrath2.get()==0:
            StepDown[TriallistStepDown[i]].update(cleanextract(va[i], TriallistStepDown[i], filelistStepDown[i]))
            StepDown[TriallistStepDown[i]].update({"Testing Type": "Single Step"})
        if vStrath2.get()==1:
            StepDown[TriallistStepDown[i]].update(cleanextract(va[i], TriallistStepDown[i], filelistStepDown[i]))
            StepDown[TriallistStepDown[i]].update({"Testing Type": "Strathclyde Steps"})
va2= [vSD1, vSD2, vSD3, vSD4, vSD5, vSD6]
extract_all_StepDown_files() 


StepDown["max"]= {}
StepDown["min"] = {}

TriallistStepDownl = []
TriallistStepDownr = []
for i in range(len(TriallistStepDown)):
    if (va[i]).get()=="Left":
        TriallistStepDownl.append(TriallistStepDown[i])
    if (va[i]).get()=="Right":
        TriallistStepDownr.append(TriallistStepDown[i])
    if (va[i]).get()=="Both":
        TriallistStepDownr.append(TriallistStepDown[i])
        TriallistStepDownl.append(TriallistStepDown[i])
        
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
                    o[move][axis] = (((fun(StepDown[cleantrials[0]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[1]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[2]][limb][move][axis])))/3)                    
                if len(cleantrials)== 4:
                    o[move][axis] = (((fun(StepDown[cleantrials[0]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[1]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[2]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[3]][limb][move][axis])))/4)
                    
                if len(cleantrials)== 5:
                    o[move][axis] = (((fun(StepDown[cleantrials[0]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[1]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[2]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[3]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[4]][limb][move][axis])))/5)
                if len(cleantrials)== 6:
                    o[move][axis] = (((fun(StepDown[cleantrials[0]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[1]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[2]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[3]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[4]][limb][move][axis]))+
                                                             (fun(StepDown[cleantrials[5]][limb][move][axis])))/6)

        return o


StepDown["max"].update({"Left":  meanmaxminvals("Left", TriallistStepDownl, "max")})
StepDown["max"].update({"Right":  meanmaxminvals("Right", TriallistStepDownr, "max")})
StepDown["min"].update({"Left":  meanmaxminvals("Left", TriallistStepDownl, "min")})
StepDown["min"].update({"Right":  meanmaxminvals("Right", TriallistStepDownr, "min")})
 









def create_StepDown_Max_Min_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepDown_Max_Min_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
               Sex TEXT, Month TEXT, Affected_Limb TEXT, Trial_Type TEXT)""")            
def columns_StepDown_Max_Min_Table():
    for limb in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Moment_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Force_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Power_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Moment_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Force_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Power_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Moment_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Force_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Power_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Foot_Progression_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_pelvis_Angle_{axis} REAL""")
               c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_COM_{axis} REAL""")   

def enter_StepDown_extrema ():  
    c.execute("""INSERT INTO StepDown_Max_Min_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb, Trial_Type)VALUES (?,?,?,?,?,?,?)""", 
             (ID, dom_limb, tpe, sex, mon, aff_limb,
              str(StepUp["Trial 1"]["Testing Type"])))
    for limb in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
                c.execute(f"""UPDATE StepDown_Max_Min_Table
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
                          (StepDown[function][limb]["KneeAngle"][axis]),
                          (StepDown[function][limb]["KneeMoment"][axis]),
                          (StepDown[function][limb]["KneeForce"][axis]),
                          (StepDown[function][limb]["KneePower"][axis]),
                          (StepDown[function][limb]["HipAngle"][axis]),
                          (StepDown[function][limb]["HipMoment"][axis]),
                          (StepDown[function][limb]["HipForce"][axis]),
                          (StepDown[function][limb]["HipPower"][axis]),
                          (StepDown[function][limb]["AnkleAngle"][axis]),
                          (StepDown[function][limb]["AnkleMoment"][axis]),
                          (StepDown[function][limb]["AnkleForce"][axis]),
                          (StepDown[function][limb]["AnklePower"][axis]),
                          (StepDown[function][limb]["FootProgressAngle"][axis]),
                          (StepDown[function][limb]["pelvisAngle"][axis]),
                          (StepDown[function][limb]["COM"][axis]),
                          ID
                          ))

create_StepDown_Max_Min_Table()
columns_StepDown_Max_Min_Table()
enter_StepDown_extrema()

              
def create_StepDown_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepDown_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
              Sex TEXT, Month TEXT, Affected_Limb TEXT,
              Filename TEXT, Trial_Type TEXT, Complete_Left_Cycle TEXT, Complete_Right_Cycle TEXT,
              Left_Footstrike_Index TEXT, Left_FootOff_Index TEXT,
              Right_Footstrike_Index TEXT, Right_FootOff_Index TEXT)""")            
def columns_StepDown_Table():
     for LR in ["Left", "Right"]:
         for axis in ["x", "y", "z"]:
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Knee_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Knee_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Knee_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Knee_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Hip_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Hip_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Hip_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Hip_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Ankle_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Ankle_Moment_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Ankle_Force_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Ankle_Power_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Foot_Progression_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_pelvis_Angle_{axis} TEXT""")
             c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_COM_{axis} TEXT""")             


def enter_StepDown_Table (numTrials):
    for TrialNum in numTrials:
        filename = StepDown[TrialNum]["Filename"] 
        c.execute("""INSERT INTO StepDown_Table 
                  (ID, Dominant_Limb, Patient_Type, 
                  Sex, Month, Affected_Limb, Filename, Trial_Type) 
                  VALUES (?,?,?,?,?,?,?,?)""", 
                  (ID, dom_limb, tpe, sex, mon, aff_limb, 
                   filename, str(StepUp["Trial 1"]["Testing Type"])))
        for LR in ["Left", "Right"]:
            try:
                for axis in ["x", "y", "z"]:
                    c.execute(f"""UPDATE StepDown_Table
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
                              (str(StepDown[TrialNum][LR]["KneeAngle"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["HipAngle"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["AnkleAngle"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["FootProgressAngle"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["pelvisAngle"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["COM"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["KneeMoment"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["KneeForce"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["KneePower"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["HipMoment"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["HipForce"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["HipPower"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["AnkleMoment"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["AnkleForce"][axis])[1:-1]),
                              (str(StepDown[TrialNum][LR]["AnklePower"][axis])[1:-1]),
                              filename
                              ))
            except:
                pass


create_StepDown_Table()
columns_StepDown_Table()
enter_StepDown_Table(TriallistStepDown)





















"""Close SQLite Connection"""
conn.commit()
conn.close()     




































# ID = vID.get()
# Type = vType.get()
# Month = str(vMonth.get()) + " Month(s)"

# patient = {}
# patient["ID"] = vID.get()
# patient["Sex"]= vSex.get()
# patient["Dominant Limb"] = vDom.get()
# patient["Affected Limb"] = vAffect.get()
# patient["Type"] = Type


# patient["Gait"]= Gait
# patient["StepUp"]= StepUp
# patient["StepDown"]= StepDown
# # patient["StandUp"]= StandUp
# # patient["SitDown"]= SitDown
# # patient["RampGait"]= RampGait

# if Type == "Post-op":
#     patient["Month"] = vMonth.get()

    



# def writetodict():
#     name = ID + Type + str(vMonth.get()) + ".json"
#     with open(name, 'w') as f:
#         json.dump(patient, f, indent = 5)    
# writetodict()


