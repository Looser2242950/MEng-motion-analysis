#cd C:\Users\Ordinateur\Documents #Current directory where the CSV file is 
 #Edited version
import csv
patientID = input('Input patient ID number: ')

while True:
    limb= str(input('Type "L" if operation on left leg, type "R" if right leg: '))
    if limb not in ('R', 'L'):
        print("Not an appropriate choice.")
    else:
        break

 # Definition of the operated limb
fname_trial1 = str(input('input file name for Trial 1: ') or 'mg1963 levelwalking03a.csv')
fname_trial2 = str(input('input file name for Trial 2: ') or 'mg1963 levelwalking03a.csv')
fname_trial3 = str(input('input file name for Trial 3: ') or 'mg1963 levelwalking03a.csv')

print()
print("Patient ID: ", patientID)
print("Limb operated on:", limb)
print("Data files:",  fname_trial1, fname_trial2, fname_trial3)
print()





if limb=='L': # Conditional statement based on the operated limb
        column_ankle_trial1 = 20 # Left Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee_trial1= 113 # Left Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip_trial1= 101 # Left Hip Column - 1 /!\ Always check column as missing markers lead to missing data
else:
        column_ankle_trial1= 221 # Right Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee_trial1= 314 # Right Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip_trial1= 302 # Right Hip Column - 1 /!\ Always check column as missing markers lead to missing data
        
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
min_value_ankle_trial1 = np.amin(array_trial1[:,column_ankle_trial1]) # Min ankle value for trial 1
max_value_ankle_trial1 = np.amax(array_trial1[:,column_ankle_trial1]) # Max ankle value for trial 1
ROM_value_ankle_trial1= max_value_ankle_trial1 - min_value_ankle_trial1 # ROM ankle value for trial 1

min_value_knee_trial1 = np.amin(array_trial1[:,column_knee_trial1]) # Min knee value for trial 1
max_value_knee_trial1 = np.amax(array_trial1[:,column_knee_trial1])  # Max knee value for trial 1
ROM_value_knee_trial1=max_value_knee_trial1-min_value_knee_trial1 # ROM knee value for trial 1

min_value_hip_trial1 = np.amin(array_trial1[:,column_hip_trial1]) # Min hip value for trial 1
max_value_hip_trial1 = np.amax(array_trial1[:,column_hip_trial1]) # Max hip value for trial 1
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

if limb=='L': # Conditional statement based on the operated limb
        column_ankle_trial2 = 20 # Left Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee_trial2= 113 # Left Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip_trial2= 101 # Left Hip Column - 1 /!\ Always check column as missing markers lead to missing data
else:
        column_ankle_trial2= 221 # Right Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee_trial2= 314 # Right Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip_trial2= 302 # Right Hip Column - 1 /!\ Always check column as missing markers lead to missing data

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

min_value_ankle_trial2 = np.amin(array_trial2[:,column_ankle_trial2]) # Min ankle value for trial 2
max_value_ankle_trial2 = np.amax(array_trial2[:,column_ankle_trial2]) # Max ankle value for trial 2
ROM_value_ankle_trial2= max_value_ankle_trial2 - min_value_ankle_trial2 # ROM ankle value for trial 2

min_value_knee_trial2 = np.amin(array_trial2[:,column_knee_trial2]) # Min knee value for trial 2
max_value_knee_trial2 = np.amax(array_trial2[:,column_knee_trial2])  # Max knee value for trial 2
ROM_value_knee_trial2=max_value_knee_trial2-min_value_knee_trial2 # ROM knee value for trial 2

min_value_hip_trial2 = np.amin(array_trial2[:,column_hip_trial2]) # Min hip value for trial 2
max_value_hip_trial2 = np.amax(array_trial2[:,column_hip_trial2]) # Max hip value for trial 2
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

if limb=='L': # Conditional statement based on the operated limb
        column_ankle_trial3 = 20 # Left Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee_trial3= 113 # Left Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip_trial3= 101 # Left Hip Column - 1 /!\ Always check column as missing markers lead to missing data
else:
        column_ankle_trial3= 221 # Right Ankle Column - 1 /!\ Always check column as missing markers lead to missing data
        column_knee_trial3= 314 # Right Knee Column - 1 /!\ Always check column as missing markers lead to missing data
        column_hip_trial3= 302 # Right Hip Column - 1 /!\ Always check column as missing markers lead to missing data

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

min_value_ankle_trial3 = np.amin(array_trial3[:,column_ankle_trial3]) # Min ankle value for trial 3
max_value_ankle_trial3 = np.amax(array_trial3[:,column_ankle_trial3]) # Max ankle value for trial 3
ROM_value_ankle_trial3= max_value_ankle_trial3 - min_value_ankle_trial3 # ROM ankle value for trial 3

min_value_knee_trial3 = np.amin(array_trial3[:,column_knee_trial3]) # Min knee value for trial 3
max_value_knee_trial3 = np.amax(array_trial3[:,column_knee_trial3])  # Max knee value for trial 3
ROM_value_knee_trial3=max_value_knee_trial3-min_value_knee_trial3 # ROM knee value for trial 3

min_value_hip_trial3 = np.amin(array_trial3[:,column_hip_trial3]) # Min hip value for trial 3
max_value_hip_trial3 = np.amax(array_trial3[:,column_hip_trial3]) # Max hip value for trial 3
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


ankle_trial1=array_trial1[:,column_ankle_trial1]
ankle_trial2=array_trial2[:,column_ankle_trial2]
ankle_trial3=array_trial3[:,column_ankle_trial3]

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

knee_trial1=array_trial1[:,column_knee_trial1]
knee_trial2=array_trial2[:,column_knee_trial2]
knee_trial3=array_trial3[:,column_knee_trial3]

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

hip_trial1=array_trial1[:,column_hip_trial1]
hip_trial2=array_trial2[:,column_hip_trial2]
hip_trial3=array_trial3[:,column_hip_trial3]

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
