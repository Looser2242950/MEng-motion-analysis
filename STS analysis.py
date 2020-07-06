cd C:\Users\Ordinateur\Documents #Current directory where the CSV file is 
 
import csv

limb='L' # Definition of the operated limb

# Trial 1

fname_trial1="MB 067 STS 01.csv" # Name of the CSV file "... .csv"

Trial1=[] # Initialisation of list Trial 1 
k = 0 # Initialisation of iterable k 
with open(fname_trial1, "r", newline ='') as f1: 
        reader = csv.reader(f1, delimiter=',') # Read CSV file
        for row in reader:
                temporary_line = []
                if k > 4: # First five lines contain str (=character) :Column ..., MB0...:..., X/Y/Z
                        for element in row:
                                if element != '':  
                                        temporary_line.append(float(element))
                                else:
                                        temporary_line.append(0)
                        if len(temporary_line) > 0:
                                Trial1.append(temporary_line) # Any non-empty and non-zero element is added to the list Trial 1 as a float (=decimal number)
                k+=1

import numpy as np
array_trial1 = np.asarray(Trial1)

vGRF_R_trial1_RD=array_trial1[:,4] #Vertical ground reaction force of the R limb
vGRF_R_trial1=(-1)*vGRF_R_trial1_RD

vGRF_L_trial1_RD=array_trial1[:,13] #Vertical ground reaction force of the L limb
vGRF_L_trial1=(-1)*vGRF_L_trial1_RD

max_vGRF_R_trial1 = np.amax(array_trial1[:,4]) # Peak of R vertical ground reaction force
max_vGRF_L_trial1 = np.amax(array_trial1[:,13]) # Peak of L vertical ground reaction force

time_trial1=[] # Initialisation of list time trial 1
n1=len(vGRF_L_trial1)
i=0 # Initialisation of iterable i
for i in range (n1):
    time_trial1.append(i*0.001) # Time of trial 1

impulse_R_trial1=np.trapz(vGRF_R_trial1, time_trial1) # Determination of R impulse vertical ground reaction force using the trapezoidal rule 
impulse_L_trial1=np.trapz(vGRF_L_trial1, time_trial1) # Determination of L impulse vertical ground reaction force using the trapezoidal rule 

if limb=='L': # Conditional statement based on the operated limb
    Peak_ratio_trial1=max_vGRF_L_trial1/max_vGRF_R_trial1 # Determination of peak vertical ground reaction force ratio for if the operated limb is the left 
    Impulse_ratio_trial1=impulse_L_trial1/impulse_R_trial1 # Determination of impulse vertical ground reaction force ratio for if the operated limb is the left 
else:
    Peak_ratio_trial1=max_vGRF_R_trial1/max_vGRF_L_trial1 # Determination of peak vertical ground reaction force ratio if the operated limb is the right 
    Impulse_ratio_trial1=impulse_R_trial1/impulse_L_trial1 # Determination of impulse vertical ground reaction force ratio for if the operated limb is the right 
    
print("Peak ratio trial 1: ", Peak_ratio_trial1,  " - Impulse ratio trial 1:", Impulse_ratio_trial1)

# Trial 2

fname_trial2="MB 067 STS 02.csv" # Name of the CSV file "... .csv"

Trial2=[] # Initialisation of list Trial 1 
k = 0 # Initialisation of iterable k 
with open(fname_trial2, "r", newline ='') as f2: 
        reader = csv.reader(f2, delimiter=',') # Read CSV file
        for row in reader:
                temporary_line = []
                if k > 4: # First five lines contain str (=character) :Column ..., MB0...:..., X/Y/Z
                        for element in row:
                                if element != '':  
                                        temporary_line.append(float(element))
                                else:
                                        temporary_line.append(0)
                        if len(temporary_line) > 0:
                                Trial2.append(temporary_line) # Any non-empty and non-zero element is added to the list Trial 1 as a float (=decimal number)
                k+=1

import numpy as np
array_trial2 = np.asarray(Trial2)

vGRF_R_trial2_RD=array_trial2[:,4] #Vertical ground reaction force of the R limb
vGRF_R_trial2=(-1)*vGRF_R_trial2_RD

vGRF_L_trial2_RD=array_trial2[:,13] #Vertical ground reaction force of the L limb
vGRF_L_trial2=(-1)*vGRF_L_trial2_RD

max_vGRF_R_trial2 = np.amax(array_trial2[:,4]) # Peak of R vertical ground reaction force
max_vGRF_L_trial2 = np.amax(array_trial2[:,13]) # Peak of L vertical ground reaction force

time_trial2=[] # Initialisation of list time trial 2
n2=len(vGRF_L_trial2)
i=0 # Initialisation of iterable i 
for i in range (n2):
    time_trial2.append(i*0.001) # Time of trial 2

impulse_R_trial2=np.trapz(vGRF_R_trial2, time_trial2) # Determination of R impulse vertical ground reaction force using the trapezoidal rule 
impulse_L_trial2=np.trapz(vGRF_L_trial2, time_trial2) # Determination of R impulse vertical ground reaction force using the trapezoidal rule 

if limb=='L': # Conditional statement based on the operated limb
    Peak_ratio_trial2=max_vGRF_L_trial2/max_vGRF_R_trial2 # Determination of peak vertical ground reaction force ratio for if the operated limb is the left 
    Impulse_ratio_trial2=impulse_L_trial2/impulse_R_trial2 # Determination of impulse vertical ground reaction force ratio for if the operated limb is the left 
else:
    Peak_ratio_trial2=max_vGRF_R_trial2/max_vGRF_L_trial2 # Determination of peak vertical ground reaction force ratio for if the operated limb is the right 
    Impulse_ratio_trial2=impulse_R_trial2/impulse_L_trial2 # Determination of impulse vertical ground reaction force ratio for if the operated limb is the right 
    
print("Peak ratio trial 2: ", Peak_ratio_trial2,  " - Impulse ratio trial 2:", Impulse_ratio_trial2)

# Trial 3

fname_trial3="MB 067 STS 03.csv" # Name of the CSV file "... .csv"

Trial3=[] # Initialisation of list Trial 1 
k = 0 # Initialisation of iterable k 
with open(fname_trial3, "r", newline ='') as f3: 
        reader = csv.reader(f3, delimiter=',') # Read CSV file
        for row in reader:
                temporary_line = []
                if k > 4: # First five lines contain str (=character) :Column ..., MB0...:..., X/Y/Z
                        for element in row:
                                if element != '':  
                                        temporary_line.append(float(element))
                                else:
                                        temporary_line.append(0)
                        if len(temporary_line) > 0:
                                Trial3.append(temporary_line) # Any non-empty and non-zero element is added to the list Trial 1 as a float (=decimal number)
                k+=1

import numpy as np
array_trial3 = np.asarray(Trial3)

vGRF_R_trial3_RD=array_trial3[:,4] #Vertical ground reaction force of the R limb
vGRF_R_trial3=(-1)*vGRF_R_trial3_RD

vGRF_L_trial3_RD=array_trial3[:,13] #Vertical ground reaction force of the L limb
vGRF_L_trial3=(-1)*vGRF_L_trial3_RD

max_vGRF_R_trial3 = np.amax(array_trial3[:,4]) # Peak of R vertical ground reaction force
max_vGRF_L_trial3 = np.amax(array_trial3[:,13]) # Peak of L vertical ground reaction force

time_trial3=[] # Initialisation of list time trial 3
n3=len(vGRF_L_trial3)
i=0 # Initialisation of iterable i 
for i in range (n3):
    time_trial3.append(i*0.001) # Time of trial 3

impulse_R_trial3=np.trapz(vGRF_R_trial3, time_trial3) # Determination of R impulse vertical ground reaction force using the trapezoidal rule 
impulse_L_trial3=np.trapz(vGRF_L_trial3, time_trial3) # Determination of R impulse vertical ground reaction force using the trapezoidal rule 

if limb=='L': # Conditional statement based on the operated limb
    Peak_ratio_trial3=max_vGRF_L_trial3/max_vGRF_R_trial3 # Determination of peak vertical ground reaction force ratio for if the operated limb is the left 
    Impulse_ratio_trial3=impulse_L_trial3/impulse_R_trial3 # Determination of impulse vertical ground reaction force ratio for if the operated limb is the left 
else:
    Peak_ratio_trial3=max_vGRF_R_trial3/max_vGRF_L_trial3 # Determination of peak vertical ground reaction force ratio for if the operated limb is the right 
    Impulse_ratio_trial3=impulse_R_trial3/impulse_L_trial3 # Determination of impulse vertical ground reaction force ratio for if the operated limb is the right 
    
print("Peak ratio trial 3: ", Peak_ratio_trial3,  " - Impulse ratio trial 3:", Impulse_ratio_trial3)

# STS results 

Peak_ratio_vGRF=np.array((Peak_ratio_trial1,Peak_ratio_trial2,Peak_ratio_trial3))
Impulse_ratio=np.array((Impulse_ratio_trial1, Impulse_ratio_trial2, Impulse_ratio_trial3))

print("Peak ratio vGRF: ", "Mean :", np.mean(Peak_ratio_vGRF), "/ SD :", np.std(Peak_ratio_vGRF))
print("Impulse ratio :", "Mean :",  np.mean(Impulse_ratio), "/SD :", np.std(Impulse_ratio))


