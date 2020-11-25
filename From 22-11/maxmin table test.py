# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:34:37 2020

@author: johan
"""
import sqlite3
import json

with open('C:/Users/johan/OneDrive/Documents/MEng FYP/From 22-11/MB 022Post-op12.json') as json_file:
    patient = json.load(json_file)
conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('MotionAnalysis14.db')
c=conn.cursor()

def create_Gait_Max_Table():
        c.execute("""CREATE TABLE IF NOT EXISTS Gait_Max_Table
              (Filename TEXT, Limb TEXT, Complete_Cycle TEXT, Phase TEXT)""")            
def columns_Gait_Max_Table():
    for axis in ["x", "y", "z"]:
        for function in ["max", "min"]:
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Knee_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Knee_Moment_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Knee_Force_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Knee_Power_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Hip_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Hip_Moment_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Hip_Force_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Hip_Power_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Ankle_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Ankle_Moment_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Ankle_Force_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Ankle_Power_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_Foot_Progression_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_GRF_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_NGRF_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_pelvis_Angle_{axis} TEXT""")
           c.execute(f"""ALTER TABLE Gait_Max_Table ADD COLUMN {function}_COM_{axis} TEXT""")      
create_Gait_Max_Table()
columns_Gait_Max_Table()

cleanlimblist = []
def enter_Gait_extrema (numTrials):
    #Trial 1: left clean right clean
    #Trial 2: right clean
    #trial 3: left clean
    for TrialNum in numTrials:
        cleanlimblist.clear()
        filename = patient["Gait"][TrialNum]["Filename"]
        if len(patient["Gait"][TrialNum]["lfootstrikeFrame"])>1:
            cleanleft = "Yes"
            cleanlimblist.append("Left")
        else:
            cleanleft = "No"
        if len(patient["Gait"][TrialNum]["rfootstrikeFrame"])>1:
            cleanright = "Yes"
            cleanlimblist.append("Right")
        else:
            cleanright = "No"
        print(cleanlimblist) 
        for LR in cleanlimblist:
            if LR=="Left":
                cleanlimb=cleanleft
            else:
                cleanlimb=cleanright
            for phase in ["stance", "swing"]:
                c.execute("""INSERT INTO Gait_Max_Table 
                          (Filename, Limb, Phase) 
                          VALUES (?,?,?)""", (filename, LR, phase))
#does not include a row for inclmplete cycles                      
                if phase == "stance" and LR == "Left":
                    start = (patient["Gait"][TrialNum]["lfootstrikeFrame"])[0]
                    end = (patient["Gait"][TrialNum]["lfootoffFrame"])[0]
                if phase == "stance" and LR == "Right":
                    start = (patient["Gait"][TrialNum]["rfootstrikeFrame"])[0]
                    end = (patient["Gait"][TrialNum]["rfootoffFrame"])[0]
                if phase == "swing" and LR == "Left":
                    start = (patient["Gait"][TrialNum]["lfootoffFrame"])[0]
                    end = (patient["Gait"][TrialNum]["lfootstrikeFrame"])[1]
                if phase == "swing" and LR == "Right":
                    start = (patient["Gait"][TrialNum]["rfootoffFrame"])[0]
                    end = (patient["Gait"][TrialNum]["rfootstrikeFrame"])[1]
                    
                for axis in ["x", "y", "z"]:
                    for function in ["max", "min"]:
                        if function=="max":
                            fun = max
                        else:
                            fun = min
                        c.execute(f"""UPDATE Gait_Max_Table
                                  SET 
                                  {function}_Knee_Angle_{axis} = ?,
                                  {function}_Knee_Moment_{axis} = ?,
                                  {function}_Knee_Force_{axis} = ?,
                                  {function}_Knee_Power_{axis} = ?,
                                  {function}_Hip_Angle_{axis} = ?,
                                  {function}_Hip_Moment_{axis} = ?,
                                  {function}_Hip_Force_{axis} = ?,
                                  {function}_Hip_Power_{axis} = ?,
                                  {function}_Ankle_Angle_{axis} = ?,
                                  {function}_Ankle_Moment_{axis} = ?,
                                  {function}_Ankle_Force_{axis} = ?,
                                  {function}_Ankle_Power_{axis} =  ?,
                                  {function}_Foot_Progression_Angle_{axis} = ?,
                                  {function}_GRF_{axis} =  ?,
                                  {function}_NGRF_{axis} =  ?,
                                  {function}_pelvis_Angle_{axis} =  ?,
                                  {function}_COM_{axis} =  ?
                                  WHERE Filename = ? and Limb = ? and Phase = ?
                                  """,(
                                  (fun(((patient["Gait"][TrialNum][LR]["KneeAngle"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["KneeMoment"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["KneeForce"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["KneePower"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["HipAngle"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["HipMoment"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["HipForce"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["HipPower"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["AnkleAngle"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["AnkleMoment"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["AnkleForce"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["AnklePower"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["FootProgressAngle"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["GRF"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["NGRF"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["pelvisAngle"][axis])[1:-1])[start: end])),
                                  (fun(((patient["Gait"][TrialNum][LR]["COM"][axis])[1:-1])[start: end])),
                                  filename, LR, phase
                                  ))


numTrialslist= ["Trial 1", "Trial 2", "Trial 3"]
enter_Gait_extrema(numTrialslist)
def selectall():
    c.execute("""SELECT max_Ankle_Angle_x FROM Gait_Max_Table where Limb = "Left" and Phase = "swing" """)
    rows = c.fetchall()
    for row in rows:
        print(row)
selectall()
def select_columns():
    c.execute("SELECT sql FROM sqlite_master WHERE name='Gait_Max_Table'")
    rows = c.fetchall()
    for row in rows:
        print(row)
#select_columns()