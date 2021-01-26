# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:07:27 2020

@author: Johanna Looser
"""
import numpy as np
import btk
import sqlite3
import json
from tkinter import *
from tkinter import filedialog 
import os.path 
from tkinter import ttk
import tkinter.font as font
import matplotlib.pyplot as plt
import csv
import os

"""connect to SQLite Database. For testing purposes, connect to "memory" """

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('MAD.db')
c=conn.cursor()

"""State all variables used and their names used in th C3D files"""
variables = ["KneeAngle", "KneeForce", "KneeMoment", "KneePower",
             "HipAngle", "HipForce", "HipMoment", "HipPower",
             "AnkleAngle", "AnkleForce", "AnkleMoment", "AnklePower",
             "FootProgressAngle", "PelvisAngle", "COM", "GRF", "NGRF"] 

leftcolumns = ["LKneeAngles", "LKneeForce", "LKneeMoment", "LKneePower",
             "LHipAngles", "LHipForce", "LHipMoment", "LHipPower",
             "LAnkleAngles", "LAnkleForce", "LAnkleMoment", "LAnklePower",
             "LFootProgressAngles", "LPelvisAngles", 
             "CentreOfMass", "LGroundReactionForce", "LNormalisedGRF"] 

rightcolumns = ["RKneeAngles", "RKneeForce", "RKneeMoment", "RKneePower",
             "RHipAngles", "RHipForce", "RHipMoment", "RHipPower",
             "RAnkleAngles", "RAnkleForce", "RAnkleMoment", "RAnklePower",
             "RFootProgressAngles", "RPelvisAngles", 
             "CentreOfMass", "RGroundReactionForce", "RNormalisedGRF"] 

"""begin Tkinter GUI window.
Setup Tabs within root window"""
root = Tk()
root.title("Motion Analysis Database System Interface")
root.geometry("600x750")
myFont = font.Font(family = "Helvetica", size=30)
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
tab_parent.pack(expand=1, fill="both")


"""TAB 1: Input Patient Data.
This is the first thing that appears in the GUI.
The tab is split vertically with three frames on top of eachother. 
The top frame contains the titel frame and frame where the patient data is input 
as well as a checkbox of which movements ahve been selected.
The next frame is the "Next" button for moving on to file selection,
The bottom Frame has buttons for accept or cancel once all files have been selected """
FrameTop = Frame(tab1, bg = "DodgerBlue3", bd = 6)
FrameTop.pack(expand = 1, fill = BOTH)
FrameTitle = Frame(FrameTop, bg = "DodgerBlue3", bd = 6)
FrameTitle.pack(fill = X)
FrameInfo = Frame(FrameTop,bd = 6, bg = "SlateGray4")
FrameInfo.pack()

FrameNext = Frame(tab1 )
FrameNext.pack(fill = BOTH, pady  =10)
FrameClose = Frame(tab1, bg = "DodgerBlue3")
FrameClose.pack(expand = 2, fill = BOTH)


label_title = Label(FrameTitle, text = "Input Motion Analysis Data", bg = "white")
label_title.pack(pady = 20, padx = 20, fill= X)
label_title["font"] = myFont

 
"""This shows the Tkinter widgets for inputting the patient data
If the preop option is selected, the month entry box is dissabled as this is
 for number of months post op. If the control option is selected, both month 
 and affected limb are dissabled as the control will have no damaged knee"""
labelID = Label(FrameInfo,  text = "Patient ID: ") 
labelID.grid(column = 1, row = 1, pady = 5)
vID = StringVar()
entryID = Entry(FrameInfo,  textvariable = vID,   fg = "RoyalBlue4", width = 20) 
entryID.grid(column = 2, row = 1, columnspan = 3)
labelSex = Label(FrameInfo,  text = "Sex: ") 
labelSex.grid(column = 1, row = 2, pady = 5)
vSex = StringVar()
vSex.set(0)
radiomale = Radiobutton(FrameInfo, text="Male",variable= vSex, value="Male")
radiomale.grid(column = 2, row = 2)
radiofemale = Radiobutton(FrameInfo, text="Female",variable= vSex, value="Female")
radiofemale.grid(column = 3, row = 2)
labelDom = Label(FrameInfo,  text = "Dominant Limb: ") 
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
            self.labelvisit.configure(state = "normal")
            self.entryVisit.configure(state = "normal")
        if vType.get() == "Control":
            self.month_entry.configure(state = "disabled")
            self.date_label.configure(state = "disabled")
            self.limb_label.configure(state = "disabled")
            self.radioleft.configure(state = "disabled")
            self.radioright.configure(state = "disabled")
            self.radioboth.configure(state = "disabled")
            self.labelvisit.configure(state = "disabled")
            self.entryVisit.configure(state = "disabled")
        if vType.get() == "Pre-op":
            self.month_entry.configure(state = "disabled")
            self.date_label.configure(state = "disabled")    
            self.limb_label.configure(state = "normal")
            self.radioleft.configure(state = "normal")
            self.radioright.configure(state = "normal")
            self.radioboth.configure(state = "normal")
            self.labelvisit.configure(state = "normal")
            self.entryVisit.configure(state = "normal")
           
    def __init__(self, master):
        self.label_type = Label(FrameInfo, text = "Patient Type: ")
        self.label_type.grid(column = 1, row = 4, pady = 5)
        global vType
        vType = StringVar()
        self.optiontype = OptionMenu(FrameInfo, vType, "Pre-op", "Post-op", "Control", 
                                      command = self.disable)
        self.optiontype.config(width = 20)
        self.optiontype.grid(column = 2, row = 4, columnspan  =3)
        
        self.date_label = Label(FrameInfo, text = "Number of months Post - Op: ")
        self.date_label.grid(column = 1, row  = 5, pady = 5)
        global vMonth
        vMonth = IntVar() 
        self.month_entry = Entry(FrameInfo, textvariable = vMonth, width = 20, fg = "RoyalBlue4")
        self.month_entry.grid(column = 2, row = 5, columnspan  = 3)
        self.limb_label = Label(FrameInfo, text = "Affected Limb: ")
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
        global vVisit
        vVisit = IntVar()
        vVisit.set(1)
        self.labelvisit = Label(FrameInfo,  text = "Patient Visit: ") 
        self.labelvisit.grid(column = 1, row = 7, pady = 5)
        self.entryVisit = Entry(FrameInfo,  textvariable = vVisit,   fg = "RoyalBlue4", width = 20) 
        self.entryVisit.grid(column = 2, row = 7, columnspan = 3)

Pattype(FrameInfo)

"""This Frame contains checkboxes for each of the movement that are automatically 
checked when files are selected. This is not fucntional and purely aesthetic at
the moment"""
gc = IntVar()
suc = IntVar()
sdc = IntVar()
stsc = IntVar()
class checkboxes:
    def __init__(self, tab):
        self.tab = tab
    def boxes(self):
        self.FrameMovement = Frame(self.tab, height = 10, bg = "DodgerBlue2", bd = 6)
        self.FrameMovement.pack(fill = BOTH, side = BOTTOM)
        self.movelabel = Label(self.FrameMovement, text = "Completed File Upload:")
        self.movelabel.pack(side = LEFT, fill = BOTH, expand  = 2)
        
        self.Gaitlabel = Label(self.FrameMovement, text = "Gait")
        self.Gaitlabel.pack(side = LEFT, fill = BOTH, expand  = 2)
        self.Gaitcheck = Checkbutton(self.FrameMovement, variable = gc, state = "disabled")
        self.Gaitcheck.pack(side = LEFT, fill = BOTH, expand  = 2)
        
        self.StepUplabel = Label(self.FrameMovement, text = "StepUp")
        self.StepUplabel.pack(side = LEFT, fill = BOTH, expand  = 2)
        self.StepUpcheck = Checkbutton(self.FrameMovement, variable = suc, state = "disabled")
        self.StepUpcheck.pack(side = LEFT, fill = BOTH, expand  = 2)
        
        self.StepDownlabel = Label(self.FrameMovement, text = "StepDown")
        self.StepDownlabel.pack(side = LEFT, fill = BOTH, expand  = 2)
        self.StepDowncheck = Checkbutton(self.FrameMovement, variable = sdc, state = "disabled")
        self.StepDowncheck.pack(side = LEFT, fill = BOTH, expand  = 2)
        
        self.SitStandSitlabel = Label(self.FrameMovement, text = "SitStandSit")
        self.SitStandSitlabel.pack(side = LEFT, fill = BOTH, expand  = 2)
        self.SitStandSitcheck = Checkbutton(self.FrameMovement, variable = stsc, state = "disabled")
        self.SitStandSitcheck.pack(side = LEFT, fill = BOTH, expand  = 2)

checkboxes(tab1).boxes()

"""The FrameNext gives a label to select next to continue to file selection, 
as well as th "Next" button to the totab2 function which switches to the next tab"""
def totab2():
    tab_parent.select(tab2)
    
label_Next = Label(FrameNext, text = """Select to Save and Continue to File Selection.""")
label_Next.pack(pady = 10)   
    
button_next1 = Button(FrameNext, bg = "RoyalBlue4",fg = "white", text = "Save and Continue", command  = lambda:[totab2()] )
button_next1.pack()





"""Tab 2: Gait
The layout of this Frame includes the top Frame (InfoFrameGait) where the title 
of the movement is, then the SelectFrame which contains the Select Trials button
and the Trial Frame Gait Frame. 
This contains 7 subframes, 6 are for each of the 6 potential uploaded trials and
one for the bottom frame where the next and skip buttons are located. 
Withi each trial subframe there i a label (labelfileexplorer) which changes to
show the filename of the uploaded file. There are two other labels which display
whether the uploaded file has a full gait cyle in the left and/or right limbs
"""

InfoFrameGait = Frame(tab2,bg = "DodgerBlue3", bd = 6)
InfoFrameGait.pack(fill = BOTH)
SelectFrameGait = Frame(tab2,bg = "DodgerBlue3", bd = 6)
SelectFrameGait.pack(fill = BOTH)
TrialFrameGait= Frame(tab2,bg = "DodgerBlue3")
TrialFrameGait.pack(expand =1, fill = BOTH)

#Display filenames + whether clean or not    
FrameTrial1Gait = Frame(TrialFrameGait, bg = "SlateGray4", bd = 6)
FrameTrial1Gait.pack()
FrameTrial2Gait = Frame(TrialFrameGait, bg = "ghost white", bd = 6)
FrameTrial2Gait.pack()
FrameTrial3Gait = Frame(TrialFrameGait, bg = "SlateGray4", bd = 6)
FrameTrial3Gait.pack()
FrameTrial4Gait = Frame(TrialFrameGait, bg = "ghost white", bd = 6)
FrameTrial4Gait.pack()
FrameTrial5Gait = Frame(TrialFrameGait, bg = "SlateGray4", bd = 6)
FrameTrial5Gait.pack()
FrameTrial6Gait = Frame(TrialFrameGait, bg = "ghost white", bd = 6)
FrameTrial6Gait.pack()
FramebottomGait = Frame(TrialFrameGait, bg = "DodgerBlue3", bd = 6)
FramebottomGait.pack()

labelGait = Label(InfoFrameGait, text = "Gait", bg = "white")
labelGait["font"] = myFont
labelGait.pack(pady = 10, padx= 20, fill = X)
labelGait2 = Label(InfoFrameGait, text = "Ensure selected files include a minimum of three clean gait cycles per limb", bg = "white")
labelGait2.pack(padx = 20,  side = BOTTOM)

labelbottomGait = Label(FramebottomGait, height = 1,  bg = "DodgerBlue3")
labelbottomGait.pack()

class gaitlabel():
    def __init__(self, Frame, col1, col2):
        self.Frame = Frame
        self.col1 = col1
        self.col2 = col2
    def label(self):
        self.label_file_explorer = Label(self.Frame,  text = "", width = 50, height = 3 ,  fg = "blue" , bg = self.col1) 
        self.label_file_explorer.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
        self.label_cleanl = Label(self.Frame, text="",  width = 25, bg =  self.col2)
        self.label_cleanl.grid(column = 2, row = 1)
        self.label_cleanr = Label(self.Frame, text="",  width = 25, bg =  self.col2)
        self.label_cleanr.grid(column = 2, row = 2)
        return self.label_file_explorer, self.label_cleanl, self.label_cleanr
        
label_file_explorer1Gait,label_clean1Gait, label_clean1rGait = gaitlabel(FrameTrial1Gait, "ghost white", "SlateGray4").label()
label_file_explorer2Gait,label_clean2Gait, label_clean2rGait = gaitlabel(FrameTrial2Gait, "gray80", "ghost white").label()
label_file_explorer3Gait,label_clean3Gait, label_clean3rGait = gaitlabel(FrameTrial3Gait, "ghost white", "SlateGray4").label()
label_file_explorer4Gait,label_clean4Gait, label_clean4rGait = gaitlabel(FrameTrial4Gait, "gray80", "ghost white").label()
label_file_explorer5Gait,label_clean5Gait, label_clean5rGait = gaitlabel(FrameTrial5Gait, "ghost white", "SlateGray4").label()
label_file_explorer6Gait,label_clean6Gait, label_clean6rGait = gaitlabel(FrameTrial6Gait, "gray80", "ghost white").label()



"""Initiate the Gait Dictionary and the lists for cleanlefttrials and clean right trials
These will include trhe trials from the complete trial list that are clean on the corresponding limb. """
Gait = {}
cleanlefttrials=[]
cleanrighttrials=[]

"""This function is called by the "Select Trials" button. This function open the 
file exploer and allows the user to select multiple files using ctrl click or click 
and dragging. The filenames of all files selected are put into the list filelistGait.
For every filename in that list, a corresponding value is entered into the TriallistGait
list in the form of "Trial 1", "Trial 2", etc. 
Starting at the first Trial Gait Frame, the labels are populated with the filename ie,
the first filename will be shown in the label of the top Frame etc """
def browseFilesGait(): 
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
        Gait[TriallistGait[i]].update({"Filename": filelistGait[i]})
        if i == 0:
            label_file_explorer1Gait.configure(text="File Opened: "+ os.path.basename(filelistGait[i]))
        if i == 1:
            label_file_explorer2Gait.configure(text="File Opened: "+os.path.basename(filelistGait[i]))
        if i == 2:
            label_file_explorer3Gait.configure(text="File Opened: "+os.path.basename(filelistGait[i]))
        if i == 3:
            label_file_explorer4Gait.configure(text="File Opened: "+os.path.basename(filelistGait[i]))
        if i == 4:
            label_file_explorer5Gait.configure(text="File Opened: "+os.path.basename(filelistGait[i]))
        if i == 5:
            label_file_explorer6Gait.configure(text="File Opened: "+os.path.basename(filelistGait[i]))
            
            
"""the following definitions are all interconnected so will be explained together below"""



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
    def extractvaluesl(trial): #for every variable, the left data is extracted into the dict x
        x=dict();
        for i in range(len(variables)):
            try:
                x[variables[i]]= (trial.GetPoint(leftcolumns[i])).GetValues()
            except:
                pass
        return x
    def extractvaluesr(trial): #for every variable the right data is extracted into dict x
        x=dict();
        for i in range(len(variables)):
            try:
                x[variables[i]]= (trial.GetPoint(rightcolumns[i])).GetValues()
            except:
                pass
        return x

    Gait[TrialNum].update({"Left": extractvaluesl(trialacq)}) #save left data in to dict
    Gait[TrialNum].update({"Right": extractvaluesr(trialacq)}) #save right data into dict
    
    
    Gait[TrialNum].update({"lfootstrikeFrame":[]}) # instantiate the nested dict to input in the footstrike etc
    Gait[TrialNum].update({"rfootstrikeFrame":[]})
    Gait[TrialNum].update({"lfootoffFrame":[]})
    Gait[TrialNum].update({"rfootoffFrame":[]})
    
    
    Gait[TrialNum].update({"startframe":trialacq.GetFirstFrame()})#first frame of data
    for i in range(trialacq.GetEventNumber()): #populate dict with event Frame numbers
        eventnum = trialacq.GetEvent(i)
        if eventnum.GetLabel()=="Foot Strike":
            if eventnum.GetContext() == "Left": #subtract start frame from frame number to get index
                Gait[TrialNum]["lfootstrikeFrame"].append(eventnum.GetFrame()-Gait[TrialNum]["startframe"])
            else:
                Gait[TrialNum]["rfootstrikeFrame"].append(eventnum.GetFrame()-Gait[TrialNum]["startframe"])
        if eventnum.GetLabel()=="Foot Off":
            if eventnum.GetContext() == "Left":
                Gait[TrialNum]["lfootoffFrame"].append(eventnum.GetFrame()-Gait[TrialNum]["startframe"])
            else:
                Gait[TrialNum]["rfootoffFrame"].append(eventnum.GetFrame()-Gait[TrialNum]["startframe"])

    for event in ["lfootstrikeFrame", "rfootstrikeFrame", "lfootoffFrame", "rfootoffFrame"]: #chronological order events
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
    
    if len(Gait[TrialNum]["lfootstrikeFrame"])>1: #if left limb is clean
        Gait[TrialNum].update({"Clean Left": "Yes"})
        cleanlefttrials.append(TrialNum)
        labelleft.configure(text = "Clean Left Gait Cycle")
        for i in range(len(variables)): #cut left data to include only full cycle
            try:
                Gait[TrialNum]["Left"][variables[i]] = cutcycle(Gait[TrialNum]["lfootstrikeFrame"], Gait[TrialNum]["Left"][variables[i]])
            except:
                pass
        Gait[TrialNum]["lfootoffFrame"]=(np.array(Gait[TrialNum]["lfootoffFrame"])-(Gait[TrialNum]["lfootstrikeFrame"])[0]).tolist()
        Gait[TrialNum]["lfootstrikeFrame"]=(np.array(Gait[TrialNum]["lfootstrikeFrame"])-(Gait[TrialNum]["lfootstrikeFrame"])[0]).tolist()
    else: #if left limb is not clean
        Gait[TrialNum].update({"Clean Left": "No"})
        labelleft.configure(text = "Incomplete Left Gait Cycle")
    for item in Gait[TrialNum]["lfootoffFrame"]: #remove events from before clean cycle begins
        if item <0:
            Gait[TrialNum]["lfootoffFrame"].remove(item)
            
    if len(Gait[TrialNum]["rfootstrikeFrame"])>1: #if right limb is clean
        cleanrighttrials.append(TrialNum)
        Gait[TrialNum].update({"Clean Right": "Yes"})
        labelright.configure(text = "Clean Right Gait Cycle")
        for i in range(len(variables)): #cut right data
            try:
                Gait[TrialNum]["Right"][variables[i]] = cutcycle(Gait[TrialNum]["rfootstrikeFrame"], Gait[TrialNum]["Right"][variables[i]])
            except:
                pass

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
    
    def interpolate(cutdata): #interpolate data over 100 points
        increment = 100/len(cutdata)
        Timepercent = np.arange(0, 100, increment).tolist() 
        x = np.array(range(100))
        datainterp = np.interp(x, Timepercent, cutdata)
        return datainterp       

#make array into list for SQL:
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
    def meanvals(limb, cleantrials): #calculate average full data sets from interpolated cycles
        o={}
        
        for axis in ["x","y","z"]:
            if len(cleantrials)== 3:
                for move in variables:
                    try:
                        o[move]={}
                        o[move][axis] = (np.mean((np.array(Gait[cleantrials[0]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[1]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[2]][limb][move][axis])), 
                                                                  axis = 0)).tolist()
                    except:
                        pass
                        
            if len(cleantrials)== 4:
                for move in variables:
                    try:
                        o[move][axis] = (np.mean((np.array(Gait[cleantrials[0]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[1]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[2]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[3]][limb][move][axis])),
                                                                  axis = 0)).tolist()
                          
                    except:
                        pass
            if len(cleantrials)== 5:
                for move in variables:
                    try:
                        o[move][axis] = (np.mean((np.array(Gait[cleantrials[0]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[1]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[2]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[3]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[4]][limb][move][axis])), 
                                                                  axis = 0)).tolist()
                    except:
                        pass
            if len(cleantrials)== 6:
                for move in variables:
                    try:
                        o[move][axis] = (np.mean((np.array(Gait[cleantrials[0]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[1]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[2]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[3]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[4]][limb][move][axis]),
                                                                  np.array(Gait[cleantrials[5]][limb][move][axis])),
                                                                  axis = 0)).tolist()
                    except:
                        pass
        return o

    Gait["Left Average"].update(meanvals("Left", cleanlefttrials)) #save mean data sets
    Gait["Right Average"].update(meanvals("Right", cleanrighttrials))


def extract_all_Gait_files():
    for i in range(len(TriallistGait)):
        extractintoDict(filelistGait[i], TriallistGait[i])
        filelistGait[i]=os.path.basename(filelistGait[i])
        Gait[TriallistGait[i]].update({"Filename": filelistGait[i]})
    print("Uploaded Gait Files: " + str(filelistGait))

"""The button for selecting the trials is created and calls two fucntions. The first is the 
"Browse files function already described. This outputs two lists f equal length: one with the filenames
and the other with the Trial numbers in the form of "Trial 1", "Trial 2", etc.

The second function it calls is the extract_all_Gait_files(). This function serves to iterate
the extractintoDict() as many times as there are files selected. 

The extract to Dict uses the btk package to create an btk acquisition object of the file.
It uses the functions extractvaluesl and extractvaluesr to extract the arrays from the 
btk acquisitioon and save them in the Gait[Trialnum]["Left"] dictionary (or right).
The btk function getEvent is used to find the heelstrike and foot off eventsand save their index 
in the corresponding lists in the dictionary. 

The start frame is the frame from the start of the recording at which the first datapoint is taken.
The point data is saved with the first datapoint being index 0, therefore the start frame index is 
subtracted from the Event indices so they correspond correctly. 

The events are sorted chronologically within their lists.

If more than one footstrike occurs on that limb, the limb is considered "clean" as a full cycle
can be shown. For these, the data is cut to only include indices from the point fo the firts heelstrike 
to the second heelstrike. There has been some issues with GRF and NGRF so they are in try excepts. 
If the data is clean the label corresponding to that trial is updated to say "Clean L/R cycle"
if not it will say "Incomplete Left/Right Cycle". The foot off index is adjusted as the data has been cut.

The next part is averaging the data. New subdictionaries (Left Average and Right Average) are
created. The left average foot off is found using the footoff function. This calculates the average percent
through the gait cycle the footoff occurs (usually between 60-70%). 

All the variables array are split into lists separating the x. y, and z data. For trials with clean 
cycle, the data is interpolated so the same pattern is followed but in exactly 100 points. 

Using the meanvals() function, these trials are averaged out to create the average left and average right 
data for each variable. 
 """

    
      
button_exploreGait = Button(SelectFrameGait, text = "Select up to 6 Trials",  width = 40, bg = "RoyalBlue4",fg= "white",
                          command = lambda : [browseFilesGait(), extract_all_Gait_files()])  
button_exploreGait.pack(pady=10)

 
"""The two buttons are "Next" for following selecting the files and "Skip" if you dont have Gait files 
to select. For this movement, both buttons do the same thing and move to the next tab via the totab3() """
def totab3():
    tab_parent.select(tab3)

def checkboxGait():  
    gc.set(1)


                    
button_nextGait = Button(FramebottomGait, bg = "RoyalBlue4",fg = "white", text = "Import Files to System", command  = lambda:[ totab3(), checkboxGait()])
button_nextGait.pack(pady = 10)

button_skip2 = Button(FramebottomGait, fg = "gray", text = "Skip", command  = lambda:[totab3()])
button_skip2.pack(pady = 10)

checkboxes(tab2).boxes()

"""Tab 3: Stepup
Very similar to Gait but no cycles to normalise
Similar Frame and label structure.
On the TrialFrames, following selecting the trials, the filenames will appear in
the labels(same as gait). Next to the file name is radiobuttons for "Left", "Right" or "both"
This shows which limb was used for stepping up in that recording. 
"""

InfoFrameStepUp = Frame(tab3,bg = "DodgerBlue3", bd = 6)
InfoFrameStepUp.pack(fill = BOTH)
SelectFrameStepUp = Frame(tab3,bg = "DodgerBlue3", bd = 6)
SelectFrameStepUp.pack(fill = BOTH)
TrialFrameStepUp1= Frame(tab3,bg = "DodgerBlue3")
TrialFrameStepUp1.pack(expand =1, fill = BOTH)   
TrialFrameStepUp2= Frame(tab3,bg = "DodgerBlue3")
TrialFrameStepUp2.pack(expand =1, fill = BOTH)

FrameTrial1StepUp = Frame(TrialFrameStepUp1, bg = "SlateGray4", bd = 6)
FrameTrial1StepUp.pack()
FrameTrial2StepUp = Frame(TrialFrameStepUp1, bg = "ghost white", bd = 6)
FrameTrial2StepUp.pack()
FrameTrial3StepUp = Frame(TrialFrameStepUp1, bg = "SlateGray4", bd = 6)
FrameTrial3StepUp.pack()
FrameTrial4StepUp = Frame(TrialFrameStepUp1, bg = "ghost white", bd = 6)
FrameTrial4StepUp.pack()
FrameTrial5StepUp = Frame(TrialFrameStepUp1, bg = "SlateGray4", bd = 6)
FrameTrial5StepUp.pack()
FrameTrial6StepUp = Frame(TrialFrameStepUp1, bg = "ghost white", bd = 6)
FrameTrial6StepUp.pack()
FramebottomStepUp = Frame(TrialFrameStepUp2, bg = "DodgerBlue3", bd = 6)
FramebottomStepUp.pack()
labelStepUp = Label(InfoFrameStepUp, text = "StepUp", bg = "white")
labelStepUp["font"] = myFont
labelStepUp2 = Label(InfoFrameStepUp, text = "Ensure selected files include a minimum of three clean steps per limb", bg = "white")
labelStepUp2.pack(padx = 20,  side = BOTTOM)

labelStepUp.pack(pady = 10, padx = 20, fill = X)
labelbottomStepUp = Label(FramebottomStepUp, height = 1,  bg = "DodgerBlue3")
labelbottomStepUp.pack()

class StepUplabel():
    def __init__(self, Frame, col1):
        self.Frame = Frame
        self.col1 = col1
    def label(self):
        self.label_file_explorer = Label(self.Frame,  text = "", width = 50, height = 3 ,  fg = "blue" , bg = self.col1) 
        self.label_file_explorer.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
        self.var=StringVar()
        self.var.set(0)
        self.radio_left = Radiobutton(self.Frame, text = "Left", variable = self.var, value="Left")
        self.radio_right = Radiobutton(self.Frame, text ="Right", variable = self.var, value = "Right")
        self.radio_both = Radiobutton(self.Frame, text ="Both", variable = self.var, value = "Both")
        self.radio_left.grid(column = 2,row = 1)
        self.radio_right.grid(column = 3,row = 1)
        self.radio_both.grid(column = 4,row = 1)
        return self.label_file_explorer, self.var
        
label_file_explorer1StepUp,vSU1,  = StepUplabel(FrameTrial1StepUp, "ghost white").label()
label_file_explorer2StepUp,vSU2,  = StepUplabel(FrameTrial2StepUp, "gray80").label()
label_file_explorer3StepUp,vSU3,  = StepUplabel(FrameTrial3StepUp, "ghost white").label()
label_file_explorer4StepUp,vSU4,  = StepUplabel(FrameTrial4StepUp, "gray80").label()
label_file_explorer5StepUp,vSU5,  = StepUplabel(FrameTrial5StepUp, "ghost white").label()
label_file_explorer6StepUp,vSU6,  = StepUplabel(FrameTrial6StepUp, "gray80").label()


"""Same as in Gait the dictionary is initiated and the Browse files function creates the 
filelist and trial list as well as updating the labels with the filenames"""
StepUp = {}
StepUp["max"]= {}
StepUp["min"] = {}
def browseFilesStepUp(): 
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
        StepUp[TriallistStepUp[i]].update({"Filename": filelistStepUp[i]})
        if i == 0:
            label_file_explorer1StepUp.configure(text="File Opened: "+os.path.basename(filelistStepUp[i]))
        if i == 1:
            label_file_explorer2StepUp.configure(text="File Opened: "+os.path.basename(filelistStepUp[i]))
        if i == 2:
            label_file_explorer3StepUp.configure(text="File Opened: "+os.path.basename(filelistStepUp[i]))
        if i == 3:
            label_file_explorer4StepUp.configure(text="File Opened: "+os.path.basename(filelistStepUp[i]))
        if i == 4:
            label_file_explorer5StepUp.configure(text="File Opened: "+os.path.basename(filelistStepUp[i]))
        if i == 5:
            label_file_explorer6StepUp.configure(text="File Opened: "+os.path.basename(filelistStepUp[i]))

"""The following fucntions are intercnnected and explained below"""
def extractintoDictStepUp(filename, TrialNum, Limb):     
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename) # set a filename to the reader
    reader.Update()
    trialacq = reader.GetOutput() # is the btk aquisition object
    def extractvaluesl(trial): #for every variable, the left data is extracted into the dict x
        x=dict();
        for i in range(len(variables)):
            try:
                x[variables[i]]= (trial.GetPoint(leftcolumns[i])).GetValues()
            except:
                pass
        return x
    def extractvaluesr(trial): #for every variable the right data is extracted into dict x
        x=dict();
        for i in range(len(variables)):
            try:
                x[variables[i]]= (trial.GetPoint(rightcolumns[i])).GetValues()
            except:
                pass
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
    va= [vSU1, vSU2, vSU3, vSU4, vSU5, vSU6]
    global TriallistStepUpl 
    global TriallistStepUpr 
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

def meanmaxminvals(limb, cleantrials, function):
        o={}
        if function == "max":
            fun = max
        if function == "min":
            fun = min
        for move in variables:
            try:
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
            except:
                pass
        return o

def add_max_min_to_dict():
    StepUp["max"].update({"Left":  meanmaxminvals("Left", TriallistStepUpl, "max")})
    StepUp["max"].update({"Right":  meanmaxminvals("Right", TriallistStepUpr, "max")})
    StepUp["min"].update({"Left":  meanmaxminvals("Left", TriallistStepUpl, "min")})
    StepUp["min"].update({"Right":  meanmaxminvals("Right", TriallistStepUpr, "min")})
    for i in range(len(filelistStepUp)):    
        filelistStepUp[i]=os.path.basename(filelistStepUp[i])
        StepUp[TriallistStepUp[i]].update({"Filename": filelistStepUp[i]})
    print("Uploaded StepUp Files: " + str(filelistStepUp))
     
            
"""The selct function calls the browse files function( explained above) but DOES NOT
excact the info, therefore it's vital the Next button is pressed.

The checkbox for if the trials were strtahclyde or not is used to create the variable which
is sved with the data for referencing when analysing."""
            
button_exploreStepUp = Button(SelectFrameStepUp, text = "Select Trials",  width = 40, bg = "RoyalBlue4",fg= "white",
                          command = lambda : [browseFilesStepUp()])  
button_exploreStepUp.pack(pady=10)
vStrath = IntVar()
vStrath.set(0)
check_strath = Checkbutton(SelectFrameStepUp, text ="Check if Strathclyde Stepping Trial", variable = vStrath)
check_strath.pack()

"""The Next button is pressed once the files are elected and all the radiobutton inputs are 
inputted. This calls the extract all stepup files function. This function creates
a list of trials with the left leg and tirals with the right leg based off the radiobutton inputs.
The variables are all extracted using btk and assigned to left or right limb. If the 
checkbox for strathclyde stepping was pressed then the key value pair is
"Testing Type": "Strathclyde Steps" if not, "Testing Type": "Single Step". 

The next button also calls the add to maxmin which find the maximum values of each
trial in the left limb, and averages them, doing the same for right limb and minimum.

The next button and the skip button also call the to tab4 function which moves on to the next tab"""

def totab4():
    tab_parent.select(tab4)
def checkboxStepUp():  
    suc.set(1)
  

button_next3 = Button(FramebottomStepUp,bg = "RoyalBlue4",fg = "white", text = "Import Files to System", 
                      command  = lambda:[extract_all_StepUp_files(), 
                                          add_max_min_to_dict(), checkboxStepUp(), totab4()] )
button_next3.pack(pady=10)

button_skip3 = Button(FramebottomStepUp, fg = "gray", text = "Skip", 
                      command  = lambda:[totab4()])
button_skip3.pack(pady = 10)  

checkboxes(tab3).boxes()


"""Tab 4: StepDown
This is identical to the StepUp movement."""

#Display filenames + whether clean or not    
InfoFrameStepDown = Frame(tab4,bg = "DodgerBlue3", bd = 6)
InfoFrameStepDown.pack(fill = BOTH)
SelectFrameStepDown = Frame(tab4,bg = "DodgerBlue3", bd = 6)
SelectFrameStepDown.pack(fill = BOTH)
TrialFrameStepDown1= Frame(tab4,bg = "DodgerBlue3")
TrialFrameStepDown1.pack(expand =1, fill = BOTH)   
TrialFrameStepDown2= Frame(tab4,bg = "DodgerBlue3")
TrialFrameStepDown2.pack(expand =1, fill = BOTH)

FrameTrial1StepDown = Frame(TrialFrameStepDown1, bg = "SlateGray4", bd = 6)
FrameTrial1StepDown.pack()
FrameTrial2StepDown = Frame(TrialFrameStepDown1, bg = "ghost white", bd = 6)
FrameTrial2StepDown.pack()
FrameTrial3StepDown = Frame(TrialFrameStepDown1, bg = "SlateGray4", bd = 6)
FrameTrial3StepDown.pack()
FrameTrial4StepDown = Frame(TrialFrameStepDown1, bg = "ghost white", bd = 6)
FrameTrial4StepDown.pack()
FrameTrial5StepDown = Frame(TrialFrameStepDown1, bg = "SlateGray4", bd = 6)
FrameTrial5StepDown.pack()
FrameTrial6StepDown = Frame(TrialFrameStepDown1, bg = "ghost white", bd = 6)
FrameTrial6StepDown.pack()
FramebottomStepDown = Frame(TrialFrameStepDown2  , bg = "DodgerBlue3", bd = 6)
FramebottomStepDown.pack()


labelStepDown = Label(InfoFrameStepDown, text = "StepDown", bg = "white")
labelStepDown["font"] = myFont
labelStepDown.pack(pady = 10, padx = 20, fill = X)
labelStepDown2 = Label(InfoFrameStepDown, text = "Ensure selected files include a minimum of three clean steps per limb", bg = "white")
labelStepDown2.pack(padx = 20,  side = BOTTOM)

labelbottomStepDown = Label(FramebottomStepDown, height = 1,  bg = "DodgerBlue3")
labelbottomStepDown.pack()

class StepDownlabel():
    def __init__(self, Frame, col1):
        self.Frame = Frame
        self.col1 = col1
    def label(self):
        self.label_file_explorer = Label(self.Frame,  text = "", width = 50, height = 3 ,  fg = "blue" , bg = self.col1) 
        self.label_file_explorer.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
        self.var=StringVar()
        self.var.set(0)
        self.radio_left = Radiobutton(self.Frame, text = "Left", variable = self.var, value="Left")
        self.radio_right = Radiobutton(self.Frame, text ="Right", variable = self.var, value = "Right")
        self.radio_both = Radiobutton(self.Frame, text ="Both", variable = self.var, value = "Both")
        self.radio_left.grid(column = 2,row = 1)
        self.radio_right.grid(column = 3,row = 1)
        self.radio_both.grid(column = 4,row = 1)
        return self.label_file_explorer, self.var
        
label_file_explorer1StepDown,vSD1,  = StepDownlabel(FrameTrial1StepDown, "ghost white").label()
label_file_explorer2StepDown,vSD2,  = StepDownlabel(FrameTrial2StepDown, "gray80").label()
label_file_explorer3StepDown,vSD3,  = StepDownlabel(FrameTrial3StepDown, "ghost white").label()
label_file_explorer4StepDown,vSD4,  = StepDownlabel(FrameTrial4StepDown, "gray80").label()
label_file_explorer5StepDown,vSD5,  = StepDownlabel(FrameTrial5StepDown, "ghost white").label()
label_file_explorer6StepDown,vSD6,  = StepDownlabel(FrameTrial6StepDown, "gray80").label()



StepDown = {}
StepDown["max"]= {}
StepDown["min"] = {}
def browseFilesStepDown(): 
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
        StepDown[TriallistStepDown[i]].update({"Filename": filelistStepDown[i]})
        if i == 0:
            label_file_explorer1StepDown.configure(text="File Opened: "+os.path.basename(filelistStepDown[i]))
        if i == 1:
            label_file_explorer2StepDown.configure(text="File Opened: "+os.path.basename(filelistStepDown[i]))
        if i == 2:
            label_file_explorer3StepDown.configure(text="File Opened: "+os.path.basename(filelistStepDown[i]))
        if i == 3:
            label_file_explorer4StepDown.configure(text="File Opened: "+os.path.basename(filelistStepDown[i]))
        if i == 4:
            label_file_explorer5StepDown.configure(text="File Opened: "+os.path.basename(filelistStepDown[i]))
        if i == 5:
            label_file_explorer6StepDown.configure(text="File Opened: "+os.path.basename(filelistStepDown[i]))

            
def extractintoDictStepDown(filename, TrialNum, Limb):     
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename) # set a filename to the reader
    reader.Update()
    trialacq = reader.GetOutput() # is the btk aquisition object
    def extractvaluesl(trial): #for every variable, the left data is extracted into the dict x
        x=dict();
        for i in range(len(variables)):
            try:
                x[variables[i]]= (trial.GetPoint(leftcolumns[i])).GetValues()
            except:
                pass
        return x
    def extractvaluesr(trial): #for every variable the right data is extracted into dict x
        x=dict();
        for i in range(len(variables)):
            try:
                x[variables[i]]= (trial.GetPoint(rightcolumns[i])).GetValues()
            except:
                pass
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
    va= [vSD1, vSD2, vSD3, vSD4, vSD5, vSD6]
    global TriallistStepDownl 
    global TriallistStepDownr 
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
    def cleanextractStepDown(v, trialnum, filename):
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
            StepDown[TriallistStepDown[i]].update(cleanextractStepDown(va[i], TriallistStepDown[i], filelistStepDown[i]))
            StepDown[TriallistStepDown[i]].update({"Testing Type": "Single Step"})
        if vStrath2.get()==1:
            StepDown[TriallistStepDown[i]].update(cleanextractStepDown(va[i], TriallistStepDown[i], filelistStepDown[i]))
            StepDown[TriallistStepDown[i]].update({"Testing Type": "Strathclyde Steps"})

        
def meanmaxminvalsStepDown(limb, cleantrials, function):
        o={}
        if function == "max":
            fun = max
        if function == "min":
            fun = min
        for move in variables:
            try:
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
            except:
                pass
        return o

def add_max_min_to_dictStepDown():
    StepDown["max"].update({"Left":  meanmaxminvalsStepDown("Left", TriallistStepDownl, "max")})
    StepDown["max"].update({"Right":  meanmaxminvalsStepDown("Right", TriallistStepDownr, "max")})
    StepDown["min"].update({"Left":  meanmaxminvalsStepDown("Left", TriallistStepDownl, "min")})
    StepDown["min"].update({"Right":  meanmaxminvalsStepDown("Right", TriallistStepDownr, "min")})
    for i in range(len(filelistStepDown)):
        filelistStepDown[i]=os.path.basename(filelistStepDown[i])
        StepDown[TriallistStepDown[i]].update({"Filename": filelistStepDown[i]})
    print("Uploaded StepDown Files: " + str(filelistStepDown))
            
button_exploreStepDown = Button(SelectFrameStepDown, text = "Select Trials",  width = 40, bg = "RoyalBlue4",fg= "white",
                          command = lambda : [browseFilesStepDown()])  
button_exploreStepDown.pack(pady=10)
vStrath2 = IntVar()
vStrath2.set(0)
check_strath2 = Checkbutton(SelectFrameStepDown, text ="Check if Strathclyde Stepping Trial", variable = vStrath2)
check_strath2.pack()

def totab5():
    tab_parent.select(tab5)
def checkboxStepDown():  
    sdc.set(1)

 
button_next4 = Button(FramebottomStepDown, bg = "RoyalBlue4",fg = "white", text = "Import Files to System", 
                      command  = lambda:[totab5(),extract_all_StepDown_files(), 
                                          add_max_min_to_dictStepDown(), checkboxStepDown()] )
button_next4.pack(pady=10)

button_skip4 = Button(FramebottomStepDown, fg = "gray", text = "Skip", 
                      command  = lambda:[totab5()])
button_skip4.pack(pady = 10)  


checkboxes(tab4).boxes()

"""Tab 4: STS
Since this is a bilateral movement, only three trials are needed.

"""

#Display filenames + whether clean or not    
InfoFrameSTS = Frame(tab5,bg = "DodgerBlue3", bd = 6)
InfoFrameSTS.pack(fill = BOTH)
SelectFrameSTS = Frame(tab5,bg = "DodgerBlue3", bd = 6)
SelectFrameSTS.pack(fill = BOTH)
TrialFrameSTS1= Frame(tab5,bg = "DodgerBlue3")
TrialFrameSTS1.pack(fill = BOTH)   
TrialFrameSTS2= Frame(tab5,bg = "DodgerBlue3")
TrialFrameSTS2.pack(fill = BOTH, expand  = 1)

FrameTrial1STS = Frame(TrialFrameSTS1, bg = "SlateGray4", bd = 6)
FrameTrial1STS.pack()
FrameTrial2STS = Frame(TrialFrameSTS1, bg = "ghost white", bd = 6)
FrameTrial2STS.pack()
FrameTrial3STS = Frame(TrialFrameSTS1, bg = "SlateGray4", bd = 6)
FrameTrial3STS.pack()
FrameTrial4STS = Frame(TrialFrameSTS1, bg = "ghost white", bd = 6)
FrameTrial4STS.pack()
FrameTrial5STS = Frame(TrialFrameSTS1, bg = "SlateGray4", bd = 6)
FrameTrial5STS.pack()
FrameTrial6STS = Frame(TrialFrameSTS1, bg = "ghost white", bd = 6)
FrameTrial6STS.pack()
FramebottomSTS = Frame(TrialFrameSTS2, bg = "DodgerBlue3", bd = 6)
FramebottomSTS.pack()


labelSTS = Label(InfoFrameSTS, text = "Sit/Stand (STS)", bg = "white")
labelSTS["font"] = myFont
labelSTS.pack(pady = 10, padx = 20, fill = X)

labelbottomSTS = Label(FramebottomSTS, height = 1,  bg = "DodgerBlue3")
labelbottomSTS.pack()

label_file_explorer1STS = Label(FrameTrial1STS,  text = "", width = 50, height = 3 ,  fg = "blue" , bg = "ghost white") 
label_file_explorer1STS.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer2STS = Label(FrameTrial2STS,  text = "", width = 50, height = 3,  fg = "blue", bg = "gray80") 
label_file_explorer2STS.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

label_file_explorer3STS = Label(FrameTrial3STS,  text = "", width = 50, height = 3,  fg = "blue", bg = "ghost white") 
label_file_explorer3STS.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 

"""Instantiate the dictionaries and browse files similar to previous movements"""

STS = {}
STS["StandtoSit"]={}
STS["StandtoSit"]["max"] = {}
STS["StandtoSit"]["min"]={}
STS["SittoStand"] = {}
STS["SittoStand"]["max"] = {}
STS["SittoStand"]["min"]={}

def browseFilesSTS(): 
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
        STS[TriallistSTS[i]].update({"Filename": filelistSTS[i]})
        if i == 0:
            label_file_explorer1STS.configure(text="File Opened: "+os.path.basename(filelistSTS[i]))
        if i == 1:
            label_file_explorer2STS.configure(text="File Opened: "+os.path.basename(filelistSTS[i]))
        if i == 2:
            label_file_explorer3STS.configure(text="File Opened: "+os.path.basename(filelistSTS[i]))

def extractintoDictSTS(filename, TrialNum, Limb):     
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename) # set a filename to the reader
    reader.Update()
    trialacq = reader.GetOutput() # is the btk aquisition object
    def extractvaluesl(trial): #for every variable, the left data is extracted into the dict x
        x=dict();
        for i in range(len(variables)):
            try:
                x[variables[i]]= (trial.GetPoint(leftcolumns[i])).GetValues()
            except:
                pass
        x["C7"] = (trial.GetPoint("C7")).GetValues()
        return x
    def extractvaluesr(trial): #for every variable the right data is extracted into dict x
        x=dict();
        for i in range(len(variables)):
            try:
                x[variables[i]]= (trial.GetPoint(rightcolumns[i])).GetValues()
            except:
                pass
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
    return y


def extract_all_STS_files():
    for i in range(len(TriallistSTS)): 
        STS[TriallistSTS[i]].update(extractintoDictSTS(filelistSTS[i], TriallistSTS[i], "Left"))
        STS[TriallistSTS[i]].update(extractintoDictSTS(filelistSTS[i], TriallistSTS[i], "Right"))
        STS[TriallistSTS[i]].update({"C7 Velocity x": ((np.gradient(STS[TriallistSTS[i]]["Left"]["C7"]["x"])*100).tolist())})



def split_STS():
    for i in range(len(TriallistSTS)): 
        Triallen = len(STS[TriallistSTS[i]]["Left"]["HipAngle"]["x"])
        #The standing motion shouldn't be initiated before 1/3 of the trial
        thirdlen = int(Triallen/3)
        #The sitting motion shouldnt finish before 1/4 of the trial
        quarterlen = int(Triallen/4)
        c7velx= np.array(STS[TriallistSTS[i]]["C7 Velocity x"])
        hipx = np.array(STS[TriallistSTS[i]]["Left"]["HipAngle"]["x"])
        c7z = np.array(STS[TriallistSTS[i]]["Left"]["C7"]["z"])
        
        #when the veloity of the C7 marker exceeds the threshold of 0.m/s (100mm/s)in the anterior (negative) direction
        StartStanding = int((np.where(c7velx[thirdlen:Triallen]<=-100))[0][0]+thirdlen)
        
        #maxC7SitStand is the maximum value in the second half of the full trial (from len/2 to len)
        maxC7SitStand=np.max(c7z[thirdlen:Triallen])
        StopStanding = int((np.where(c7z==maxC7SitStand))[0][0])
        
        #Stand to Sit Initiation Index where the hip angle first breaks 10 degrees
        StartSitting = int((np.where(hipx>10))[0][0])
        
        #Stand to Sit completion index where the c7 velocity is about 0 for at least 0.25s
        stableindices = np.where((c7velx[quarterlen:]<60)&(c7velx[quarterlen:] >-60))[0]
        indices_in_row =[f for f in np.split(stableindices, np.where(np.diff(stableindices)>1)[0]) if len(f)>=25][0]
        StopSitting = int(indices_in_row[1]+quarterlen)
        
        
        STS[TriallistSTS[i]].update({"SitStandCompletion":StopStanding})
        STS[TriallistSTS[i]].update({"SitStandInitiation":StartStanding})
        STS[TriallistSTS[i]].update({"StandSitInitiation":StartSitting})
        STS[TriallistSTS[i]].update({"StandSitCompletion":StopSitting})




def add_moves_to_dict():
    for i in range(len(TriallistSTS)):
        STS["StandtoSit"][TriallistSTS[i]]={}
        for LR in ["Left", "Right"]:
            STS["StandtoSit"][TriallistSTS[i]][LR]={}
            for key in STS[TriallistSTS[i]]["Left"].keys():
                STS["StandtoSit"][TriallistSTS[i]][LR][key]={}
                for axis in ["x", "y", "z"]:
                    STS["StandtoSit"][TriallistSTS[i]][LR][key][axis]=STS[TriallistSTS[i]][LR][key][axis][STS[TriallistSTS[i]]["StandSitInitiation"]:STS[TriallistSTS[i]]["StandSitCompletion"]]
        STS["SittoStand"][TriallistSTS[i]]={}
        for LR in ["Left", "Right"]:
            STS["SittoStand"][TriallistSTS[i]][LR]={}
            for key in STS[TriallistSTS[i]]["Left"].keys():
                STS["SittoStand"][TriallistSTS[i]][LR][key]={}
                for axis in ["x", "y", "z"]:
                    STS["SittoStand"][TriallistSTS[i]][LR][key][axis]=STS[TriallistSTS[i]][LR][key][axis][STS[TriallistSTS[i]]["SitStandInitiation"]:STS[TriallistSTS[i]]["SitStandCompletion"]]
        STS["StandtoSit"][TriallistSTS[i]].update({"Filename": STS[TriallistSTS[i]]["Filename"]})
        STS["SittoStand"][TriallistSTS[i]].update({"Filename": STS[TriallistSTS[i]]["Filename"]})
#Sit to stand approx 135-145 values 
#Stand ot sit 145-155
def meaninterpolate():
    def interpolateSTS(trimdata):
        #x axis point between each point
        incrementSTS = 100/len(trimdata)
        #creates a list of eveny distributed values form 0 to 100 in steps of the increment
        #has same length as cut data
        TimepercentSTS = np.arange(0,100, incrementSTS).tolist()
        #creates an array of point from 0 to x
        STSpercent = np.array(range(100))
        interpolatedSTS = np.interp(STSpercent, TimepercentSTS, trimdata)
        return interpolatedSTS

    for move in ["StandtoSit", "SittoStand"]:
        for T in ["Trial 1", "Trial 2", "Trial 3"]:
            for LR in ["Left","Right"]:
                for key in STS[T][LR].keys():
                    for axis in ["x", "y", "z"]:
                        array = STS[move][T][LR][key]
                        STS[move][T][LR][key] = {
                            "x": interpolateSTS(array["x"]).tolist(),
                            "y": interpolateSTS(array["x"]).tolist(),
                            "z": interpolateSTS(array["z"]).tolist()}
    
    def meanSTS(limb, movement):
        o = {}
        for key in STS[movement]["Trial 1"]["Left"].keys():
            o[key] = {}
            try:
                for axis in["x", "y", "z"]:
                    o[key][axis] = (np.mean((np.array(STS[movement]["Trial 1"][limb][key][axis]),
                                             np.array(STS[movement]["Trial 2"][limb][key][axis]),
                                             np.array(STS[movement]["Trial 3"][limb][key][axis])),
                                             axis = 0)).tolist()
            except:
                pass
        return o

    STS["StandtoSit"]["mean"]={}
    STS["StandtoSit"]["mean"]["Left"]={}
    STS["StandtoSit"]["mean"]["Right"]={}
    STS["StandtoSit"]["mean"]["Left"].update(meanSTS("Left", "StandtoSit"))
    STS["StandtoSit"]["mean"]["Right"].update(meanSTS("Right", "StandtoSit"))
    STS["SittoStand"]["mean"]={}
    STS["SittoStand"]["mean"]["Left"] = {}
    STS["SittoStand"]["mean"]["Right"] = {}
    STS["SittoStand"]["mean"]["Left"].update(meanSTS("Left", "SittoStand"))
    STS["SittoStand"]["mean"]["Right"].update(meanSTS("Right", "SittoStand"))   

def meanmaxminvalsSTS(limb, function, test):
    o={}
    if function == "max":
        fun2 = max
    if function == "min":
        fun2 = min
    for move in (variables+["C7"]):
        try:
            o[move]={}
            for axis in ["x","y","z"]:
                o[move][axis] = (((fun2(STS[test][TriallistSTS[0]][limb][move][axis]))+
                                                          (fun2(STS[test][TriallistSTS[1]][limb][move][axis]))+
                                                          (fun2(STS[test][TriallistSTS[2]][limb][move][axis])))/3)                    
        except:
            pass
    
    return o


def add_max_min_to_dict_STS():
    STS["StandtoSit"]["max"].update({"Left":  meanmaxminvalsSTS("Left", "max", "StandtoSit")})
    STS["StandtoSit"]["min"].update({"Left":  meanmaxminvalsSTS("Left", "min", "StandtoSit")})
    STS["StandtoSit"]["max"].update({"Right":  meanmaxminvalsSTS("Right", "max", "StandtoSit")})
    STS["StandtoSit"]["min"].update({"Right":  meanmaxminvalsSTS("Right", "min", "StandtoSit")})
    
    STS["SittoStand"]["max"].update({"Left":  meanmaxminvalsSTS("Left", "max", "SittoStand")})
    STS["SittoStand"]["min"].update({"Left":  meanmaxminvalsSTS("Left", "min", "SittoStand")})
    STS["SittoStand"]["max"].update({"Right":  meanmaxminvalsSTS("Right", "max", "SittoStand")})
    STS["SittoStand"]["min"].update({"Right":  meanmaxminvalsSTS("Right", "min", "SittoStand")})
    
    for i in range(len(filelistSTS)):
        filelistSTS[i]=os.path.basename(filelistSTS[i])
        STS[TriallistSTS[i]].update({"Filename": filelistSTS[i]})
    print("Uploaded STS Files: " + str(filelistSTS))


           
            
button_exploreSTS = Button(SelectFrameSTS, text = "Select Trials",  width = 40, bg = "RoyalBlue4",fg= "white",
                          command = lambda : [browseFilesSTS()])  
button_exploreSTS.pack(pady=10) 

"""Extract_all_STS_files() uses btk to extract all the variables into the STS dict for each
trial and for in left and right. It also extractt the C7 position variable.

The split_STS() fucntion is used to find the inices where the patient nitiates/completes the
sit to stand movement and the stand to sit movement. These inde values are saved 
The c7 velocity is determined by taking the gradient of the c7 positional data. 

The initiation of the standing motion is when the veloity of the C7 marker exceeds 
the threshold of 0.1m/s (100mm/s)in the anterior (negative) direction. Since this can occur 
in the beginning of the sitting motion, this excludes when this occurs in the first third of
the recording. 

The completion of the standing motion is the maximum c7 positional data value (z axis)
 in the second half of the full trial (from len/2 to len)

The initiation of the sitting motion is where the hip angle first breaks 10 degrees in the x axis

The completion of the siitin motion is where the c7 velocity (x axis) is about 0 for at least 0.25s (25 indices)
"Stable" is taken btween 60 and -60 mm/s.

add_moves_to_dict() uses the index values found previously to cut the data into the standing movement
and the sitting movement and asssign these values to their own subdictionary

add_max_min calculates the max and min of each move, averages them over the three trials and saves them

The data is interpolated and averged out, just like the gait

Again the next and skip values go to the next tab which in this case is back to the first main screen

"""

def totab1():
    tab_parent.select(tab1)
def checkboxSTS():  
    stsc.set(1)


button_next5 = Button(FramebottomSTS, bg = "RoyalBlue4",fg = "white", text = "Import Files to System", 
                      command  = lambda:[extract_all_STS_files(),
                                          split_STS(), add_moves_to_dict(), 
                                          meaninterpolate(),
                                          add_max_min_to_dict_STS(), totab1(), checkboxSTS()])
button_next5.pack(pady = 10)

button_skip5 = Button(FramebottomSTS, fg = "gray", text = "Skip", 
                      command  = lambda:[totab1()])
button_skip5.pack(pady = 10)   
SitStandSit = STS 

checkboxes(tab5).boxes()


"""TABLES
This inputs the variables into the various SQLite tbles within the larger SQLite database"""
def variable():
    global ID, sex, dom_limb, aff_limb, pattype, mon, visit
    ID = vID.get()
    sex = vSex.get()
    dom_limb = vDom.get()
    pattype = vType.get()
    aff_limb = vAffect.get()
    mon = vMonth.get()
    visit = vVisit.get()
    
SQLcolumns = ["Knee_Angle", "Knee_Force", "Knee_Moment", "Knee_Power", 
              "Hip_Angle", "Hip_Force", "Hip_Moment", "Hip_Power", 
              "Ankle_Angle", "Ankle_Force", "Ankle_Moment", "Ankle_Power", 
              "Foot_Progression_Angle", "Pelvis_Angle", "COM", "GRF", "NGRF"]

def enter_Mean_Gait_Table (limb_avl, limb_avr):
    c.execute("""INSERT INTO Mean_Gait_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb, Visit_Number)VALUES (?,?,?,?,?,?,?)""", 
              (ID, dom_limb, pattype, sex, mon, aff_limb, visit))
    for i in range(len(variables)): 
        for axis in ["x", "y", "z"]:
            try:
                c.execute(f"""UPDATE Mean_Gait_Table
                  SET 
                  Left_{SQLcolumns[i]}_{axis} = ?
                  WHERE ID = ? and Visit_Number = ?
                  """,(
                  (str(limb_avl[variables[i]][axis])[1:-1]),
                  ID, visit
                  ))
            except:
                pass
            try:
                c.execute(f"""UPDATE Mean_Gait_Table
                  SET 
                  Right_{SQLcolumns[i]}_{axis} = ?
                  WHERE ID = ? and Visit_Number = ?
                  """,(
                  (str(limb_avr[variables[i]][axis])[1:-1]),
                  ID, visit
                  ))
            except:
                pass
    print("Data added to 'Mean_Gait_Table'")
    
def enter_Gait_extrema ():  
    c.execute("""INSERT INTO Gait_Max_Min_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb, Visit_Number)VALUES (?,?,?,?,?,?,?)""", 
              (ID, dom_limb, pattype, sex, mon, aff_limb, visit))
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
        for i in range(len(variables)): 
            for axis in ["x", "y", "z"]:
                for function in ["max", "min"]:
                    if function=="max":
                        fun = max
                    else:
                        fun = min
                    try:
                        c.execute(f"""UPDATE Gait_Max_Min_Table
                          SET 
                          {function}_Left_{SQLcolumns[i]}_{axis}_{phase} = ?
                          WHERE ID = ? and Visit_Number = ?
                          """,(                          
                          (fun((Gait["Left Average"][variables[i]][axis])[startl:endl])),
                          ID, visit
                          ))
                    except:
                        pass
                    try:
                        c.execute(f"""UPDATE Mean_Gait_Table
                          SET 
                          {function}_Right_{SQLcolumns[i]}_{axis}_{phase} = ?
                          WHERE ID = ? and Visit_Number = ?
                          """,(
                          (fun((Gait["Right Average"][variables[i]][axis])[startl:endl])),
                          ID, visit
                          ))
                    except:
                         pass
    print("Data added to 'Gait_Extrema'")
   
    
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
                  Sex, Month, Affected_Limb, Visit_Number,Filename, 
                  Complete_left_Cycle, Complete_Right_Cycle, 
                  Left_Footstrike_Index, Left_FootOff_Index, 
                  Right_Footstrike_Index, Right_FootOff_Index) 
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", 
                  (ID, dom_limb, pattype, sex, mon, aff_limb, visit,
                    filename, cleanleft, cleanright,
                  (str(Gait[TrialNum]["lfootstrikeFrame"])[1:-1]),
                  (str(Gait[TrialNum]["lfootoffFrame"])[1:-1]),
                  (str(Gait[TrialNum]["rfootstrikeFrame"])[1:-1]),
                  (str(Gait[TrialNum]["rfootoffFrame"])[1:-1])))
        for LR in ["Left", "Right"]:
            for axis in ["x", "y", "z"]:
                for i in range(len(variables)): 
                    try:
                        c.execute(f"""UPDATE Gait_Table
                                  SET 
                                  {LR}_{SQLcolumns[i]}_{axis} = ?
                                  WHERE Filename = ?
                                  """,(
                                  (str(Gait[TrialNum][LR][variables[i]][axis])[1:-1]),
                                  filename
                                  ))
                    except:
                        pass
    print("Data added to 'Gait_Table'")

#Step Up
def enter_StepUp_extrema ():  
    c.execute("""INSERT INTO StepUp_Max_Min_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb, Trial_Type, Visit_Number )VALUES (?,?,?,?,?,?,?,?)""", 
              (ID, dom_limb, pattype, sex, mon, aff_limb, 
               str(StepUp["Trial 1"]["Testing Type"]), visit))
    for LR in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
                for i in range(len(variables)):
                    try:
                        c.execute(f"""UPDATE StepUp_Max_Min_Table
                                  SET 
                                  {function}_{LR}_{SQLcolumns[i]}_{axis} = ?
                                  WHERE ID = ? and Visit_Number =?
                                  """,(
                                  (StepUp[function][LR][variables[i]][axis]),
                                  ID, visit
                                  ))
                    except:
                        pass
    print("Data added to 'StepUp_extrema'")
    
    
def enter_StepUp_Table (numTrials):
    for TrialNum in numTrials:
        filename = StepUp[TrialNum]["Filename"] 
        c.execute("""INSERT INTO StepUp_Table 
                  (ID, Dominant_Limb, Patient_Type, 
                  Sex, Month, Affected_Limb, Filename, Trial_Type, Visit_Number) 
                  VALUES (?,?,?,?,?,?,?,?,?)""", 
                  (ID, dom_limb, pattype, sex, mon, aff_limb, 
                    filename, str(StepUp["Trial 1"]["Testing Type"]), visit))
        for LR in ["Left", "Right"]:
                for axis in ["x", "y", "z"]:
                    for i in range(len(variables)):
                        try:
                            c.execute(f"""UPDATE StepUp_Table
                                      SET 
                                      {LR}_{SQLcolumns[i]}_{axis} = ?
                                      WHERE Filename = ?
                                      """,(
                                      (str(StepUp[TrialNum][LR][variables[i]][axis])[1:-1]),
                                      filename
                                      ))
                        except:
                            pass
    print("Data added to 'StepUp_Table'")


#Step Down
def enter_StepDown_extrema ():  
    c.execute("""INSERT INTO StepDown_Max_Min_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb, Trial_Type, Visit_Number)VALUES (?,?,?,?,?,?,?,?)""", 
              (ID, dom_limb, pattype, sex, mon, aff_limb,
              str(StepDown["Trial 1"]["Testing Type"]), visit))
    for LR in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
                for i in range(len(variables)):
                    try:
                        c.execute(f"""UPDATE StepDown_Max_Min_Table
                                  SET 
                                  {function}_{LR}_{SQLcolumns[i]}_{axis} = ?
                                  WHERE ID = ? and Visit_Number =?
                                  """,(
                                  (StepDown[function][LR][variables[i]][axis]),
                                  ID, visit
                                  ))
                    except:
                        pass
    print("Data added to 'StepDown_extrema'")
             
def enter_StepDown_Table (numTrials):
    for TrialNum in numTrials:
        filename = StepDown[TrialNum]["Filename"] 
        c.execute("""INSERT INTO StepDown_Table 
                  (ID, Dominant_Limb, Patient_Type, 
                  Sex, Month, Affected_Limb, Filename, Trial_Type, Visit_Number) 
                  VALUES (?,?,?,?,?,?,?,?,?)""", 
                  (ID, dom_limb, pattype, sex, mon, aff_limb, 
                    filename, str(StepDown["Trial 1"]["Testing Type"]), visit))
        for LR in ["Left", "Right"]:
                for axis in ["x", "y", "z"]:
                    for i in range(len(variables)):
                        try:
                            c.execute(f"""UPDATE StepDown_Table
                                      SET 
                                      {LR}_{SQLcolumns[i]}_{axis} = ?
                                      WHERE Filename = ?
                                      """,(
                                      (str(StepDown[TrialNum][LR][variables[i]][axis])[1:-1]),
                                      filename
                                      ))
                        except:
                            pass
    print("Data added to 'StepDown_Table'")


#Stand to Sit
def enter_StandtoSit_extrema ():  
    c.execute("""INSERT INTO StandtoSit_Max_Min_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb, Visit_Number)VALUES (?,?,?,?,?,?,?)""", 
              (ID, dom_limb, pattype, sex, mon, aff_limb, visit))
    for LR in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
                for i in range(len(variables+["C7"])):
                    try:
                        c.execute(f"""UPDATE StandtoSit_Max_Min_Table
                                  SET 
                                  {function}_{LR}_{(SQLcolumns+["C7"])[i]}_{axis} = ?
                                  WHERE ID = ? and Visit_Number =?
                                  """,(
                                  (STS["StandtoSit"][function][LR][(variables+["C7"])[i]][axis]),
                                  ID, visit
                                  ))
                    except:
                        pass
    print("Data added to 'StandtoSit_extrema'")

def enter_StandtoSit_Table (numTrials):
    for TrialNum in numTrials:
        filename = STS[TrialNum]["Filename"] 
        c.execute("""INSERT INTO StandtoSit_Table 
                  (ID, Dominant_Limb, Patient_Type, 
                  Sex, Month, Affected_Limb, Filename, Visit_Number) 
                  VALUES (?,?,?,?,?,?,?,?)""", 
                  (ID, dom_limb, pattype, sex, mon, aff_limb, 
                    filename, visit))
        for LR in ["Left", "Right"]:
                for axis in ["x", "y", "z"]:
                    for i in range(len(variables+["C7"])):
                        try:
                            c.execute(f"""UPDATE StandtoSit_Table
                                      SET 
                                      {LR}_{(SQLcolumns+["C7"])[i]}_{axis} = ?
                                      WHERE Filename = ?
                                      """,(
                                      (str(STS["StandtoSit"][TrialNum][LR][(variables+["C7"])[i]][axis])[1:-1]),
                                      filename
                                      ))
                        except:
                            pass
    print("Data added to 'StandtoSit_Table'")

def enter_Mean_StandtoSit_Table (limb_avl, limb_avr):
    c.execute("""INSERT INTO Mean_StandtoSit_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb, Visit_Number)VALUES (?,?,?,?,?,?,?)""", 
              (ID, dom_limb, pattype, sex, mon, aff_limb, visit))
    for i in range(len(variables+["C7"])): 
        for axis in ["x", "y", "z"]:
            for LR in ["Left", "Right"]:
                try:
                    c.execute(f"""UPDATE Mean_StandtoSit_Table
                      SET 
                      {LR}_{(SQLcolumns+["C7"])[i]}_{axis} = ?
                      WHERE ID = ? and Visit_Number = ?
                      """,(
                      (str(STS["StandtoSit"]["mean"][LR][(variables+["C7"])[i]][axis])[1:-1]),
                      ID, visit
                      ))
                except:
                    pass
    print("Data added to 'Mean_StandtoSit_Table'")
    
def enter_SittoStand_extrema ():  
    c.execute("""INSERT INTO SittoStand_Max_Min_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb, Visit_Number)VALUES (?,?,?,?,?,?,?)""", 
              (ID, dom_limb, pattype, sex, mon, aff_limb, visit))
    for LR in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
                for i in range(len(variables+["C7"])):
                    try:
                        c.execute(f"""UPDATE SittoStand_Max_Min_Table
                                  SET 
                                  {function}_{LR}_{(SQLcolumns+["C7"])[i]}_{axis} = ?
                                  WHERE ID = ? and Visit_Number =?
                                  """,(
                                  (STS["SittoStand"][function][LR][(variables+["C7"])[i]][axis]),
                                  ID, visit
                                  ))
                    except:
                        pass
    print("Data added to 'SittoStand_Extrema'")
    
def enter_SittoStand_Table (numTrials):
    for TrialNum in numTrials:
        filename = STS[TrialNum]["Filename"] 
        c.execute("""INSERT INTO SittoStand_Table 
                  (ID, Dominant_Limb, Patient_Type, 
                  Sex, Month, Affected_Limb, Filename, Visit_Number) 
                  VALUES (?,?,?,?,?,?,?,?)""", 
                  (ID, dom_limb, pattype, sex, mon, aff_limb, 
                    filename, visit))
        for LR in ["Left", "Right"]:
                for axis in ["x", "y", "z"]:
                    for i in range(len(variables+["C7"])):
                        try:
                            c.execute(f"""UPDATE SittoStand_Table
                                      SET 
                                      {LR}_{(SQLcolumns+["C7"])[i]}_{axis} = ?
                                      WHERE Filename = ?
                                      """,(
                                      (str(STS["SittoStand"][TrialNum][LR][(variables+["C7"])[i]][axis])[1:-1]),
                                      filename
                                      ))
                        except:
                            pass
    print("Data added to 'SittoStand_Table'")

def enter_Mean_SittoStand_Table ():
    c.execute("""INSERT INTO Mean_SittoStand_Table 
              (ID, Dominant_Limb, Patient_Type, 
              Sex, Month, Affected_Limb, Visit_Number)VALUES (?,?,?,?,?,?,?)""", 
              (ID, dom_limb, pattype, sex, mon, aff_limb, visit))
    for i in range(len(variables+["C7"])): 
        for axis in ["x", "y", "z"]:
            for LR in ["Left", "Right"]:
                try:
                    c.execute(f"""UPDATE Mean_SittoStand_Table
                      SET 
                      {LR}_{(SQLcolumns+["C7"])[i]}_{axis} = ?
                      WHERE ID = ? and Visit_Number = ?
                      """,(
                      (str(STS["SittoStand"]["mean"][LR][(variables+["C7"])[i]][axis])[1:-1]),
                      ID, visit
                      ))
                except:
                    pass
    print("Data added to 'Mean_SittoStand_Table'")

"""The accept button runs all the SWLite functions so if you click cancel the database 
will not be changed in any way. Both buttons will close the window. It also creates a JSON file"""
patient = {}
def writetodict():
    Month = str(vMonth.get()) + " Month(s)"
    patient["ID"] = ID
    patient["Sex"]= sex
    patient["Dominant Limb"] = dom_limb
    patient["Affected Limb"] = aff_limb
    patient["Visit Number"] = visit
    patient["Patient Type"] = pattype
    patient["Months postop"] = mon
    patient["Gait"]= Gait
    patient["StepDown"]= StepDown
    patient["STS"] = STS
    patient["StepUp"]= StepUp
    
        
def close_window():
    root.destroy()
#FRAME 3: CANCEL/ACCEPT
label_save= Label(FrameClose, text = """Once finished selecting all files 
                  and inputting patient data, click "Accept" to update database. 
                  If you've made an error, click "Cancel" and start again """)
label_save.pack(pady = 10)   

buttoncancel = Button(FrameClose, bg ="RoyalBlue4",fg = "white",text = "Cancel", command = lambda: close_window())
buttoncancel.pack(side = RIGHT, anchor = CENTER, padx = 10)

patienttoJSON = patient
def writejson():
    if gc.get() == 1:
        for limb in ["Left","Right"]:
            for axis in ["x","y","z"]:
                for trialnum in TriallistGait:
                    for key in  patienttoJSON["Gait"][trialnum][limb].keys():
                        patienttoJSON["Gait"][trialnum][limb][key][axis]=str(patienttoJSON["Gait"][trialnum][limb][key][axis])[1:-1]
                        patienttoJSON["Gait"]["Left Average"][key][axis] = str(patienttoJSON["Gait"]["Left Average"][key][axis])[1:-1]
                        patienttoJSON["Gait"]["Right Average"][key][axis] = str(patienttoJSON["Gait"]["Right Average"][key][axis])[1:-1]
    if suc.get() == 1:
        for limb in ["Left","Right"]:
            for key in  patienttoJSON["StepUp"]["Trial 1"]["Left"].keys():
                for axis in ["x","y","z"]:
                    for trialnum in TriallistStepUp:
                        try:
                            patienttoJSON["StepUp"][trialnum][limb][key][axis]=str(patienttoJSON["StepUp"][trialnum][limb][key][axis])[1:-1]
                        except:
                            pass
    if sdc.get() == 1:
        for limb in ["Left","Right"]:
            for key in  patienttoJSON["StepDown"]["Trial 1"]["Left"].keys():
                for axis in ["x","y","z"]:
                    for trialnum in TriallistStepDown:
                        try: 
                            patienttoJSON["StepDown"][trialnum][limb][key][axis]=str(patienttoJSON["StepDown"][trialnum][limb][key][axis])[1:-1]
                        except:
                            pass
    if stsc.get() == 1:
        for limb in ["Left","Right"]:
            for key in  patienttoJSON["STS"]["Trial 1"]["Left"].keys():
                for axis in ["x","y","z"]:
                    for trialnum in TriallistSTS:
                        patienttoJSON["STS"]["SittoStand"][trialnum][limb][key][axis]=str(patienttoJSON["STS"]["SittoStand"][trialnum][limb][key][axis])[1:-1]
                        patienttoJSON["STS"]["StandtoSit"][trialnum][limb][key][axis]=str(patienttoJSON["STS"]["StandtoSit"][trialnum][limb][key][axis])[1:-1]
                        patienttoJSON["STS"][trialnum][limb][key][axis]=str(patienttoJSON["STS"][trialnum][limb][key][axis])[1:-1]
                        patienttoJSON["STS"][trialnum][limb][key][axis]=str(patienttoJSON["STS"][trialnum][limb][key][axis])[1:-1]
                        patienttoJSON["STS"][trialnum]["C7 Velocity x"]=str(patienttoJSON["STS"][trialnum]["C7 Velocity x"])[1:-1]
                        
                    patienttoJSON["STS"]["SittoStand"]["mean"]["Left"][key][axis] = str(patienttoJSON["STS"]["SittoStand"]["mean"]["Left"][key][axis])[1:-1]
                    patienttoJSON["STS"]["SittoStand"]["mean"]["Right"][key][axis] = str(patienttoJSON["STS"]["SittoStand"]["mean"]["Right"][key][axis])[1:-1]
                    
                    patienttoJSON["STS"]["StandtoSit"]["mean"]["Left"][key][axis] = str(patienttoJSON["STS"]["StandtoSit"]["mean"]["Left"][key][axis])[1:-1]
                    patienttoJSON["STS"]["StandtoSit"]["mean"]["Right"][key][axis] = str(patienttoJSON["STS"]["StandtoSit"]["mean"]["Right"][key][axis])[1:-1]
    
    name = patient["ID"] + "visit" + str(patient["Visit Number"]) + ".json"
    with open(name, 'w') as f:
        json.dump(patienttoJSON, f, indent = 7) 

def sqlitecommands():
    variable()
    writetodict()
    sqlitecommands
    close_window()
    if gc.get() == 1:
        enter_Mean_Gait_Table(Gait["Left Average"],Gait["Right Average"])
        enter_Gait_extrema(),
        enter_Gait_Table(TriallistGait)
    if suc.get() == 1:
        enter_StepUp_extrema()
        enter_StepUp_Table(TriallistStepUp)
    if sdc.get() ==1:
        enter_StepDown_extrema()
        enter_StepDown_Table(TriallistStepDown)
    if stsc.get() == 1:
        enter_StandtoSit_extrema()
        enter_StandtoSit_Table(TriallistSTS)
        enter_SittoStand_extrema()
        enter_SittoStand_Table(TriallistSTS)
        enter_Mean_SittoStand_Table()
        enter_Mean_StandtoSit_Table(STS["StandtoSit"]["mean"]["Left"],
                                    STS["StandtoSit"]["mean"]["Right"])
    writejson()



buttonaccept = Button(FrameClose, bg ="RoyalBlue4",fg = "white", text = "Accept", command = sqlitecommands)

buttonaccept.pack(side = RIGHT, anchor = CENTER, padx = 10, pady = 20)


"""Tkinter mainloop is run. and finally the SQLite ocnnection is closed"""

root.mainloop()


"""for test purposes"""

def delete():
   c.execute(f"""DELETE FROM {table} WHERE "ID" = "delete test" AND "Visit_Number"= 1""") 
table = "Gait_Table"
#delete()

Tablelist= []
def export_all_tables_to_csv():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = c.fetchall()
    print("Table Names: ")
    for row in rows:
        Tablelist.append(row[0])
        print(row)
    
    for table in Tablelist:
        c.execute(f"""select * from {table}""")
        with open(f"""{table}.csv""", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow([i[0] for i in c.description])
            csv_writer.writerows(c)
        
        dirpath = os.getcwd() + """/{table}.csv"""
        print ("Data exported Successfully into {}".format(dirpath))

export_all_tables_to_csv()

"""Close SQLite Connection"""
conn.commit()
conn.close()     







   



