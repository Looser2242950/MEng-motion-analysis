# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:43:15 2020

@author: johan
"""

import sqlite3
import json

with open('C:/Users/johan/OneDrive/Documents/MEng FYP/From 22-11/573813Pre-op0.json') as json_file:
    patient = json.load(json_file)
conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('MotionAnalysis14.db')
c=conn.cursor()

def enter_filenames(gait_dict):
    for key in gait_dict.keys():
        Trialnum = key[-1]
        c.execute(f"""UPDATE Patient_Data SET
              Filename_Gait_Trial_{Trialnum} = ?""",(gait_dict[key]["Filename"],))  
        

enter_filenames(patient["Pre-op"]["Gait"])