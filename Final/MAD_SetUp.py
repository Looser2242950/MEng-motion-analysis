

import numpy as np
import sys
import btk
import sqlite3
import json
from tkinter import *
from tkinter import filedialog 
import os.path 





"""Start SQLite Connection""" 
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('MAD.db')
c=conn.cursor()


def create_Mean_Gait_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Mean_Gait_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
                Sex TEXT, Month TEXT, Affected_Limb TEXT, Visit_Number REAL
                )""")            
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
              c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_Pelvis_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_Gait_Table ADD COLUMN {LR}_COM_{axis} TEXT""")   


def create_Gait_Max_Min_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Gait_Max_Min_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
                Sex TEXT, Month TEXT, Affected_Limb TEXT, Visit_Number REAL)""")            
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
                    c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_Pelvis_Angle_{axis}_{phase} REAL""")
                    c.execute(f"""ALTER TABLE Gait_Max_Min_Table ADD COLUMN {function}_{limb}_COM_{axis}_{phase} REAL""")   

          
def create_Gait_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Gait_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
              Sex TEXT, Month TEXT, Affected_Limb TEXT, Visit_Number REAL,
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
              c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_Pelvis_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Gait_Table ADD COLUMN {LR}_COM_{axis} TEXT""")             


def create_StepUp_Max_Min_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepUp_Max_Min_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
                Sex TEXT, Month TEXT, Affected_Limb TEXT, Trial_Type TEXT, Visit_Number REAL)""")            
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
                c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_Pelvis_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE StepUp_Max_Min_Table ADD COLUMN {function}_{limb}_COM_{axis} REAL""")   

          
def create_StepUp_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepUp_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
              Sex TEXT, Month TEXT, Affected_Limb TEXT, Trial_Type TEXT, 
              Visit_Number REAL, Filename TEXT)""")            
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
              c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_Pelvis_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StepUp_Table ADD COLUMN {LR}_COM_{axis} TEXT""")             

def create_StepDown_Max_Min_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepDown_Max_Min_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
                Sex TEXT, Month TEXT, Affected_Limb TEXT, Trial_Type TEXT, 
                Visit_Number REAL)""")            
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
                c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_Pelvis_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE StepDown_Max_Min_Table ADD COLUMN {function}_{limb}_COM_{axis} REAL""")   

def create_StepDown_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StepDown_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
              Sex TEXT, Month TEXT, Affected_Limb TEXT,Trial_Type TEXT,
              Filename TEXT, Visit_Number REAL)""")            
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
              c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_Pelvis_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StepDown_Table ADD COLUMN {LR}_COM_{axis} TEXT""")             

def create_StandtoSit_Max_Min_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StandtoSit_Max_Min_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
                Sex TEXT, Month TEXT, Affected_Limb TEXT, Visit_Number REAL)""")            
def columns_StandtoSit_Max_Min_Table():
    for limb in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Moment_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Force_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Power_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Moment_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Force_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Power_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Moment_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Force_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Power_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Foot_Progression_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_Pelvis_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_COM_{axis} REAL""")   
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_C7_{axis} REAL""")
                c.execute(f"""ALTER TABLE StandtoSit_Max_Min_Table ADD COLUMN {function}_{limb}_NGRF_{axis} REAL""")

def create_StandtoSit_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS StandtoSit_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
              Sex TEXT, Month TEXT, Affected_Limb TEXT,
              Filename TEXT, Visit_Number REAL)""")            
def columns_StandtoSit_Table():
      for LR in ["Left", "Right"]:
          for axis in ["x", "y", "z"]:
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Knee_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Knee_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Knee_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Knee_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Hip_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Hip_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Hip_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Hip_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Ankle_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Ankle_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Ankle_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Ankle_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Foot_Progression_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_Pelvis_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_COM_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_C7_{axis} TEXT""")
              c.execute(f"""ALTER TABLE StandtoSit_Table ADD COLUMN {LR}_NGRF_{axis} TEXT""")
def create_Mean_StandtoSit_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Mean_StandtoSit_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
                Sex TEXT, Month TEXT, Affected_Limb TEXT, Visit_Number REAL
                )""")            
def columns_Mean_StandtoSit_Table():
      for LR in ["Left", "Right"]:
          for axis in ["x", "y", "z"]:
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Knee_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Knee_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Knee_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Knee_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Hip_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Hip_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Hip_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Hip_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Ankle_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Ankle_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Ankle_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Ankle_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Foot_Progression_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_Pelvis_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_COM_{axis} TEXT""")  
              c.execute(f"""ALTER TABLE Mean_StandtoSit_Table ADD COLUMN {LR}_NGRF_{axis} TEXT""")
def create_SittoStand_Max_Min_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS SittoStand_Max_Min_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
                Sex TEXT, Month TEXT, Affected_Limb TEXT, Visit_Number REAL)""")            
def columns_SittoStand_Max_Min_Table():
    for limb in ["Left", "Right"]:
        for axis in ["x", "y", "z"]:
            for function in ["max", "min"]:
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Moment_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Force_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Knee_Power_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Moment_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Force_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Hip_Power_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Moment_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Force_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Ankle_Power_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Foot_Progression_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_Pelvis_Angle_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_COM_{axis} REAL""")  
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_C7_{axis} REAL""")
                c.execute(f"""ALTER TABLE SittoStand_Max_Min_Table ADD COLUMN {function}_{limb}_NGRF_{axis} REAL""")


def create_SittoStand_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS SittoStand_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
              Sex TEXT, Month TEXT, Affected_Limb TEXT,
              Filename TEXT, Visit_Number REAL)""")            
def columns_SittoStand_Table():
      for LR in ["Left", "Right"]:
          for axis in ["x", "y", "z"]:
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Knee_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Knee_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Knee_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Knee_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Hip_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Hip_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Hip_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Hip_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Ankle_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Ankle_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Ankle_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Ankle_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Foot_Progression_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_Pelvis_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_COM_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_C7_{axis} TEXT""")
              c.execute(f"""ALTER TABLE SittoStand_Table ADD COLUMN {LR}_NGRF_{axis} TEXT""")

def create_Mean_SittoStand_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Mean_SittoStand_Table
              (ID TEXT, Dominant_Limb TEXT, Patient_Type TEXT, 
                Sex TEXT, Month TEXT, Affected_Limb TEXT, Visit_Number REAL
                )""")            
def columns_Mean_SittoStand_Table():
      for LR in ["Left", "Right"]:
          for axis in ["x", "y", "z"]:
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Knee_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Knee_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Knee_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Knee_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Hip_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Hip_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Hip_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Hip_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Ankle_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Ankle_Moment_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Ankle_Force_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Ankle_Power_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Foot_Progression_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_Pelvis_Angle_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_COM_{axis} TEXT""")
              c.execute(f"""ALTER TABLE Mean_SittoStand_Table ADD COLUMN {LR}_NGRF_{axis} TEXT""")


create_Gait_Max_Min_Table()
columns_Gait_Max_Min_Table()
create_Gait_Table()
columns_Gait_Table()
create_Mean_Gait_Table()
columns_Mean_Gait_Table()

create_StepUp_Max_Min_Table()
columns_StepUp_Max_Min_Table()
create_StepUp_Table()
columns_StepUp_Table()

create_StepDown_Max_Min_Table()
columns_StepDown_Max_Min_Table()
create_StepDown_Table()
columns_StepDown_Table()

create_SittoStand_Max_Min_Table()
columns_SittoStand_Max_Min_Table()
create_SittoStand_Table()
columns_SittoStand_Table()
create_Mean_SittoStand_Table()
columns_Mean_SittoStand_Table()


create_StandtoSit_Max_Min_Table()
columns_StandtoSit_Max_Min_Table()
create_StandtoSit_Table()
columns_StandtoSit_Table()
create_Mean_StandtoSit_Table()
columns_Mean_StandtoSit_Table()




def select_all():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = c.fetchall()
    for row in rows:
        print(row)
select_all()
"""Close SQLite Connection"""
conn.commit()
conn.close()     
