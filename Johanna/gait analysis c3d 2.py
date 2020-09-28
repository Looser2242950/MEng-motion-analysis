# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:08:36 2020

@author: johan
"""



import csv
import numpy as np
import matplotlib.pyplot as plt
import sys
import btk
import sqlite3

""" SQLite is initialised and the table is created """
#conn = sqlite3.connect('MotionAnalysis.db')
conn = sqlite3.connect(':memory:')
c=conn.cursor()
def create_max_min_table():
    c.execute("""CREATE TABLE IF NOT EXISTS GaitAnalysis_Max_Min
              (Patient_ID INTEGER, Trial_number INTEGER, Trial_Type TEXT, Trial_Date TEXT, File_name TEXT 
              
              max_knee_left_x REAL, min_knee_left_x REAL,
              max_hip_left_x REAL, min_hip_left_x REAL,
              max_ankle_left_x REAL, min_ankle_left_x REAL, 
              max_knee_right_x REAL, min_knee_right_x REAL,
              max_hip_right_x REAL, min_hip_right_x REAL,
              max_ankle_right_x REAL, min_ankle_right_x REAL
              
              max_knee_left_y REAL, min_knee_left_y REAL,
              max_hip_left_y REAL, min_hip_left_y REAL,
              max_ankle_left_y REAL, min_ankle_left_y REAL, 
              max_knee_right_y REAL, min_knee_right_y REAL,
              max_hip_right_y REAL, min_hip_right_y REAL,
              max_ankle_right_y REAL, min_ankle_right_y REAL
             
              max_knee_left_z REAL, min_knee_left_z REAL,
              max_hip_left_z REAL, min_hip_left_z REAL,
              max_ankle_left_z REAL, min_ankle_left_z REAL, 
              max_knee_right_z REAL, min_knee_right_z REAL,
              max_hip_right_z REAL, min_hip_right_z REAL,
              max_ankle_right_z REAL, min_ankle_right_z REAL
              
              )""")
create_max_min_table()

# patientID = input('Input patient ID number: ')
# while True:
#     limb= str(input('Type "L" if operation on left leg, type "R" if right leg: '))
#     if limb not in ('R', 'L'):
#         print("Not an appropriate choice.")
#     else:
#         break
# trial_type = input('Input "Pre-op", "Post-op" or "Control"')

# trial_date = input('Input trial date in form YYYY/MMM/DD')



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
    COM = trial_number.GetPoint("CentreOfMass")
    COM_values = COM.GetValues() 
#Left Side
#Ankle Values
    lankle = trial_number.GetPoint("LAnkleAngles")
    lankle_values = lankle.GetValues() 
    lankleforce = trial_number.GetPoint("LAnkleForce")
    lankleforce_values = lankleforce.GetValues()
    lankleMoment = trial_number.GetPoint("LAnkleMoment")
    lankleMoment_values = lankleMoment.GetValues()
    lanklePower = trial_number.GetPoint("LAnklePower")
    lanklePower_values = lanklePower.GetValues()

    lFootProgressAngle = trial_number.GetPoint("LFootProgressAngles")
    lFootProgressAngle_values = lFootProgressAngle.GetValues()    

    lGRF = trial_number.GetPoint("LGroundReactionForce")
    lGRF_values = lGRF.GetValues()    

#Hip Values
    lhip = trial_number.GetPoint("LHipAngles")
    lhip_values = lhip.GetValues() 
    lhipforce = trial_number.GetPoint("LHipForce")
    lhipforce_values = lhipforce.GetValues()
    lhipMoment = trial_number.GetPoint("LHipMoment")
    lhipMoment_values = lhipMoment.GetValues()
    lhipPower = trial_number.GetPoint("LHipPower")
    lhipPower_values = lhipPower.GetValues()    

#Knee Values
    lknee = trial_number.GetPoint("LKneeAngles")
    lknee_values = lknee.GetValues() 
    lkneeforce = trial_number.GetPoint("LKneeForce")
    lkneeforce_values = lkneeforce.GetValues()
    lkneeMoment = trial_number.GetPoint("LKneeMoment")
    lkneeMoment_values = lkneeMoment.GetValues()
    lkneePower = trial_number.GetPoint("LKneePower")
    lkneePower_values = lkneePower.GetValues()       
     
    lNGRF = trial_number.GetPoint("LNormalisedGRF")
    lNGRF_values = lNGRF.GetValues()   

    lpelvisAngle = trial_number.GetPoint("LPelvisAngles")
    lpelvisAngle_values = lpelvisAngle.GetValues()   

#Right Side
#Ankle Values
    rankle = trial_number.GetPoint("RAnkleAngles")
    rankle_values = rankle.GetValues() 
    rankleforce = trial_number.GetPoint("RAnkleForce")
    rankleforce_values = rankleforce.GetValues()
    rankleMoment = trial_number.GetPoint("RAnkleMoment")
    rankleMoment_values = rankleMoment.GetValues()
    ranklePower = trial_number.GetPoint("RAnklePower")
    ranklePower_values = ranklePower.GetValues()

    rFootProgressAngle = trial_number.GetPoint("RFootProgressAngles")
    rFootProgressAngle_values = rFootProgressAngle.GetValues()    

    rGRF = trial_number.GetPoint("RGroundReactionForce")
    rGRF_values = rGRF.GetValues()    

#Hip Values
    rhip = trial_number.GetPoint("RHipAngles")
    rhip_values = rhip.GetValues() 
    rhipforce = trial_number.GetPoint("RHipForce")
    rhipforce_values = rhipforce.GetValues()
    rhipMoment = trial_number.GetPoint("RHipMoment")
    rhipMoment_values = rhipMoment.GetValues()
    rhipPower = trial_number.GetPoint("RHipPower")
    rhipPower_values = rhipPower.GetValues()    

#Knee Values
    rknee = trial_number.GetPoint("RKneeAngles")
    rknee_values = rknee.GetValues() 
    rkneeforce = trial_number.GetPoint("RKneeForce")
    rkneeforce_values = rkneeforce.GetValues()
    rkneeMoment = trial_number.GetPoint("RKneeMoment")
    rkneeMoment_values = rkneeMoment.GetValues()
    rkneePower = trial_number.GetPoint("RKneePower")
    rkneePower_values = rkneePower.GetValues()       
       
    rNGRF = trial_number.GetPoint("RNormalisedGRF")
    rNGRF_values = rNGRF.GetValues()   

    rpelvisAngle = trial_number.GetPoint("RPelvisAngles")
    rpelvisAngle_values = rpelvisAngle.GetValues()   

    return (COM_values, 
            lankle_values, lankleforce_values, lankleMoment_values, lanklePower_values, 
            lFootProgressAngle_values, lGRF_values, 
            lhip_values, lhipforce_values, lhipMoment_values, lhipPower_values, 
            lknee_values, lkneeforce_values, lkneeMoment_values, lkneePower_values, 
            lNGRF_values, lpelvisAngle_values, 
            rankle_values, rankleforce_values, rankleMoment_values, ranklePower_values, 
            rFootProgressAngle_values, rGRF_values, 
            rhip_values, rhipforce_values, rhipMoment_values, rhipPower_values, 
            rknee_values, rkneeforce_values, rkneeMoment_values, rkneePower_values, 
            rNGRF_values, rpelvisAngle_values)



reader = btk.btkAcquisitionFileReader()
reader.SetFilename(trial1c3d) # set a filename to the reader
reader.Update()
trial_1 = reader.GetOutput() # is the btk aquisition object

(t1_COM, \
     t1_lankle, t1_lankleforce, t1_lankleMoment, t1_lanklePower, \
     t1_lFootProgressAngle, t1_lGRF, \
     t1_lhip, t1_lhipforce, t1_lhipMoment, t1_lhipPower, \
     t1_lknee, t1_lkneeforce, t1_lkneeMoment, t1_lkneePower, \
     t1_lNGRF, t1_lpelvisAngle, \
     t1_rankle, t1_rankleforce, t1_rankleMoment, t1_ranklePower, \
     t1_rFootProgressAngle, t1_rGRF, \
     t1_rhip, t1_rhipforce, t1_rhipMoment, t1_rhipPower, \
     t1_rknee, t1_rkneeforce, t1_rkneeMoment, t1_rkneePower, \
     t1_rNGRF, t1_rpelvisAngle) = extractvalues(trial_1)

    #find max ankle flexion for heelstrike
t1l_heelstrike = np.amax(t1_lankle[:,0])
print(t1l_heelstrike)
t1_variable_list = t1_lankle[:,0]
T_trial1=[] # Time as percentage gait cycle
n1=len(t1_variable_list)
for i in range (n1):
    T_trial1.append((len(t1_variable_list[0:i])/len(t1_variable_list))*100)
peak_index_t1 = np.where (t1_lankle == t1l_heelstrike)
peak_index_t1= int(peak_index_t1[0])
print(peak_index_t1)
t1_ankle_l=[]
t1_ankle_l[0:len(t1_lankle)-peak_index_t1]=t1_lankle[peak_index_t1:len(t1_lankle)]
t1_ankle_l[len(t1_lankle)-peak_index_t1:len(t1_lankle)] =t1_lankle[0:peak_index_t1]

reader.SetFilename(trial2c3d) 
reader.Update()
trial_2 = reader.GetOutput()
(t2_COM, \
    t2_lankle, t2_lankleforce, t2_lankleMoment, t2_lanklePower, \
    t2_lFootProgressAngle, t2_lGRF, \
    t2_lhip, t2_lhipforce, t2_lhipMoment, t2_lhipPower, \
    t2_lknee, t2_lkneeforce, t2_lkneeMoment, t2_lkneePower, \
    t2_lNGRF, t2_lpelvisAngle, \
    t2_rankle, t2_rankleforce, t2_rankleMoment, t2_ranklePower, \
    t2_rFootProgressAngle, t2_rGRF, \
    t2_rhip, t2_rhipforce, t2_rhipMoment, t2_rhipPower, \
    t2_rknee, t2_rkneeforce, t2_rkneeMoment, t2_rkneePower, \
    t2_rNGRF, t2_rpelvisAngle) = extractvalues(trial_2)

t2l_heelstrike = np.amax(t2_lankle[:,0])
print(t2l_heelstrike)
t2_variable_list = t2_lankle[:,0]
T_trial2=[] # Time as percentage gait cycle
n2=len(t2_variable_list)
for i in range (n2):
    T_trial2.append((len(t2_variable_list[0:i])/len(t2_variable_list))*100)
peak_index_t2 = np.where (t2_lankle == t2l_heelstrike)
peak_index_t2= int(peak_index_t2[0])
print(peak_index_t2)
    
# reader.SetFilename(trial3c3d) 
# reader.Update()
# trial_3 = reader.GetOutput()
# (t3_COM, \
#     t3_lankle, t3_lankleforce, t3_lankleMoment, t3_lanklePower, \
#     t3_lFootProgressAngle, t3_lGRF, \
#     t3_lhip, t3_lhipforce, t3_lhipMoment, t3_lhipPower, \
#     t3_lknee, t3_lkneeforce, t3_lkneeMoment, t3_lkneePower, \
#     t3_lNGRF, t3_lpelvisAngle, \
#     t3_rankle, t3_rankleforce, t3_rankleMoment, t3_ranklePower, \
#     t3_rFootProgressAngle, t3_rGRF, \
#     t3_rhip, t3_rhipforce, t3_rhipMoment, t3_rhipPower, \
#     t3_rknee, t3_rkneeforce, t3_rkneeMoment, t3_rkneePower, \
#     t3_rNGRF, t3_rpelvisAngle) = extractvalues(trial_3)



"""
Use functions for max and min to find values for all variables
"""



def max_min(variable):
    max_x = np.amax(variable[:,0])
    min_x = np.amin(variable[:,0])
    max_x = round(max_x, 3)
    min_x = round(min_x, 3)
    
    max_y = np.amax(variable[:,1])
    min_y = np.amin(variable[:,1])
    max_y = round(max_y, 3)
    min_y = round(min_y, 3)
    
    max_z = np.amax(variable[:,2])
    min_z = np.amin(variable[:,2])
    max_z = round(max_z, 3)
    min_z = round(min_z, 3) 
    return max_x, min_x, max_y, min_y, max_z, min_z

# """Trial 1""" 
# #knee angles
# t1_max_lk_x, t1_min_lk_x, t1_max_lk_y, t1_min_lk_y, t1_max_lk_z, t1_min_lk_z = max_min(t1_lknee) 
# t1_max_rk_x, t1_min_rk_x, t1_max_rk_y, t1_min_rk_y, t1_max_rk_z, t1_min_rk_z = max_min(t1_rknee) 

# t1_max_lkf_x, t1_min_lkf_x, t1_max_lkf_y, t1_min_lkf_y, t1_max_lkf_z, t1_min_lkf_z = max_min(t1_lkneeforce) 
# t1_max_rkf_x, t1_min_rkf_x, t1_max_rkf_y, t1_min_rkf_y, t1_max_rkf_z, t1_min_rkf_z = max_min(t1_rkneeforce) 

# t1_max_lkm_x, t1_min_lkm_x, t1_max_lkm_y, t1_min_lkm_y, t1_max_lkm_z, t1_min_lkm_z = max_min(t1_lkneeMoment) 
# t1_max_rkm_x, t1_min_rkm_x, t1_max_rkm_y, t1_min_rkm_y, t1_max_rkm_z, t1_min_rkm_z = max_min(t1_rkneeMoment) 

# t1_max_lkp_x, t1_min_lkp_x, t1_max_lkp_y, t1_min_lkp_y, t1_max_lkp_z, t1_min_lkp_z = max_min(t1_lkneePower) 
# t1_max_rkp_x, t1_min_rkp_x, t1_max_rkp_y, t1_min_rkp_y, t1_max_rkp_z, t1_min_rkp_z = max_min(t1_rkneePower) 

# #hip angles
# t1_max_lh_x, t1_min_lh_x, t1_max_lh_y, t1_min_lh_y, t1_max_lh_z, t1_min_lh_z = max_min(t1_lhip) 
# t1_max_rh_x, t1_min_rh_x, t1_max_rh_y, t1_min_rh_y, t1_max_rh_z, t1_min_rh_z = max_min(t1_rhip) 

# t1_max_lhf_x, t1_min_lhf_x, t1_max_lhf_y, t1_min_lhf_y, t1_max_lhf_z, t1_min_lhf_z = max_min(t1_lhipforce) 
# t1_max_rhf_x, t1_min_rhf_x, t1_max_rhf_y, t1_min_rhf_y, t1_max_rhf_z, t1_min_rhf_z = max_min(t1_rhipforce) 

# t1_max_lhm_x, t1_min_lhm_x, t1_max_lhm_y, t1_min_lhm_y, t1_max_lhm_z, t1_min_lhm_z = max_min(t1_lhipMoment) 
# t1_max_rhm_x, t1_min_rhm_x, t1_max_rhm_y, t1_min_rhm_y, t1_max_rhm_z, t1_min_rhm_z = max_min(t1_rhipMoment) 

# t1_max_lhp_x, t1_min_lhp_x, t1_max_lhp_y, t1_min_lhp_y, t1_max_lhp_z, t1_min_lhp_z = max_min(t1_lhipPower) 
# t1_max_rhp_x, t1_min_rhp_x, t1_max_rhp_y, t1_min_rhp_y, t1_max_rhp_z, t1_min_rhp_z = max_min(t1_rhipPower) 


# #ankle angles
# t1_max_la_x, t1_min_la_x, t1_max_la_y, t1_min_la_y, t1_max_la_z, t1_min_la_z = max_min(t1_lankle) 
# t1_max_ra_x, t1_min_ra_x, t1_max_ra_y, t1_min_ra_y, t1_max_ra_z, t1_min_ra_z = max_min(t1_rankle) 

# t1_max_laf_x, t1_min_laf_x, t1_max_laf_y, t1_min_laf_y, t1_max_laf_z, t1_min_laf_z = max_min(t1_lankleforce) 
# t1_max_raf_x, t1_min_raf_x, t1_max_raf_y, t1_min_raf_y, t1_max_raf_z, t1_min_raf_z = max_min(t1_rankleforce) 

# t1_max_lam_x, t1_min_lam_x, t1_max_lam_y, t1_min_lam_y, t1_max_lam_z, t1_min_lam_z = max_min(t1_lankleMoment) 
# t1_max_ram_x, t1_min_ram_x, t1_max_ram_y, t1_min_ram_y, t1_max_ram_z, t1_min_ram_z = max_min(t1_rankleMoment) 

# t1_max_lap_x, t1_min_lap_x, t1_max_lap_y, t1_min_lap_y, t1_max_lap_z, t1_min_lap_z = max_min(t1_lanklePower) 
# t1_max_rap_x, t1_min_rap_x, t1_max_rap_y, t1_min_rap_y, t1_max_rap_z, t1_min_rap_z = max_min(t1_ranklePower) 


# #COM
# t1_max_COM_x, t1_min_COM_x, t1_max_COM_y, t1_min_COM_y, t1_max_COM_z, t1_min_COM_z = max_min(t1_COM) 

# #Foot Progression Angle
# t1_max_lFPA_x, t1_min_lFPA_x, t1_max_lFPA_y, t1_min_lFPA_y, t1_max_lFPA_z, t1_min_lFPA_z = max_min(t1_lFootProgressAngle) 
# t1_max_rFPA_x, t1_min_rFPA_x, t1_max_rFPA_y, t1_min_rFPA_y, t1_max_rFPA_z, t1_min_rFPA_z = max_min(t1_rFootProgressAngle) 

# #Ground Reaction Force
# t1_max_lGRF_x, t1_min_lGRF_x, t1_max_lGRF_y, t1_min_lGRF_y, t1_max_lGRF_z, t1_min_lGRF_z = max_min(t1_lGRF) 
# t1_max_rGRF_x, t1_min_rGRF_x, t1_max_rGRF_y, t1_min_rGRF_y, t1_max_rGRF_z, t1_min_rGRF_z = max_min(t1_rGRF) 

# #Normalised Ground Reaction Force
# t1_max_lNGRF_x, t1_min_lNGRF_x, t1_max_lNGRF_y, t1_min_lNGRF_y, t1_max_lNGRF_z, t1_min_lNGRF_z = max_min(t1_lNGRF) 
# t1_max_rNGRF_x, t1_min_rNGRF_x, t1_max_rNGRF_y, t1_min_rNGRF_y, t1_max_rNGRF_z, t1_min_rNGRF_z = max_min(t1_rNGRF) 

# #Pelvis Angle
# t1_max_lpelvis_x, t1_min_lpelvis_x, t1_max_lpelvis_y, t1_min_lpelvis_y, t1_max_lpelvis_z, t1_min_lpelvis_z = max_min(t1_lpelvisAngle) 
# t1_max_rpelvis_x, t1_min_rpelvis_x, t1_max_rpelvis_y, t1_min_rpelvis_y, t1_max_rpelvis_z, t1_min_rpelvis_z = max_min(t1_rpelvisAngle) 


# """Trial 2""" 
# #knee angles
# t2_max_lk_x, t2_min_lk_x, t2_max_lk_y, t2_min_lk_y, t2_max_lk_z, t2_min_lk_z = max_min(t2_lknee) 
# t2_max_rk_x, t2_min_rk_x, t2_max_rk_y, t2_min_rk_y, t2_max_rk_z, t2_min_rk_z = max_min(t2_rknee) 

# t2_max_lkf_x, t2_min_lkf_x, t2_max_lkf_y, t2_min_lkf_y, t2_max_lkf_z, t2_min_lkf_z = max_min(t2_lkneeforce) 
# t2_max_rkf_x, t2_min_rkf_x, t2_max_rkf_y, t2_min_rkf_y, t2_max_rkf_z, t2_min_rkf_z = max_min(t2_rkneeforce) 

# t2_max_lkm_x, t2_min_lkm_x, t2_max_lkm_y, t2_min_lkm_y, t2_max_lkm_z, t2_min_lkm_z = max_min(t2_lkneeMoment) 
# t2_max_rkm_x, t2_min_rkm_x, t2_max_rkm_y, t2_min_rkm_y, t2_max_rkm_z, t2_min_rkm_z = max_min(t2_rkneeMoment) 

# t2_max_lkp_x, t2_min_lkp_x, t2_max_lkp_y, t2_min_lkp_y, t2_max_lkp_z, t2_min_lkp_z = max_min(t2_lkneePower) 
# t2_max_rkp_x, t2_min_rkp_x, t2_max_rkp_y, t2_min_rkp_y, t2_max_rkp_z, t2_min_rkp_z = max_min(t2_rkneePower) 

# #hip angles
# t2_max_lh_x, t2_min_lh_x, t2_max_lh_y, t2_min_lh_y, t2_max_lh_z, t2_min_lh_z = max_min(t2_lhip) 
# t2_max_rh_x, t2_min_rh_x, t2_max_rh_y, t2_min_rh_y, t2_max_rh_z, t2_min_rh_z = max_min(t2_rhip) 

# t2_max_lhf_x, t2_min_lhf_x, t2_max_lhf_y, t2_min_lhf_y, t2_max_lhf_z, t2_min_lhf_z = max_min(t2_lhipforce) 
# t2_max_rhf_x, t2_min_rhf_x, t2_max_rhf_y, t2_min_rhf_y, t2_max_rhf_z, t2_min_rhf_z = max_min(t2_rhipforce) 

# t2_max_lhm_x, t2_min_lhm_x, t2_max_lhm_y, t2_min_lhm_y, t2_max_lhm_z, t2_min_lhm_z = max_min(t2_lhipMoment) 
# t2_max_rhm_x, t2_min_rhm_x, t2_max_rhm_y, t2_min_rhm_y, t2_max_rhm_z, t2_min_rhm_z = max_min(t2_rhipMoment) 

# t2_max_lhp_x, t2_min_lhp_x, t2_max_lhp_y, t2_min_lhp_y, t2_max_lhp_z, t2_min_lhp_z = max_min(t2_lhipPower) 
# t2_max_rhp_x, t2_min_rhp_x, t2_max_rhp_y, t2_min_rhp_y, t2_max_rhp_z, t2_min_rhp_z = max_min(t2_rhipPower) 


# #ankle angles
# t2_max_la_x, t2_min_la_x, t2_max_la_y, t2_min_la_y, t2_max_la_z, t2_min_la_z = max_min(t2_lankle) 
# t2_max_ra_x, t2_min_ra_x, t2_max_ra_y, t2_min_ra_y, t2_max_ra_z, t2_min_ra_z = max_min(t2_rankle) 

# t2_max_laf_x, t2_min_laf_x, t2_max_laf_y, t2_min_laf_y, t2_max_laf_z, t2_min_laf_z = max_min(t2_lankleforce) 
# t2_max_raf_x, t2_min_raf_x, t2_max_raf_y, t2_min_raf_y, t2_max_raf_z, t2_min_raf_z = max_min(t2_rankleforce) 

# t2_max_lam_x, t2_min_lam_x, t2_max_lam_y, t2_min_lam_y, t2_max_lam_z, t2_min_lam_z = max_min(t2_lankleMoment) 
# t2_max_ram_x, t2_min_ram_x, t2_max_ram_y, t2_min_ram_y, t2_max_ram_z, t2_min_ram_z = max_min(t2_rankleMoment) 

# t2_max_lap_x, t2_min_lap_x, t2_max_lap_y, t2_min_lap_y, t2_max_lap_z, t2_min_lap_z = max_min(t2_lanklePower) 
# t2_max_rap_x, t2_min_rap_x, t2_max_rap_y, t2_min_rap_y, t2_max_rap_z, t2_min_rap_z = max_min(t2_ranklePower) 


# #COM
# t2_max_COM_x, t2_min_COM_x, t2_max_COM_y, t2_min_COM_y, t2_max_COM_z, t2_min_COM_z = max_min(t2_COM) 

# #Foot Progression Angle
# t2_max_lFPA_x, t2_min_lFPA_x, t2_max_lFPA_y, t2_min_lFPA_y, t2_max_lFPA_z, t2_min_lFPA_z = max_min(t2_lFootProgressAngle) 
# t2_max_rFPA_x, t2_min_rFPA_x, t2_max_rFPA_y, t2_min_rFPA_y, t2_max_rFPA_z, t2_min_rFPA_z = max_min(t2_rFootProgressAngle) 

# #Ground Reaction Force
# t2_max_lGRF_x, t2_min_lGRF_x, t2_max_lGRF_y, t2_min_lGRF_y, t2_max_lGRF_z, t2_min_lGRF_z = max_min(t2_lGRF) 
# t2_max_rGRF_x, t2_min_rGRF_x, t2_max_rGRF_y, t2_min_rGRF_y, t2_max_rGRF_z, t2_min_rGRF_z = max_min(t2_rGRF) 

# #Normalised Ground Reaction Force
# t2_max_lNGRF_x, t2_min_lNGRF_x, t2_max_lNGRF_y, t2_min_lNGRF_y, t2_max_lNGRF_z, t2_min_lNGRF_z = max_min(t2_lNGRF) 
# t2_max_rNGRF_x, t2_min_rNGRF_x, t2_max_rNGRF_y, t2_min_rNGRF_y, t2_max_rNGRF_z, t2_min_rNGRF_z = max_min(t2_rNGRF) 

# #Pelvis Angle
# t2_max_lpelvis_x, t2_min_lpelvis_x, t2_max_lpelvis_y, t2_min_lpelvis_y, t2_max_lpelvis_z, t2_min_lpelvis_z = max_min(t2_lpelvisAngle) 
# t2_max_rpelvis_x, t2_min_rpelvis_x, t2_max_rpelvis_y, t2_min_rpelvis_y, t2_max_rpelvis_z, t2_min_rpelvis_z = max_min(t2_rpelvisAngle) 


# """Trial 3""" 
# #knee angles
# t3_max_lk_x, t3_min_lk_x, t3_max_lk_y, t3_min_lk_y, t3_max_lk_z, t3_min_lk_z = max_min(t3_lknee) 
# t3_max_rk_x, t3_min_rk_x, t3_max_rk_y, t3_min_rk_y, t3_max_rk_z, t3_min_rk_z = max_min(t3_rknee) 

# t3_max_lkf_x, t3_min_lkf_x, t3_max_lkf_y, t3_min_lkf_y, t3_max_lkf_z, t3_min_lkf_z = max_min(t3_lkneeforce) 
# t3_max_rkf_x, t3_min_rkf_x, t3_max_rkf_y, t3_min_rkf_y, t3_max_rkf_z, t3_min_rkf_z = max_min(t3_rkneeforce) 

# t3_max_lkm_x, t3_min_lkm_x, t3_max_lkm_y, t3_min_lkm_y, t3_max_lkm_z, t3_min_lkm_z = max_min(t3_lkneeMoment) 
# t3_max_rkm_x, t3_min_rkm_x, t3_max_rkm_y, t3_min_rkm_y, t3_max_rkm_z, t3_min_rkm_z = max_min(t3_rkneeMoment) 

# t3_max_lkp_x, t3_min_lkp_x, t3_max_lkp_y, t3_min_lkp_y, t3_max_lkp_z, t3_min_lkp_z = max_min(t3_lkneePower) 
# t3_max_rkp_x, t3_min_rkp_x, t3_max_rkp_y, t3_min_rkp_y, t3_max_rkp_z, t3_min_rkp_z = max_min(t3_rkneePower) 

# #hip angles
# t3_max_lh_x, t3_min_lh_x, t3_max_lh_y, t3_min_lh_y, t3_max_lh_z, t3_min_lh_z = max_min(t3_lhip) 
# t3_max_rh_x, t3_min_rh_x, t3_max_rh_y, t3_min_rh_y, t3_max_rh_z, t3_min_rh_z = max_min(t3_rhip) 

# t3_max_lhf_x, t3_min_lhf_x, t3_max_lhf_y, t3_min_lhf_y, t3_max_lhf_z, t3_min_lhf_z = max_min(t3_lhipforce) 
# t3_max_rhf_x, t3_min_rhf_x, t3_max_rhf_y, t3_min_rhf_y, t3_max_rhf_z, t3_min_rhf_z = max_min(t3_rhipforce) 

# t3_max_lhm_x, t3_min_lhm_x, t3_max_lhm_y, t3_min_lhm_y, t3_max_lhm_z, t3_min_lhm_z = max_min(t3_lhipMoment) 
# t3_max_rhm_x, t3_min_rhm_x, t3_max_rhm_y, t3_min_rhm_y, t3_max_rhm_z, t3_min_rhm_z = max_min(t3_rhipMoment) 

# t3_max_lhp_x, t3_min_lhp_x, t3_max_lhp_y, t3_min_lhp_y, t3_max_lhp_z, t3_min_lhp_z = max_min(t3_lhipPower) 
# t3_max_rhp_x, t3_min_rhp_x, t3_max_rhp_y, t3_min_rhp_y, t3_max_rhp_z, t3_min_rhp_z = max_min(t3_rhipPower) 


# #ankle angles
# t3_max_la_x, t3_min_la_x, t3_max_la_y, t3_min_la_y, t3_max_la_z, t3_min_la_z = max_min(t3_lankle) 
# t3_max_ra_x, t3_min_ra_x, t3_max_ra_y, t3_min_ra_y, t3_max_ra_z, t3_min_ra_z = max_min(t3_rankle) 

# t3_max_laf_x, t3_min_laf_x, t3_max_laf_y, t3_min_laf_y, t3_max_laf_z, t3_min_laf_z = max_min(t3_lankleforce) 
# t3_max_raf_x, t3_min_raf_x, t3_max_raf_y, t3_min_raf_y, t3_max_raf_z, t3_min_raf_z = max_min(t3_rankleforce) 

# t3_max_lam_x, t3_min_lam_x, t3_max_lam_y, t3_min_lam_y, t3_max_lam_z, t3_min_lam_z = max_min(t3_lankleMoment) 
# t3_max_ram_x, t3_min_ram_x, t3_max_ram_y, t3_min_ram_y, t3_max_ram_z, t3_min_ram_z = max_min(t3_rankleMoment) 

# t3_max_lap_x, t3_min_lap_x, t3_max_lap_y, t3_min_lap_y, t3_max_lap_z, t3_min_lap_z = max_min(t3_lanklePower) 
# t3_max_rap_x, t3_min_rap_x, t3_max_rap_y, t3_min_rap_y, t3_max_rap_z, t3_min_rap_z = max_min(t3_ranklePower) 


# #COM
# t3_max_COM_x, t3_min_COM_x, t3_max_COM_y, t3_min_COM_y, t3_max_COM_z, t3_min_COM_z = max_min(t3_COM) 

# #Foot Progression Angle
# t3_max_lFPA_x, t3_min_lFPA_x, t3_max_lFPA_y, t3_min_lFPA_y, t3_max_lFPA_z, t3_min_lFPA_z = max_min(t3_lFootProgressAngle) 
# t3_max_rFPA_x, t3_min_rFPA_x, t3_max_rFPA_y, t3_min_rFPA_y, t3_max_rFPA_z, t3_min_rFPA_z = max_min(t3_rFootProgressAngle) 

# #Ground Reaction Force
# t3_max_lGRF_x, t3_min_lGRF_x, t3_max_lGRF_y, t3_min_lGRF_y, t3_max_lGRF_z, t3_min_lGRF_z = max_min(t3_lGRF) 
# t3_max_rGRF_x, t3_min_rGRF_x, t3_max_rGRF_y, t3_min_rGRF_y, t3_max_rGRF_z, t3_min_rGRF_z = max_min(t3_rGRF) 

# #Normalised Ground Reaction Force
# t3_max_lNGRF_x, t3_min_lNGRF_x, t3_max_lNGRF_y, t3_min_lNGRF_y, t3_max_lNGRF_z, t3_min_lNGRF_z = max_min(t3_lNGRF) 
# t3_max_rNGRF_x, t3_min_rNGRF_x, t3_max_rNGRF_y, t3_min_rNGRF_y, t3_max_rNGRF_z, t3_min_rNGRF_z = max_min(t3_rNGRF) 

# #Pelvis Angle
# t3_max_lpelvis_x, t3_min_lpelvis_x, t3_max_lpelvis_y, t3_min_lpelvis_y, t3_max_lpelvis_z, t3_min_lpelvis_z = max_min(t3_lpelvisAngle) 
# t3_max_rpelvis_x, t3_min_rpelvis_x, t3_max_rpelvis_y, t3_min_rpelvis_y, t3_max_rpelvis_z, t3_min_rpelvis_z = max_min(t3_rpelvisAngle) 

























# def maxangle(knee, hip, ankle):
#     max_knee_x = np.amax(knee[:,0])
#     max_hip_x = np.amax(hip[:,0])
#     max_ankle_x = np.amax(ankle[:,0])
#     max_knee_x = round(max_knee_x, 3)
#     max_hip_x = round(max_hip_x, 3)
#     max_ankle_x = round(max_ankle_x, 3)
    
#     max_knee_y = np.amax(knee[:,1])
#     max_hip_y = np.amax(hip[:,1])
#     max_ankle_y = np.amax(ankle[:,1])
#     max_knee_y = round(max_knee_y, 3)
#     max_hip_y = round(max_hip_y, 3)
#     max_ankle_y = round(max_ankle_y, 3)
    
#     max_knee_z = np.amax(knee[:,2])
#     max_hip_z = np.amax(hip[:,2])
#     max_ankle_z = np.amax(ankle[:,2])
#     max_knee_z = round(max_knee_z, 3)
#     max_hip_z = round(max_hip_z, 3)
#     max_ankle_z = round(max_ankle_z, 3)
#     return max_knee_x, max_hip_x, max_ankle_x, max_knee_y, max_hip_y, max_ankle_y, max_knee_z, max_hip_z, max_ankle_z


# t1_max_lk_x, t1_max_lh_x, t1_max_la_x, t1_max_lk_y, t1_max_lh_y, t1_max_la_y, t1_max_lk_z, t1_max_lh_z, t1_max_la_z = maxangle(t1_lknee, t1_lhip, t1_lankle)
# t1_max_rk_x, t1_max_rh_x, t1_max_ra_x, t1_max_rk_y, t1_max_rh_y, t1_max_ra_y, t1_max_rk_z, t1_max_rh_z, t1_max_ra_z = maxangle(t1_rknee, t1_rhip, t1_rankle)

# t2_max_lk_x, t2_max_lh_x, t2_max_la_x, t2_max_lk_y, t2_max_lh_y, t2_max_la_y, t2_max_lk_z, t2_max_lh_z, t2_max_la_z = maxangle(t2_lknee, t2_lhip, t2_lankle)
# t2_max_rk_x, t2_max_rh_x, t2_max_ra_x, t2_max_rk_y, t2_max_rh_y, t2_max_ra_y, t2_max_rk_z, t2_max_rh_z, t2_max_ra_z = maxangle(t2_rknee, t2_rhip, t2_rankle)

# t3_max_lk_x, t3_max_lh_x, t3_max_la_x, t3_max_lk_y, t3_max_lh_y, t3_max_la_y, t3_max_lk_z, t3_max_lh_z, t3_max_la_z = maxangle(t3_lknee, t3_lhip, t3_lankle)
# t3_max_rk_x, t3_max_rh_x, t3_max_ra_x, t3_max_rk_y, t3_max_rh_y, t3_max_ra_y, t3_max_rk_z, t3_max_rh_z, t3_max_ra_z = maxangle(t3_rknee, t3_rhip, t3_rankle)


# def minangle(knee, hip, ankle):
#     min_knee = np.amin(knee[:,0])
#     min_hip = np.amin(hip[:,0])
#     min_ankle = np.amin(ankle[:,0])
#     min_knee = round(min_knee,3)
#     min_hip = round(min_hip,3)
#     min_ankle = round(min_ankle,3)
#     return min_knee, min_hip, min_ankle

# t1_min_lk, t1_min_lh,t1_min_la = minangle(t1_lknee, t1_lhip, t1_lankle)
# t1_min_rk, t1_min_rh,t1_min_ra = minangle(t1_rknee, t1_rhip, t1_rankle)

# t2_min_lk, t2_min_lh,t2_min_la = minangle(t2_lknee, t2_lhip, t2_lankle)
# t2_min_rk, t2_min_rh,t2_min_ra = minangle(t2_rknee, t2_rhip, t2_rankle)

# t3_min_lk, t3_min_lh,t3_min_la = minangle(t3_lknee, t3_lhip, t3_lankle)
# t3_min_rk, t3_min_rh,t3_min_ra = minangle(t3_rknee, t3_rhip, t3_rankle)
