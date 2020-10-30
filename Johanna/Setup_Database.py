# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:57:25 2020

@author: johan
"""
import json
import sqlite3

# ID = "1234M"
# month = 7
# movement = "Gait"
# filename1 = "file MB 022"
# filename2 = "file MB 024"
# filename3 = "file MB 056"
# filename4 = None
# filename5 = None
# filename6 = None
# cleanleft1 = "No"
# cleanright1 = "No"
# cleanleft2 = "No"
# cleanright2 = "No"
# cleanleft3 = "No"
# cleanright3 = "No"
# cleanleft4 = "No"
# cleanright4 = "No"
# cleanleft5 = "No"
# cleanright5 = "No"
# cleanleft6 = "No"
# cleanright6 = "No"

pattype = "control"
AffectedLimb  = "Left"
DomLimb = "Left"
movement = "Gait"

with open('data1.json') as json_file:
    patient = json.load(json_file)

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('MotionAnalysis10.db')
c=conn.cursor()

def create_patient_data_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Patient_Data
              (ID TEXT PRIMARY KEY, Dominant_Limb TEXT, Patient_Type TEXT, 
              Month TEXT, Affected_Limb TEXT,
              Filename_Gait_Trial_1 TEXT, Filename_Gait_Trial_2 TEXT, Filename_Gait_Trial_3 TEXT,
              Filename_Gait_Trial_4 TEXT,Filename_Gait_Trial_5 TEXT, Filename_Gait_Trial_6 TEXT
              )""")
              #add Filename_STS_Trial_1,.... for different movements
              
def create_Gait_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Gait_Table
              (Filename TEXT PRIMARY KEY, Complete_Left_Cycle TEXT, Complete_Right_Cycle TEXT)""")
              
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
              
                       
create_patient_data_table()
create_Gait_Table()
columns_Gait_Table()



# def enter_patient_data():
#     c.execute("""INSERT INTO Patient_Data
#               (ID, Dominant_Limb, Patient_Type, Month, Affected_Limb,
#               Filename_Gait_Trial_1, Filename_Gait_Trial_2, Filename_Gait_Trial_3,
#               Filename_Gait_Trial_4, Filename_Gait_Trial_5, Filename_Gait_Trial_6)
#               VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
#               (ID, DomLimb, pattype, month, AffectedLimb, 
#                filename1,filename2, filename3, filename4, filename5, filename6))
 
# numTrials = ["Trial 1", "Trial 2", "Trial 3"]
# def enter_Gait_Table ():
#     for TrialNum in numTrials:
#         if TrialNum=="Trial 1":
#             filename = filename1
#             cleanleft = cleanleft1
#             cleanright = cleanright1
#         if TrialNum=="Trial 2":
#             filename = filename2
#             cleanleft = cleanleft2
#             cleanright = cleanright2
#         if TrialNum=="Trial 3":
#             filename = filename3
#             cleanleft = cleanleft3
#             cleanright = cleanright3
#         if TrialNum=="Trial 4":
#             filename = filename4
#             cleanleft = cleanleft4
#             cleanright = cleanright4
#         if TrialNum=="Trial 5":
#             filename = filename5
#             cleanleft = cleanleft5
#             cleanright = cleanright5
#         if TrialNum=="Trial 6":
#             filename = filename6
#             cleanleft = cleanleft6
#             cleanright = cleanright6
         
#         c.execute("""INSERT INTO Gait_Table 
#                   (Filename, Complete_left_Cycle, Complete_Right_Cycle) 
#                   VALUES (?,?,?)""", (filename, cleanleft, cleanright))
#         for LR in ["Left", "Right"]:
#             for axis in ["x", "y", "z"]:
#                 c.execute(f"""UPDATE Gait_Table
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
#                           {LR}_GRF_{axis} =  ?,
#                           {LR}_NGRF_{axis} =  ?,
#                           {LR}_pelvis_Angle_{axis} =  ?,
#                           {LR}_COM_{axis} =  ?
#                           WHERE Filename = ?
#                           """,(
#                           (str(patient["Gait"][TrialNum][LR]["KneeAngle"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["KneeMoment"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["KneeForce"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["KneePower"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["HipAngle"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["HipMoment"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["HipForce"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["HipPower"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["AnkleAngle"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["AnkleMoment"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["AnkleForce"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["AnklePower"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["FootProgressAngle"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["GRF"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["NGRF"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["pelvisAngle"][axis])[1:-1]),
#                           (str(patient["Gait"][TrialNum][LR]["COM"][axis])[1:-1]),
#                           filename
#                           ))
                             
# enter_patient_data()                
# enter_Gait_Table()
# def selectall():
#     c.execute("""SELECT * FROM Gait_Table""")
#     rows = c.fetchall()
#     for row in rows:
#         print(row)

# def selectall2():
#     c.execute("""SELECT * FROM Patient_Data""")
#     lines = c.fetchall()
#     for line in lines:
#         print(line)
        
# selectall()  
# selectall2()

conn.commit()

conn.close()     