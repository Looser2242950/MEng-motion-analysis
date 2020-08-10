#cd C:\Users\Ordinateur\Documents #Current directory where the CSV file is 
 #Edited version


import csv

"""This code is used in the Gait analysis tests"""

#Input data about patient
patientID = input('Input patient ID number: ')
while True:
    limb= str(input('Type "L" if operation on left leg, type "R" if right leg: '))
    if limb not in ('R', 'L'):
        print("Not an appropriate choice.")
    else:
        break
fname_trial1 = str(input('input file name for Trial 1: ') or 'mg1963 levelwalking03a.csv')
fname_trial2 = str(input('input file name for Trial 2: ') or 'mg1963 levelwalking03a.csv')
fname_trial3 = str(input('input file name for Trial 3: ') or 'mg1963 levelwalking03a.csv')

#prints out Patient data
print()
print("Patient ID: ", patientID)
print("Limb operated on:", limb)
print("Data files:",  fname_trial1, fname_trial2, fname_trial3)
print()




#based on input, runs code on either Left or Right side
if limb=='L': # Conditional statement based on the operated limb
        column_ankle = 20 # Left Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee= 113 # Left Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip= 101 # Left Hip Column - 1 /!\ Always check column as missing markers lead to missing data
else:
        column_ankle= 221 # Right Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee= 314 # Right Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip= 302 # Right Hip Column - 1 /!\ Always check column as missing markers lead to missing data
        
#fname_trial1="mg1963 levelwalking03a.csv" # Name of the CSV file "... .csv"

Trial1=[] # Initialisation of list Trial 1 
k = 0 # Initialisation of iterable k 
with open(fname_trial1, "r", newline ='') as f1: 
        reader = csv.reader(f1, delimiter=',') # Read CSV file /!\ Always check delimiter
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
print(array_trial1)
min_value_ankle_trial1 = np.amin(array_trial1[:,column_ankle]) # Min ankle value for trial 1
max_value_ankle_trial1 = np.amax(array_trial1[:,column_ankle]) # Max ankle value for trial 1
ROM_value_ankle_trial1= max_value_ankle_trial1 - min_value_ankle_trial1 # ROM ankle value for trial 1

min_value_knee_trial1 = np.amin(array_trial1[:,column_knee]) # Min knee value for trial 1
max_value_knee_trial1 = np.amax(array_trial1[:,column_knee])  # Max knee value for trial 1
ROM_value_knee_trial1=max_value_knee_trial1-min_value_knee_trial1 # ROM knee value for trial 1

min_value_hip_trial1 = np.amin(array_trial1[:,column_hip]) # Min hip value for trial 1
max_value_hip_trial1 = np.amax(array_trial1[:,column_hip]) # Max hip value for trial 1
ROM_value_hip_trial1= max_value_hip_trial1- min_value_hip_trial1 # ROM hip value for trial 1

print()
print("Ankle trial 1: ")
print("Min: ",min_value_ankle_trial1) 
print("Max: ",max_value_ankle_trial1)
print("ROM", ROM_value_ankle_trial1)
print()

print("Knee trial 1: ")
print("Min: ",min_value_knee_trial1) 
print("Max: ",max_value_knee_trial1)
print("ROM", ROM_value_knee_trial1)
print()

print("Hip trial 1: ")
print("Min: ",min_value_hip_trial1) 
print("Max: ",max_value_hip_trial1)
print("ROM", ROM_value_hip_trial1)
print()


#Trial 2 

# if limb=='L': # Conditional statement based on the operated limb
#         column_ankle_trial2 = 20 # Left Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
#         column_knee_trial2= 113 # Left Knee Column - 1 /!\ Always check column as missing markers lead to missing data
#         column_hip_trial2= 101 # Left Hip Column - 1 /!\ Always check column as missing markers lead to missing data
# else:
#         column_ankle_trial2= 221 # Right Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
#         column_knee_trial2= 314 # Right Knee Column - 1 /!\ Always check column as missing markers lead to missing data
#         column_hip_trial2= 302 # Right Hip Column - 1 /!\ Always check column as missing markers lead to missing data

fname_trial2="mg1963 levelwalking03a.csv" # Name of the CSV file "... .csv"

Trial2=[] # Initialisation of list Trial 2 
k = 0 # Initialisation of iterable k 
with open(fname_trial2, "r", newline ='') as f2: 
        reader = csv.reader(f2, delimiter=',') # Read CSV file /!\ Always check delimiter
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

min_value_ankle_trial2 = np.amin(array_trial2[:,column_ankle]) # Min ankle value for trial 2
max_value_ankle_trial2 = np.amax(array_trial2[:,column_ankle]) # Max ankle value for trial 2
ROM_value_ankle_trial2= max_value_ankle_trial2 - min_value_ankle_trial2 # ROM ankle value for trial 2

min_value_knee_trial2 = np.amin(array_trial2[:,column_knee]) # Min knee value for trial 2
max_value_knee_trial2 = np.amax(array_trial2[:,column_knee])  # Max knee value for trial 2
ROM_value_knee_trial2=max_value_knee_trial2-min_value_knee_trial2 # ROM knee value for trial 2

min_value_hip_trial2 = np.amin(array_trial2[:,column_hip]) # Min hip value for trial 2
max_value_hip_trial2 = np.amax(array_trial2[:,column_hip]) # Max hip value for trial 2
ROM_value_hip_trial2= max_value_hip_trial2- min_value_hip_trial2 # ROM hip value for trial 2


print()
print("Ankle trial 2: ")
print("Min: ",min_value_ankle_trial2) 
print("Max: ",max_value_ankle_trial2)
print("ROM", ROM_value_ankle_trial2)
print()

print("Knee trial 2: ")
print("Min: ",min_value_knee_trial2) 
print("Max: ",max_value_knee_trial2)
print("ROM", ROM_value_knee_trial2)
print()

print("Hip trial 2: ")
print("Min: ",min_value_hip_trial2) 
print("Max: ",max_value_hip_trial2)
print("ROM", ROM_value_hip_trial2)
print()

# Trial 3 

# if limb=='L': # Conditional statement based on the operated limb
#         column_ankle_trial3 = 20 # Left Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
#         column_knee_trial3= 113 # Left Knee Column - 1 /!\ Always check column as missing markers lead to missing data
#         column_hip_trial3= 101 # Left Hip Column - 1 /!\ Always check column as missing markers lead to missing data
# else:
#         column_ankle_trial3= 221 # Right Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
#         column_knee_trial3= 314 # Right Knee Column - 1 /!\ Always check column as missing markers lead to missing data
#         column_hip_trial3= 302 # Right Hip Column - 1 /!\ Always check column as missing markers lead to missing data

fname_trial3="mg1963 levelwalking03a.csv" # Name of the CSV file "... .csv"

Trial3=[] # Initialisation of list Trial 3
k = 0 # Initialisation of iterable k 
with open(fname_trial3, "r", newline ='') as f3: 
        reader = csv.reader(f3, delimiter=',') # Read CSV file /!\ Always check delimiter
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

min_value_ankle_trial3 = np.amin(array_trial3[:,column_ankle]) # Min ankle value for trial 3
max_value_ankle_trial3 = np.amax(array_trial3[:,column_ankle]) # Max ankle value for trial 3
ROM_value_ankle_trial3= max_value_ankle_trial3 - min_value_ankle_trial3 # ROM ankle value for trial 3

min_value_knee_trial3 = np.amin(array_trial3[:,column_knee]) # Min knee value for trial 3
max_value_knee_trial3 = np.amax(array_trial3[:,column_knee])  # Max knee value for trial 3
ROM_value_knee_trial3=max_value_knee_trial3-min_value_knee_trial3 # ROM knee value for trial 3

min_value_hip_trial3 = np.amin(array_trial3[:,column_hip]) # Min hip value for trial 3
max_value_hip_trial3 = np.amax(array_trial3[:,column_hip]) # Max hip value for trial 3
ROM_value_hip_trial3= max_value_hip_trial3- min_value_hip_trial3 # ROM hip value for trial 3

print()
print("Ankle trial 3: ")
print("Min: ",min_value_ankle_trial3) 
print("Max: ",max_value_ankle_trial3)
print("ROM", ROM_value_ankle_trial3)
print()

print("Knee trial 3: ")
print("Min: ",min_value_knee_trial3) 
print("Max: ",max_value_knee_trial3)
print("ROM", ROM_value_knee_trial3)
print()

print("Hip trial 3: ")
print("Min: ",min_value_hip_trial3) 
print("Max: ",max_value_hip_trial3)
print("ROM", ROM_value_hip_trial3)
print()


# Gait results 

min_ankle=np.array((min_value_ankle_trial1, min_value_ankle_trial2, min_value_ankle_trial3))
max_ankle=np.array((max_value_ankle_trial1, max_value_ankle_trial2,max_value_ankle_trial3))
ROM_ankle=np.array((ROM_value_ankle_trial1,ROM_value_ankle_trial2, ROM_value_ankle_trial3))

min_knee=np.array((min_value_knee_trial1, min_value_knee_trial2, min_value_knee_trial3))
max_knee=np.array((max_value_knee_trial1, max_value_knee_trial2,max_value_knee_trial3))
ROM_knee=np.array((ROM_value_knee_trial1,ROM_value_knee_trial2, ROM_value_knee_trial3))

min_hip=np.array((min_value_hip_trial1, min_value_hip_trial2, min_value_hip_trial3))
max_hip=np.array((max_value_hip_trial1, max_value_hip_trial2,max_value_hip_trial3))
ROM_hip=np.array((ROM_value_hip_trial1,ROM_value_hip_trial2, ROM_value_hip_trial3))

print()
print("Ankle")
print("Mean min :", np.mean(min_ankle)) 
print( "SD :", np.std(min_ankle))
print("Mean max :", np.mean(max_ankle))
print("SD :", np.std(max_ankle))
print("Mean ROM :", np.mean(ROM_ankle))
print("SD: ", np.std(ROM_ankle))
print()

print("Knee")
print("Mean min :", np.mean(min_knee)) 
print( "SD :", np.std(min_knee))
print("Mean max :", np.mean(max_knee))
print("SD :", np.std(max_knee))
print("Mean ROM :", np.mean(ROM_knee))
print("SD: ", np.std(ROM_knee))
print()

print()
print("Hip")
print("Mean min :", np.mean(min_hip)) 
print( "SD :", np.std(min_hip))
print("Mean max :", np.mean(max_hip))
print("SD :", np.std(max_hip))
print("Mean ROM :", np.mean(ROM_hip))
print("SD : ", np.std(ROM_hip))
print()

print()
print("Ankle: ", "Mean min :", np.mean(min_ankle), "/ SD :", np.std(min_ankle), "-  Mean max :", np.mean(max_ankle), "/ SD :", np.std(max_ankle), "-  Mean ROM :", np.mean(ROM_ankle), "/ SD: ", np.std(ROM_ankle))
print("Knee: ", "Mean min :", np.mean(min_knee), "/ SD :", np.std(min_knee), "-  Mean max :", np.mean(max_knee), "/ SD :", np.std(max_knee), "-  Mean ROM :", np.mean(ROM_knee), "/ SD: ", np.std(ROM_knee))
print("Hip: ", "Mean min :", np.mean(min_hip), "/ SD :", np.std(min_hip), "-  Mean max :", np.mean(max_hip), "/ SD :", np.std(max_hip), "-  Mean ROM :", np.mean(ROM_hip), "/ SD: ", np.std(ROM_hip))

# Gait cycle graphs
import matplotlib.pyplot as plt

array_T_trial1 = array_trial1[:,0]
T_trial1=[] # Time as percentage gait cycle
n1=len(array_T_trial1)
for i in range (n1):
        T_trial1.append(((array_T_trial1[i]-array_T_trial1[0])/(array_T_trial1[n1-1]-array_T_trial1[0]))*100)
        
array_T_trial2 = array_trial2[:,0]
T_trial2=[] # Time as percentage gait cycle
n2=len(array_T_trial2)
for i in range (n2):
        T_trial2.append(((array_T_trial2[i]-array_T_trial2[0])/(array_T_trial2[n2-1]-array_T_trial2[0]))*100)
        
        
array_T_trial3 = array_trial3[:,0]
T_trial3=[] # Time as percentage gait cycle
n3=len(array_T_trial3)
for i in range (n3):
        T_trial3.append(((array_T_trial3[i]-array_T_trial3[0])/(array_T_trial3[n3-1]-array_T_trial3[0]))*100)


ankle_trial1=array_trial1[:,column_ankle]
ankle_trial2=array_trial2[:,column_ankle]
ankle_trial3=array_trial3[:,column_ankle]

plt.figure('MB067: Ankle ROM')
plt.plot(T_trial1, ankle_trial1, label='Trial 1')
plt.plot(T_trial2, ankle_trial2, label='Trial 2')
plt.plot(T_trial3, ankle_trial3, label='Trial 3')
plt.grid(True)
plt.title('MB067: Ankle ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Ankle ROM (°)')
plt.legend()
plt.show()

knee_trial1=array_trial1[:,column_knee]
knee_trial2=array_trial2[:,column_knee]
knee_trial3=array_trial3[:,column_knee]

plt.figure('MB067: Knee ROM')
plt.plot(T_trial1, knee_trial1, label='Trial 1')
plt.plot(T_trial2, knee_trial2, label='Trial 2')
plt.plot(T_trial3, knee_trial3, label='Trial 3')
plt.grid(True)
plt.title('MB067: Knee ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Knee ROM (°)')
plt.legend()
plt.show()

hip_trial1=array_trial1[:,column_hip]
hip_trial2=array_trial2[:,column_hip]
hip_trial3=array_trial3[:,column_hip]

plt.figure('MB067: Hip ROM')
plt.plot(T_trial1, hip_trial1, label='Trial 1')
plt.plot(T_trial2, hip_trial2, label='Trial2')
plt.plot(T_trial3, hip_trial3, label='Trial3')
plt.grid(True)
plt.title('MB067: Hip ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Hip ROM (°)')
plt.legend()
plt.show()

###################################
#Get data for control leg

if limb=='L': # Conditional statement based on the operated limb
        column_ankle_control = 221  # Left Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee_control= 314    # Left Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip_control= 302     # Left Hip Column - 1 /!\ Always check column as missing markers lead to missing data
else:
        column_ankle_control= 20 # Right Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee_control= 113 # Right Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip_control= 101 # Right Hip Column - 1 /!\ Always check column as missing markers lead to missing data
        

ankle_trial1_control=array_trial1[:,column_ankle_control]
ankle_trial2_control=array_trial2[:,column_ankle_control]
ankle_trial3_control=array_trial3[:,column_ankle_control]

plt.figure('MB067: Ankle ROM')
plt.plot(T_trial1, ankle_trial1, label='Trial 1')
plt.plot(T_trial1, ankle_trial1_control, label='Trial 1_control')
plt.plot(T_trial2, ankle_trial2, label='Trial 2')
plt.plot(T_trial2, ankle_trial2_control, label='Trial 2_control')
plt.plot(T_trial3, ankle_trial3, label='Trial 3', color ='red')
plt.plot(T_trial2, ankle_trial3_control, label='Trial 3_control',color = 'blue')
plt.grid(True)
plt.title('MB067: Ankle ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Ankle ROM (°)')
plt.legend()
plt.show()


knee_trial1_control=array_trial1[:,column_knee_control]
knee_trial2_control=array_trial2[:,column_knee_control]
knee_trial3_control=array_trial3[:,column_knee_control]

plt.figure('MB067: Knee ROM')
plt.plot(T_trial1, knee_trial1, label='Trial 1')
plt.plot(T_trial2, knee_trial2, label='Trial 2')
plt.plot(T_trial3, knee_trial3, label='Trial 3', color = 'red')
plt.plot(T_trial1, knee_trial1_control, label='Trial 1 Control')
plt.plot(T_trial2, knee_trial2_control, label='Trial 2 Control')
plt.plot(T_trial3, knee_trial3_control, label='Trial 3 Control', color = 'blue')
plt.grid(True)
plt.title('MB067: Knee ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Knee ROM (°)')
plt.legend()
plt.show()



hip_trial1_control=array_trial1[:,column_hip_control]
hip_trial2_control=array_trial2[:,column_hip_control]
hip_trial3_control=array_trial3[:,column_hip_control]

plt.figure('MB067: Hip ROM')
plt.plot(T_trial1, hip_trial1, label='Trial 1')
plt.plot(T_trial2, hip_trial2, label='Trial2')
plt.plot(T_trial3, hip_trial3, label='Trial3', color = 'red')
plt.plot(T_trial1, hip_trial1_control, label='Trial 1 Control')
plt.plot(T_trial2, hip_trial2_control, label='Trial2 Control')
plt.plot(T_trial3, hip_trial3_control, label='Trial3 Control', color = 'blue')
plt.grid(True)
plt.title('MB067: Hip ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Hip ROM (°)')
plt.legend()
plt.show()


#Try to match up peak hip 9right before toe strike with eachother

plt.figure('MB067: Hip ROM Squared')
plt.plot(T_trial1, hip_trial1**2, label='Trial 1')
plt.plot(T_trial2, hip_trial2**2, label='Trial2')
plt.plot(T_trial3, hip_trial3**2, label='Trial3', color = 'red')
plt.plot(T_trial1, hip_trial1_control**2, label='Trial 1 Control')
plt.plot(T_trial2, hip_trial2_control**2, label='Trial2 Control')
plt.plot(T_trial3, hip_trial3_control**2, label='Trial3 Control', color = 'blue')
plt.grid(True)
plt.title('MB067: Hip ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Hip ROM (°)')
plt.legend()
plt.show()

#find index of peak in control
#peak is one value
#is it at the peak more than once????



peak_hip_flexion_control1 = np.amax(hip_trial1_control)
print('peak value of control: ', peak_hip_flexion_control1)
#print('shape of trial list/array', hip_trial1_control.shape)
control_peak_index1 = np.where (hip_trial1_control == peak_hip_flexion_control1)
print(control_peak_index1)
#not in correct form so take integer of the first value
control_peak_index1 = int(control_peak_index1[0])
print('index of peak in control: ',control_peak_index1)



#THIS IS A TUPLE AND I NEED IT TO BE AN INT

#find index of peak in trial
peak_hip_flexion1 = np.amax(hip_trial1)
print(peak_hip_flexion1)
peak_index1 = np.where (hip_trial1 == peak_hip_flexion1)
#peak_index1 = sq_hip_trial1.index(peak_hip_flexion1)
print(peak_index1)
trial_peak_index1 = int(peak_index1[0])
#not in correct form so take integer of the first value
print('index of peak in trial: ',trial_peak_index1)
#find what index the trial peaks at

length_of_trial1 = len(T_trial1)
fitted_hip_control1 = np.zeros(length_of_trial1)
#create empty array of length of the trial
fitted_hip_control1[trial_peak_index1:length_of_trial1+1] = hip_trial1_control[control_peak_index1:length_of_trial1-trial_peak_index1 + control_peak_index1]
fitted_hip_control1[trial_peak_index1-control_peak_index1: trial_peak_index1] = hip_trial1_control[0:control_peak_index1]
fitted_hip_control1[:trial_peak_index1-control_peak_index1] = hip_trial1_control[length_of_trial1-trial_peak_index1+control_peak_index1:]
print(hip_trial1_control)
print(fitted_hip_control1)

plt.figure('MB067: Fitted Hip ROM')
plt.plot(T_trial1, hip_trial1, label='Trial 1', color = 'red')
plt.plot(T_trial1, hip_trial1_control, label='Trial 1 Control', color = 'blue')
plt.plot(T_trial1, fitted_hip_control1, label='Trial 1 Control fitted', color = 'green')
plt.grid(True)
plt.title('MB067: Hip ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Hip ROM (°)')
plt.legend()
plt.show()


length_of_trial1 = len(T_trial1)
fitted_knee_control1 = np.zeros(length_of_trial1)
#create empty array of length of the trial
fitted_knee_control1[trial_peak_index1:length_of_trial1+1] = knee_trial1_control[control_peak_index1:length_of_trial1-trial_peak_index1 + control_peak_index1]
fitted_knee_control1[trial_peak_index1-control_peak_index1: trial_peak_index1] = knee_trial1_control[0:control_peak_index1]
fitted_knee_control1[:trial_peak_index1-control_peak_index1] = knee_trial1_control[length_of_trial1-trial_peak_index1+control_peak_index1:]
# print(hip_trial1_control)
# print(fitted_hip_control1)

plt.figure('MB067: Fitted knee ROM')
plt.plot(T_trial1, knee_trial1, label='Trial 1', color = 'red')
plt.plot(T_trial1, knee_trial1_control, label='Trial 1 Control', color = 'blue')
plt.plot(T_trial1, fitted_knee_control1, label='Trial 1 Control fitted', color = 'green')
plt.grid(True)
plt.title('MB067: Knee ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Knee ROM (°)')
plt.legend()
plt.show()


length_of_trial1 = len(T_trial1)
fitted_ankle_control1 = np.zeros(length_of_trial1)
#create empty array of length of the trial
fitted_ankle_control1[trial_peak_index1:length_of_trial1+1] = ankle_trial1_control[control_peak_index1:length_of_trial1-trial_peak_index1 + control_peak_index1]
fitted_ankle_control1[trial_peak_index1-control_peak_index1: trial_peak_index1] = ankle_trial1_control[0:control_peak_index1]
fitted_ankle_control1[:trial_peak_index1-control_peak_index1] = ankle_trial1_control[length_of_trial1-trial_peak_index1+control_peak_index1:]
# print(hip_trial1_control)
# print(fitted_hip_control1)

plt.figure('MB067: Fitted ankle ROM')
plt.plot(T_trial1, ankle_trial1, label='Trial 1', color = 'red')
plt.plot(T_trial1, ankle_trial1_control, label='Trial 1 Control', color = 'blue')
plt.plot(T_trial1, fitted_ankle_control1, label='Trial 1 Control fitted', color = 'green')
plt.grid(True)
plt.title('MB067: Ankle ROM')
plt.xlabel('Percentage gait cycle')
plt.ylabel('Ankle ROM (°)')
plt.legend()
plt.show()



# last=0
# upflag=0
# p=0
# gait_cycle = np.zeros(len(hip_trial1_control))
# for j in range(len(hip_trial1_control)):
#     if sq_hip_trial1_control[j]== peak_hip_flexion:
#         if upflag == 0:
#             if last >0:
#                 timem = j-last
#                 p=1000/timem*60
#             last=j
#             upflag=200
#     else:
#         if upflag>0:
#             upflag=upflag-1


