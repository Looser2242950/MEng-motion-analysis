# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:25:25 2020

@author: johan
"""


#cd C:\Users\Ordinateur\Documents #Current directory where the CSV file is 
 #Edited version


import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import btk
import sqlite3

""" SQLite is initialised and the table is created """
conn = sqlite3.connect('MotionAnalysis.db')
#conn = sqlite3.connect(':memory:')
c=conn.cursor()
def create_max_min_table():
    c.execute("""CREATE TABLE IF NOT EXISTS GaitAnalysis_Max_Min
              (Patient_ID INTEGER, Trial_number INTEGER, Trial_Type TEXT, 
              max_knee_left REAL, min_knee_left REAL,
              max_hip_left REAL, min_hip_left REAL,
              max_ankle_left REAL, min_ankle_left REAL, 
              max_knee_right REAL, min_knee_right REAL,
              max_hip_right REAL, min_hip_right REAL,
              max_ankle_right REAL, min_ankle_right REAL)""")
create_max_min_table()

def create_vital_info_table():
    c.execute("""CREATE TABLE IF NOT EXISTS VitalData
              (Patient_ID INTEGER, Trial_Type TEXT, limb TEXT,
              av_max_leftk REAL, av_min_leftk REAL, 
              av_max_lefth REAL, av_min_lefth REAL, 
              av_max_lefta REAL, av_min_lefta REAL, 
              av_max_rightk REAL, av_min_rightk REAL,
              av_max_righth REAL, av_min_righth REAL, 
              av_max_righta REAL, av_min_righta REAL)""")
create_vital_info_table()

""" Input important data about patient"""


patientID = input('Input patient ID number: ')
while True:
    limb= str(input('Type "L" if operation on left leg, type "R" if right leg: '))
    if limb not in ('R', 'L'):
        print("Not an appropriate choice.")
    else:
        break
trial_type = input('Input "Pre-op", "Post-op" or "Control"')


"""
File uses data aquired directly from the c3d file using the btk package.

The file names are inputted in in their c3d format. The files are read into trial_1, trial_2 and trial_3

The function is used on each trial to extract the data and save it into new varibales 
for knee, hip and ankle, left and right and for each trial
""" 
trial1c3d = str(input('input file name for Trial 1 (including the .c3d): ') or 'MB 022 Gait 02.c3d')
trial2c3d = str(input('input file name for Trial 2 (including the .c3d): ') or 'MB 022 Gait 04.c3d')
trial3c3d = str(input('input file name for Trial 3 (including the .c3d): ') or 'MB 022 Gait 05.c3d')

def extractvalues(trial_number):
    lknee = trial_number.GetPoint("LKneeAngles")
    lknee_values = lknee.GetValues() 

    lhip = trial_number.GetPoint("LHipAngles")
    lhip_values = lhip.GetValues() 

    lankle = trial_number.GetPoint("LAnkleAngles")
    lankle_values = lankle.GetValues() 
    
    rknee = trial_number.GetPoint("RKneeAngles")
    rknee_values = rknee.GetValues() 
  
    rhip = trial_number.GetPoint("RHipAngles")
    rhip_values = rhip.GetValues() 

    rankle = trial_number.GetPoint("RAnkleAngles")
    rankle_values = rankle.GetValues() 

    return lknee_values, lhip_values, lankle_values, rknee_values, rhip_values, rankle_values


reader = btk.btkAcquisitionFileReader()
reader.SetFilename(trial1c3d) # set a filename to the reader
reader.Update()
trial_1 = reader.GetOutput() # is the btk aquisition object
t1_lknee, t1_lhip, t1_lankle, t1_rknee, t1_rhip, t1_rankle = extractvalues(trial_1) 

reader.SetFilename(trial2c3d) 
reader.Update()
trial_2 = reader.GetOutput()
t2_lknee, t2_lhip, t2_lankle, t2_rknee, t2_rhip, t2_rankle = extractvalues(trial_2) 

reader.SetFilename(trial3c3d) 
reader.Update()
trial_3 = reader.GetOutput()
t3_lknee, t3_lhip, t3_lankle, t3_rknee, t3_rhip, t3_rankle = extractvalues(trial_3) 

"""
Use functions for max and min to find values for all variables
"""


def maxangle(knee, hip, ankle):
    max_knee = np.amax(knee[:,0])
    max_hip = np.amax(hip[:,0])
    max_ankle = np.amax(ankle[:,0])
    max_knee = round(max_knee, 3)
    max_hip = round(max_hip, 3)
    max_ankle = round(max_ankle, 3)
    return max_knee, max_hip, max_ankle

t1_max_lk, t1_max_lh,t1_max_la = maxangle(t1_lknee, t1_lhip, t1_lankle)
t1_max_rk, t1_max_rh,t1_max_ra = maxangle(t1_rknee, t1_rhip, t1_rankle)

t2_max_lk, t2_max_lh,t2_max_la = maxangle(t2_lknee, t2_lhip, t2_lankle)
t2_max_rk, t2_max_rh,t2_max_ra = maxangle(t2_rknee, t2_rhip, t2_rankle)

t3_max_lk, t3_max_lh,t3_max_la = maxangle(t3_lknee, t3_lhip, t3_lankle)
t3_max_rk, t3_max_rh,t3_max_ra = maxangle(t3_rknee, t3_rhip, t3_rankle)

def minangle(knee, hip, ankle):
    min_knee = np.amin(knee[:,0])
    min_hip = np.amin(hip[:,0])
    min_ankle = np.amin(ankle[:,0])
    min_knee = round(min_knee,3)
    min_hip = round(min_hip,3)
    min_ankle = round(min_ankle,3)
    return min_knee, min_hip, min_ankle

t1_min_lk, t1_min_lh,t1_min_la = minangle(t1_lknee, t1_lhip, t1_lankle)
t1_min_rk, t1_min_rh,t1_min_ra = minangle(t1_rknee, t1_rhip, t1_rankle)

t2_min_lk, t2_min_lh,t2_min_la = minangle(t2_lknee, t2_lhip, t2_lankle)
t2_min_rk, t2_min_rh,t2_min_ra = minangle(t2_rknee, t2_rhip, t2_rankle)

t3_min_lk, t3_min_lh,t3_min_la = minangle(t3_lknee, t3_lhip, t3_lankle)
t3_min_rk, t3_min_rh,t3_min_ra = minangle(t3_rknee, t3_rhip, t3_rankle)

av_min_lk = round(np.mean([t1_min_lk, t2_min_lk, t3_min_lk]),3)
av_min_lh = round(np.mean([t1_min_lh, t2_min_lh, t3_min_lh]),3)
av_min_la = round(np.mean([t1_min_la, t2_min_la, t3_min_la]),3)
av_max_lk = round(np.mean([t1_max_lk, t2_max_lk, t3_max_lk]),3)
av_max_lh = round(np.mean([t1_max_lh, t2_max_lh, t3_max_lh]),3)
av_max_la = round(np.mean([t1_max_la, t2_max_la, t3_max_la]),3)

av_min_rk = round(np.mean([t1_min_rk, t2_min_rk, t3_min_rk]),3)
av_min_rh = round(np.mean([t1_min_rh, t2_min_rh, t3_min_rh]),3)
av_min_ra = round(np.mean([t1_min_ra, t2_min_ra, t3_min_ra]),3)
av_max_rk = round(np.mean([t1_max_rk, t2_max_rk, t3_max_rk]),3)
av_max_rh = round(np.mean([t1_max_rh, t2_max_rh, t3_max_rh]),3)
av_max_ra = round(np.mean([t1_max_ra, t2_max_ra, t3_max_ra]),3)

"""
Put into SQLite
"""
   

def enter_max_min(Patient_num, trial_num, trial_type, max_lk, min_lk, max_lh, min_lh, max_la, min_la, max_rk, min_rk, max_rh, min_rh, max_ra, min_ra):
  
    c.execute("""INSERT INTO GaitAnalysis_Max_Min
              (Patient_ID, trial_number, Trial_Type,
              max_knee_left, min_knee_left,
              max_hip_left, min_hip_left,
              max_ankle_left, min_ankle_left, 
              max_knee_right, min_knee_right,
              max_hip_right, min_hip_right,
              max_ankle_right, min_ankle_right) 
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              """,(Patient_num, trial_num, trial_type, max_lk, min_lk, max_lh, min_lh, max_la, min_la, max_rk, min_rk, max_rh, min_rh, max_ra, min_ra))

def enter_averages(patientID, trial_type, limb, av_max_lk, av_min_lk, av_max_lh, av_min_lh, av_max_la, av_min_la, av_max_rk, av_min_rk, av_max_rh, av_min_rh, av_max_ra, av_min_ra):
    c.execute("""INSERT INTO VitalData
              (Patient_ID,Trial_Type, limb,
              av_max_leftk, av_min_leftk, 
              av_max_lefth, av_min_lefth, 
              av_max_lefta,av_min_lefta, 
              av_max_rightk, av_min_rightk,
              av_max_righth, av_min_righth,
              av_max_righta,av_min_righta) 
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
              """, (patientID, trial_type, limb, av_max_lk, av_min_lk, av_max_lh, av_min_lh, av_max_la, av_min_la, av_max_rk, av_min_rk, av_max_rh, av_min_rh, av_max_ra, av_min_ra))

#data_entry()
enter_max_min(patientID, 1, trial_type, t1_max_lk, t1_min_lk, t1_max_lh, t1_min_lh, t1_max_la, t1_min_la, t1_max_rk, t1_min_rk, t1_max_rh, t1_min_rh, t1_max_ra, t1_min_ra)
enter_max_min(patientID, 2, trial_type, t2_max_lk, t2_min_lk, t2_max_lh, t2_min_lh, t2_max_la, t2_min_la, t2_max_rk, t2_min_rk, t2_max_rh, t2_min_rh, t2_max_ra, t2_min_ra)
enter_max_min(patientID, 3, trial_type, t3_max_lk, t3_min_lk, t3_max_lh, t3_min_lh, t3_max_la, t3_min_la, t3_max_rk, t3_min_rk, t3_max_rh, t3_min_rh, t3_max_ra, t3_min_ra)

enter_averages(patientID, trial_type, limb, av_max_lk, av_min_lk, av_max_lh, av_min_lh, av_max_la, av_min_la, av_max_rk, av_min_rk, av_max_rh, av_min_rh, av_max_ra, av_min_ra)

def select_all_from_table():
    c.execute("SELECT * FROM GaitAnalysis_Max_Min")
    rows = c.fetchall()
    for row in rows:
        print(row)
def select_all_from_other_table():
    c.execute("SELECT * FROM VitalData")
    rows = c.fetchall()
    for row in rows:
        print(row)
       
select_all_from_table()  
select_all_from_other_table()

conn.commit()
c.close()
conn.close()
