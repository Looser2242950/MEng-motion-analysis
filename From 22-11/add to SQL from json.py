# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:18:31 2020

@author: johan
"""

import sqlite3
import json

with open('C:/Users/johan/OneDrive/Documents/MEng FYP/From 22-11/573813Pre-op0.json') as json_file:
    patient = json.load(json_file)
conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('MotionAnalysis14.db')
c=conn.cursor()

Month = 2

def create_patient_data_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Patient_Data
              (ID TEXT PRIMARY KEY, Dominant_Limb TEXT, Patient_Type TEXT, 
              Sex TEXT, Month TEXT, Affected_Limb TEXT,
              Filename_Gait_Trial_1 TEXT, Filename_Gait_Trial_2 TEXT, Filename_Gait_Trial_3 TEXT,
              Filename_Gait_Trial_4 TEXT,Filename_Gait_Trial_5 TEXT, Filename_Gait_Trial_6 TEXT,
              Filename_StepUp_Left_Trial_1 TEXT, Filename_StepUp_Left_Trial_2 TEXT, Filename_StepUp_Left_Trial_3 TEXT,
              Filename_StepUp_Right_Trial_1 TEXT,Filename_StepUp_Right_Trial_2 TEXT, Filename_StepUp_Right_Trial_3 TEXT,
              Filename_StepDown_Left_Trial_1 TEXT, Filename_StepDown_Left_Trial_2 TEXT, Filename_StepDown_Left_Trial_3 TEXT,
              Filename_StepDown_Right_Trial_1 TEXT,Filename_StepDown_Right_Trial_2 TEXT, Filename_StepDown_Right_Trial_3 TEXT
              Filename_Ramp_Trial_1 TEXT, Filename_Ramp_Trial_2 TEXT, Filename_Ramp_Trial_3 TEXT,
              Filename_Ramp_Trial_4 TEXT,Filename_Ramp_Trial_5 TEXT, Filename_Ramp_Trial_6 TEXT,
              Filename_STS_Trial_1 TEXT, Filename_STS_Trial_2 TEXT, Filename_STS_Trial_3 TEXT,
              Filename_STS_Trial_4 TEXT,Filename_STS_Trial_5 TEXT, Filename_STS_Trial_6 TEXT)""")
              #add Filename_STS_Trial_1,.... for different movements   
create_patient_data_table()      

def enter_patient_data():
    c.execute("""INSERT INTO Patient_Data
              (ID, Dominant_Limb, Patient_Type, Sex) VALUES (?,?,?,?)""",
              (patient["ID"], patient["Dominant Limb"],patient["Type"],
               patient["Sex"]))
    if patient["Type"]=="Pre-op" or "Post-op":
        c.execute("""UPDATE Patient_Data SET
              Affected_Limb = ?""",(patient["Affected Limb"],))  
    if patient["Type"]=="Post-op":
        c.execute("""UPDATE Patient_Data SET
              Month = ?""",(patient["Post-op"][Month]["Month Post-op"],))  
enter_patient_data()

def enter_filenames_Gait(gait_dict):
    for key in gait_dict.keys():
        Trialnum = key[-1]
        c.execute(f"""UPDATE Patient_Data SET
              Filename_Gait_Trial_{Trialnum} = ?""",(gait_dict[key]["Filename"],))  
              
def enter_filenames_StepUp(stepup_dict):
    for key in stepup_dict["Left"].keys():
        Trialnum = key[-1]
        c.execute(f"""UPDATE Patient_Data SET
              Filename_StepUp_Left_Trial_{Trialnum} = ?""",(stepup_dict["Left"][key]["Filename"],))  
    for key in stepup_dict["Right"].keys():
        Trialnum = key[-1]
        c.execute(f"""UPDATE Patient_Data SET
              Filename_StepUp_Right_Trial_{Trialnum} = ?""",(stepup_dict["Right"][key]["Filename"],))  

def enter_filenames_StepDown(stepdown_dict):
    for key in stepdown_dict["Left"].keys():
        Trialnum = key[-1]
        c.execute(f"""UPDATE Patient_Data SET
              Filename_StepDown_Left_Trial_{Trialnum} = ?""",(stepdown_dict["Left"][key]["Filename"],))  
    for key in stepdown_dict["Right"].keys():
        Trialnum = key[-1]
        c.execute(f"""UPDATE Patient_Data SET
              Filename_StepDown_Right_Trial_{Trialnum} = ?""",(stepdown_dict["Right"][key]["Filename"],))  

def enter_filenames_STS(sts_dict):
    for key in sts_dict.keys():
        Trialnum = key[-1]
        c.execute(f"""UPDATE Patient_Data SET
              Filename_STS_Trial_{Trialnum} = ?""",(sts_dict[key]["Filename"],))  

def enter_filenames_Ramp(ramp_dict):
    for key in ramp_dict.keys():
        Trialnum = key[-1]
        c.execute(f"""UPDATE Patient_Data SET
              Filename_Ramp_Trial_{Trialnum} = ?""",(ramp_dict[key]["Filename"],))  
        
        
enter_filenames_Gait(patient["Pre-op"]["Gait"])      
enter_filenames_StepUp(patient["Pre-op"]["StepUp"])        
#enter_filenames_StepDown(patient["Pre-op"]["StepDown"]) 
#enter_filenames_Gait(patient["Pre-op"]["Ramp"])
#enter_filenames_Gait(patient["Pre-op"]["SitStandSit"])       
    








def create_StepUp_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepUp_Table
              (filename_StepUp TEXT)""")            
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
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_GRF_{axis} TEXT""") 
             c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_COM_{axis} TEXT""") 
create_StepUp_Table()
columns_StepUp_Table()

# def enter_StepUp_Table (stepup_dict):            
#     for LR in ["Left", "Right"]:
#         for key in stepup_dict[LR].keys():
#             Trialnum = key[-1]
#             c.execute("""INSERT INTO StepUp_Table 
#                   (filename_StepUp) 
#                   VALUES (?)""", ((stepup_dict[LR][key]["Filename"])))
#             for axis in ["x", "y", "z"]:
#                 c.execute(f"""UPDATE StepUp_Table
#                           SET 
#                           {LR}_Knee_Angle_{axis} = ?,
#                           {LR}_Knee_Moment_{axis} = ?,
#                           {LR}_Knee_Force_{axis} = ?,
#                           {LR}_Knee_Power_{axis} = ?,
#                           {LR}_Hip_Angle_{axis} = ?,
#                           {LR}_Hip_Moment_{axis} = ?,
#                           {LR}_Hip_Force_{axis} = ?,
#                           {LR}_Hip_Power_{axis} = ?,
#                           {LR}_Ankle_Angle_{axis} = ?,
#                           {LR}_Ankle_Moment_{axis} = ?,
#                           {LR}_Ankle_Force_{axis} = ?,
#                           {LR}_Ankle_Power_{axis} =  ?,
#                           {LR}_Foot_Progression_Angle_{axis} = ?,
#                           {LR}_pelvis_Angle_{axis} =  ?,
#                           {LR}_COM_{axis} =  ?
#                           WHERE filename_StepUp = ?
#                           """,(
#                           (str(stepup_dict[LR][key]["KneeAngle"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["KneeMoment"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["KneeForce"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["KneePower"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["HipAngle"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["HipMoment"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["HipForce"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["HipPower"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["AnkleAngle"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["AnkleMoment"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["AnkleForce"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["AnklePower"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["FootProgressAngle"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["pelvisAngle"][axis])[1:-1]),
#                           (str(stepup_dict[LR][key]["COM"][axis])[1:-1]), 
#                           (stepup_dict[LR][key]["Filename"])
#                           ))

enter_StepUp_Table(patient["Pre-op"]["StepUp"])




def selectall():
    c.execute("""SELECT * FROM StepUp_Table""") 
    rows = c.fetchall()
    for row in rows:
        print(row)

def selectall2():
    c.execute("""SELECT * FROM Patient_Data""")
    lines = c.fetchall()
    for line in lines:
        print(line)
#selectall()
selectall2()

"""Close SQLite Connection"""
conn.commit()
conn.close()     