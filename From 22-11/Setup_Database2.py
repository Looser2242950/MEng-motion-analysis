

import numpy as np
import sys
import btk
import sqlite3
import json
from tkinter import *
from tkinter import filedialog 
import os.path 





"""Start SQLite Connection""" 
conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('MotionAnalysis14.db')
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
              (Filename TEXT, Complete_Left_Cycle TEXT, Complete_Right_Cycle TEXT,
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
def create_Gait_Max_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Gait_Max_Table
              (Filename TEXT, Limb TEXT, Complete_Cycle TEXT)""")            
def columns_Gait_Max_Table():
    for phase in ["stance", "swing"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Knee_Angle_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Knee_Moment_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Knee_Force_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Knee_Power_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Hip_Angle_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Hip_Moment_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Hip_Force_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Hip_Power_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Ankle_Angle_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Ankle_Moment_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Ankle_Force_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Ankle_Power_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Foot_Progression_Angle_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_GRF_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_NGRF_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_pelvis_Angle_{axis}_{phase} TEXT""")
               c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_COM_{axis}_{phase} TEXT""")      

create_Gait_Max_Table()
columns_Gait_Max_Table()                 
create_patient_data_table()
create_Gait_Table()
columns_Gait_Table()

