# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:29:31 2020

@author: johan
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import btk
import sqlite3
import json

from tkinter import *
from tkinter import filedialog 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

"""Inputs from GUI Data
ID = string
AffectedLimb  = int (1=Left, 2=Right, = control)
DomLimb = int (1=Left, 2=Right, 3)
filename1 = String with full path
file1FP = Int (1 = Left, 2 = Right, 3= Both, 4 = Neither)
file1K = Int (0 = No (unticked), 1 = Yes (ticked))
filename2 = String with full path
file2FP = Int (1 = Left, 2 = Right, 3= Both, 4 = Neither)
file2K = Int (0 = No (unticked), 1 = Yes (ticked))
filename3 = String with full path
file3FP = Int (1 = Left, 2 = Right, 3= Both, 4 = Neither)
file3K = Int (0 = No (unticked), 1 = Yes (ticked))
month = String
year = String
pattype = string
"""

ID = 1234
AffectedLimb  = 1
DomLimb =  1
filename1 = 'C:/Users/johan/Documents/MEng FYP/C3d_files/MB 022 Gait 02.c3d'
file1FP = 2
file1K = 1
filename2 = 'C:/Users/johan/Documents/MEng FYP/C3d_files/MB 022 Gait 04.c3d'
file2FP = 3
file2K = 1
filename3 = 'C:/Users/johan/Documents/MEng FYP/C3d_files/MB 022 Gait 05.c3d'
file3FP = 1
file3K = 1
month = "Jan"
year = 2020
pattype = "Control"
datetype = str(pattype) + " " + str(year) + " " + str(month)
print(datetype)

"""Read the C3D file in"""
def extracttodict(trial):
    x = dict();  
    x["Knee"]={}
    x["Hip"]={}
    x["Ankle"]={}
    x["Knee"]["Angle"]= (trial.GetPoint("LKneeAngles")).GetValues()
    x["Knee"]["Force"]= (trial.GetPoint("LKneeForce")).GetValues()
    x["Knee"]["Moment"]= (trial.GetPoint("LKneeMoment")).GetValues()
    x["Knee"]["Power"]= (trial.GetPoint("LKneePower")).GetValues() 
    x["Hip"]["Angle"]= ((trial.GetPoint("LHipAngles")).GetValues())
    x["Hip"]["Force"]= (trial.GetPoint("LHipForce")).GetValues()
    x["Hip"]["Moment"]= (trial.GetPoint("LHipMoment")).GetValues()
    x["Hip"]["Power"]= (trial.GetPoint("LHipPower")).GetValues() 
    x["Ankle"]["Angle"]= (trial.GetPoint("LAnkleAngles")).GetValues()
    x["Ankle"]["Force"]= (trial.GetPoint("LAnkleForce")).GetValues()
    x["Ankle"]["Moment"]= (trial.GetPoint("LAnkleMoment")).GetValues()
    x["Ankle"]["Power"]= (trial.GetPoint("LAnklePower")).GetValues()    
    x["FootProgressAngle"] = (trial.GetPoint("LFootProgressAngles")).GetValues()
    x["GRF"] = (trial.GetPoint("LGroundReactionForce")).GetValues()
    x["NGRF"] = (trial.GetPoint("LNormalisedGRF")).GetValues()
    x["pelvisAngle"] = (trial.GetPoint("LPelvisAngles")).GetValues() 
    x["COM"] = (trial.GetPoint("CentreOfMass")).GetValues()
    return x

#Initialise the Dict
patient = {}
patient[ID] = {}
patient[ID][datetype] = {}

#For loop repeats everything for all three trials
for TrialNum in ["Trial 1", "Trial 2", "Trial 3"]: 
    if TrialNum=="Trial 1":
        filename = filename1
    elif TrialNum == "Trial 2":
        filename = filename2
    elif TrialNum == "Trial 3":
        filename = filename3
    print(filename)  
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(filename) # set a filename to the reader
    reader.Update()
    trialoutput = reader.GetOutput() # is the btk aquisition object

    patient[ID][datetype][TrialNum] ={}
    patient[ID][datetype][TrialNum].update({"Left": extracttodict(trialoutput)})
    patient[ID][datetype][TrialNum].update({"Right": extracttodict(trialoutput)})
    
    #PLOT FULL DATA
    Frames = [*range(len((patient[ID][datetype][TrialNum]["Left"]["Knee"]["Angle"])[:,0]))]
    plt.figure('MB067:Total Knee ROM')
    plt.plot(Frames, (patient[ID][datetype][TrialNum]["Left"]["Knee"]["Angle"])[:,0], label='Full data')
    plt.grid(True)
    plt.title('MB067:Total Knee ROM'+str(filename))
    plt.xlabel('Frames')
    plt.ylabel('Knee ROM (°)')
    plt.legend()
    plt.show()
    
    patient[ID][datetype][TrialNum].update({"startframe":trialoutput.GetFirstFrame()})#first frame of data
    
#instantiate the nested dict to input in the footstrike etc
    patient[ID][datetype][TrialNum].update({"lfootstrikeFrame":[]})
    patient[ID][datetype][TrialNum].update({"rfootstrikeFrame":[]})
    patient[ID][datetype][TrialNum].update({"lfootoffFrame":[]})
    patient[ID][datetype][TrialNum].update({"rfootoffFrame":[]})

    
    for i in range(trialoutput.GetEventNumber()):
        eventnum = trialoutput.GetEvent(i)
        if eventnum.GetLabel()=="Foot Strike":
            if eventnum.GetContext() == "Left":
                patient[ID][datetype][TrialNum]["lfootstrikeFrame"].append(eventnum.GetFrame()-patient[ID][datetype][TrialNum]["startframe"])
            else:
                patient[ID][datetype][TrialNum]["rfootstrikeFrame"].append(eventnum.GetFrame()-patient[ID][datetype][TrialNum]["startframe"])
        if eventnum.GetLabel()=="Foot Off":
            if eventnum.GetContext() == "Left":
                patient[ID][datetype][TrialNum]["lfootoffFrame"].append(eventnum.GetFrame()-patient[ID][datetype][TrialNum]["startframe"])
            else:
                patient[ID][datetype][TrialNum]["rfootoffFrame"].append(eventnum.GetFrame()-patient[ID][datetype][TrialNum]["startframe"])
        print(i)
      
    def cutcycle(footstrike, data):
        footstrike1 = footstrike[0]
        footstrike2 = footstrike[1]
        data1 = (data[footstrike1:footstrike2])
        return data1
    
    if len(patient[ID][datetype][TrialNum]["lfootstrikeFrame"])>1:
        for i in ["Angle", "Force","Moment","Power"]:        
            patient[ID][datetype][TrialNum]["Left"]["Knee"][i] = cutcycle(patient[ID][datetype][TrialNum]["lfootstrikeFrame"], patient[ID][datetype][TrialNum]["Left"]["Knee"][i])
            patient[ID][datetype][TrialNum]["Left"]["Hip"][i] = cutcycle(patient[ID][datetype][TrialNum]["lfootstrikeFrame"], patient[ID][datetype][TrialNum]["Left"]["Hip"][i])
            patient[ID][datetype][TrialNum]["Left"]["Ankle"][i] = cutcycle(patient[ID][datetype][TrialNum]["lfootstrikeFrame"], patient[ID][datetype][TrialNum]["Left"]["Ankle"][i])
    
        patient[ID][datetype][TrialNum]["Left"]["FootProgressAngle"] =cutcycle(patient[ID][datetype][TrialNum]["lfootstrikeFrame"], patient[ID][datetype][TrialNum]["Left"]["FootProgressAngle"])
        patient[ID][datetype][TrialNum]["Left"]["GRF"] =cutcycle(patient[ID][datetype][TrialNum]["lfootstrikeFrame"], patient[ID][datetype][TrialNum]["Left"]["GRF"])
        patient[ID][datetype][TrialNum]["Left"]["NGRF"] =cutcycle(patient[ID][datetype][TrialNum]["lfootstrikeFrame"], patient[ID][datetype][TrialNum]["Left"]["NGRF"])
        patient[ID][datetype][TrialNum]["Left"]["pelvisAngle"] =cutcycle(patient[ID][datetype][TrialNum]["lfootstrikeFrame"], patient[ID][datetype][TrialNum]["Left"]["pelvisAngle"])  
        patient[ID][datetype][TrialNum]["Left"]["COM"] =cutcycle(patient[ID][datetype][TrialNum]["lfootstrikeFrame"], patient[ID][datetype][TrialNum]["Left"]["COM"])
    else:
        print("no full left limb gait cycle")
    if len(patient[ID][datetype][TrialNum]["rfootstrikeFrame"])>1:
        for i in ["Angle", "Force","Moment","Power"]:        
            patient[ID][datetype][TrialNum]["Right"]["Knee"][i] = cutcycle(patient[ID][datetype][TrialNum]["rfootstrikeFrame"], patient[ID][datetype][TrialNum]["Right"]["Knee"][i])
            patient[ID][datetype][TrialNum]["Right"]["Hip"][i] = cutcycle(patient[ID][datetype][TrialNum]["rfootstrikeFrame"], patient[ID][datetype][TrialNum]["Right"]["Hip"][i])
            patient[ID][datetype][TrialNum]["Right"]["Ankle"][i] = cutcycle(patient[ID][datetype][TrialNum]["rfootstrikeFrame"], patient[ID][datetype][TrialNum]["Right"]["Ankle"][i])
    
        patient[ID][datetype][TrialNum]["Right"]["FootProgressAngle"] =cutcycle(patient[ID][datetype][TrialNum]["rfootstrikeFrame"], patient[ID][datetype][TrialNum]["Right"]["FootProgressAngle"])
        patient[ID][datetype][TrialNum]["Right"]["GRF"] =cutcycle(patient[ID][datetype][TrialNum]["rfootstrikeFrame"], patient[ID][datetype][TrialNum]["Right"]["GRF"])
        patient[ID][datetype][TrialNum]["Right"]["NGRF"] =cutcycle(patient[ID][datetype][TrialNum]["rfootstrikeFrame"], patient[ID][datetype][TrialNum]["Right"]["NGRF"])
        patient[ID][datetype][TrialNum]["Right"]["pelvisAngle"] =cutcycle(patient[ID][datetype][TrialNum]["rfootstrikeFrame"], patient[ID][datetype][TrialNum]["Right"]["pelvisAngle"])
        patient[ID][datetype][TrialNum]["Right"]["COM"] =cutcycle(patient[ID][datetype][TrialNum]["rfootstrikeFrame"], patient[ID][datetype][TrialNum]["Right"]["COM"])
    else:
        print("no full right limb gait cycle")    
   
    increment = 100/len((patient[ID][datetype][TrialNum]["Left"]["Knee"]["Angle"])[:,0])
    Timpercent = np.arange(0, 100, increment).tolist()    
    plt.figure('MB067:Total Knee ROM')
    plt.plot(Timpercent, (patient[ID][datetype][TrialNum]["Left"]["Knee"]["Angle"])[:,0], label='Full data')
    plt.grid(True)
    plt.title('MB067:Total Knee ROM')
    plt.xlabel('Frames')
    plt.ylabel('Knee ROM (°)')
    plt.legend()
    plt.show()
    
    for LR in ['Right','Left']:
        for key in patient[ID][datetype][TrialNum][LR].keys():
            if isinstance(patient[ID][datetype][TrialNum][LR][key],dict):
                for key2 in patient[ID][datetype][TrialNum][LR][key].keys():
                    arr = patient[ID][datetype][TrialNum][LR][key][key2]
                    patient[ID][datetype][TrialNum][LR][key][key2] = {
                        'x':arr[:,0],
                        'y':arr[:,1],
                        'z':arr[:,2]
                        }
            else:
                arr = patient[ID][datetype][TrialNum][LR][key]
                patient[ID][datetype][TrialNum][LR][key] = {
                        'x':arr[:,0],
                        'y':arr[:,1],
                        'z':arr[:,2]
                        }
        


# with open('data.json', 'w') as f:
#     json.dump(patient, f, indent = 5)
