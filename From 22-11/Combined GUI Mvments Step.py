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


"""STRAHTCLYDE STYLE STEPPING"""

# labelSteppingUp = Label(InfoFrameSteppingUp, text = "OR Select Strathclyde Stepping Trials")
# labelSteppingUp.pack()

# label_file_explorer1SteppingUp = Label(FrameTrial1SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
# label_file_explorer1SteppingUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
# VUp1 = StringVar()
# VUp1.set(0)
# radioleft1 = Radiobutton(FrameTrial1SteppingUp, text="Left",variable= VUp1, value="Left")
# radioleft1.grid(column = 2, row = 1)
# radioright1 = Radiobutton(FrameTrial1SteppingUp, text="Right",variable =VUp1, value="Right")
# radioright1.grid(column = 3, row = 1)
# radioboth1= Radiobutton(FrameTrial1SteppingUp, text="Both",variable =VUp1, value="Noth")
# radioboth1.grid(column = 4, row = 1)

# label_file_explorer2SteppingUp = Label(FrameTrial2SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
# label_file_explorer2SteppingUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
# VUp2 = StringVar()
# VUp2.set(0)
# radioleft2 = Radiobutton(FrameTrial2SteppingUp, text="Left",variable= VUp2, value="Left")
# radioleft2.grid(column = 2, row = 1)
# radioright2 = Radiobutton(FrameTrial2SteppingUp, text="Right",variable =VUp2, value="Right")
# radioright2.grid(column = 3, row = 1)
# radioboth2= Radiobutton(FrameTrial2SteppingUp, text="Both",variable =VUp2, value="Noth")
# radioboth2.grid(column = 4, row = 1)

# label_file_explorer3SteppingUp = Label(FrameTrial3SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
# label_file_explorer3SteppingUp.grid(column = 1, row = 1, columnspan = 1, rowspan = 2) 
# VUp3 = StringVar()
# VUp3.set(0)
# radioleft3 = Radiobutton(FrameTrial3SteppingUp, text="Left",variable= VUp3, value="Left")
# radioleft3.grid(column = 2, row = 1)
# radioright3 = Radiobutton(FrameTrial3SteppingUp, text="Right",variable =VUp3, value="Right")
# radioright3.grid(column = 3, row = 1)
# radioboth3= Radiobutton(FrameTrial3SteppingUp, text="Both",variable =VUp3, value="Noth")
# radioboth3.grid(column = 4, row = 1)

# label_file_explorer4SteppingUp = Label(FrameTrial4SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
# label_file_explorer4SteppingUp.grid(column = 5, row = 1, columnspan = 1, rowspan = 2) 
# VUp4 = StringVar()
# VUp4.set(0)
# radioleft4 = Radiobutton(FrameTrial4SteppingUp, text="Left",variable= VUp4, value="Left")
# radioleft4.grid(column = 6, row = 1)
# radioright4 = Radiobutton(FrameTrial4SteppingUp, text="Right",variable =VUp4, value="Right")
# radioright4.grid(column = 7, row = 1)
# radioboth4= Radiobutton(FrameTrial4SteppingUp, text="Both",variable =VUp4, value="Noth")
# radioboth4.grid(column = 8, row = 1)

# label_file_explorer5SteppingUp = Label(FrameTrial5SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
# label_file_explorer5SteppingUp.grid(column = 5, row = 1, columnspan = 1, rowspan = 2) 
# VUp5 = StringVar()
# VUp5.set(0)
# radioleft5 = Radiobutton(FrameTrial5SteppingUp, text="Left",variable= VUp5, value="Left")
# radioleft5.grid(column = 6, row = 1)
# radioright5 = Radiobutton(FrameTrial5SteppingUp, text="Right",variable =VUp5, value="Right")
# radioright5.grid(column = 7, row = 1)
# radioboth5= Radiobutton(FrameTrial5SteppingUp, text="Both",variable =VUp5, value="Noth")
# radioboth5.grid(column = 8, row = 1)

# label_file_explorer6SteppingUp = Label(FrameTrial6SteppingUp,  text = "", width = 40, height = 2 ,  fg = "blue" , bg = "ghost white") 
# label_file_explorer6SteppingUp.grid(column = 5, row = 1, columnspan = 1, rowspan = 2) 
# VUp6 = StringVar()
# VUp6.set(0)
# radioleft6 = Radiobutton(FrameTrial6SteppingUp, text="Left",variable= VUp6, value="Left")
# radioleft6.grid(column = 6, row = 1)
# radioright6 = Radiobutton(FrameTrial6SteppingUp, text="Right",variable =VUp6, value="Right")
# radioright6.grid(column = 7, row = 1)
# radioboth6= Radiobutton(FrameTrial6SteppingUp, text="Both",variable =VUp6, value="Noth")
# radioboth6.grid(column = 8, row = 1)


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
            print(z.keys())
            z.update(extractintoDictStepUp(filename, trialnum, "Right"))
            print(z.keys())
        return z
    for i in range(len(TriallistStepUp)):    
        print("test")         
        if vStrath.get()==0:
            StepUp[TriallistStepUp[i]].update(cleanextract(va[i], TriallistStepUp[i], filelistStepUp[i]))
            StepUp[TriallistStepUp[i]].update({"Testing Type": "Single Step"})
        if vStrath.get()==1:
            StepUp[TriallistStepUp[i]].update(cleanextract(va[i], TriallistStepUp[i], filelistStepUp[i]))
            StepUp[TriallistStepUp[i]].update({"Testing Type": "Strathclyde Steps"})
va= [vSU1, vSU2, vSU3, vSU4, vSU5, vSU6]
extract_all_StepUp_files() 


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