#                      Drug Efficiancy Analysis: Hypertension Medication Trial(Before and After)



#We import numpy first of all as np
import numpy as np 

#This script is designed to analyse the data(random self generated) of 100 patients and then see if the hospital did a good job at treating them or not
#We set a seed for the set of the values needed for our project
np.random.seed(123)
#Generate 100 ID's
ids = np.arange(0,100)
#Generate 100 Ages
ages = np.random.randint(17,81, size = 100)
#Generate 100 BP Before
bp_before = np.random.randint(119,171, size = 100)
#Generate 100 BP After
bp_after = np.random.randint(110, 151, size=100)
#Combining all 4 of these datasets into one database
dataset = np.column_stack((ids,ages,bp_before,bp_after)) 
#To print the shape and the databse of the dataset
#print("Dataset Shape:", dataset.shape)
#print(dataset[:5])

#Now we Slice and Index them
#To separate the columns form the main datset 
bpb = dataset[:,2]
bpa = dataset[:,3]
#print(bpb)
#print(bpa)

#Now we calculate the drop in the BP for every patient
bp_drop = bpb-bpa
avg_drop = np.mean(bp_drop)
max_drop = np.max(bp_drop)
std_drop = np.std(bp_drop)

#Now we use the filtering(kind of) in numpy to see how many cases were failed and print 
failed_cases = dataset[bp_drop < 0]
#print(f"Number of Filed Cases: {len(failed_cases)}.")

#To add some more interactivity in this same 
#Finding the oldest and the youngest aged patient
oldest = np.max(dataset[:,1])
youngest = np.min(dataset[:,1])
#print(f"The oldest patient was {oldest} years, and the youngest patient was {youngest}  years old.")
#Finding the sucess rate of the total lot of 100 students in this field
sucess_rate = ((100 - len(failed_cases)) / 100) * 100
#print(f"The rate of sucess in the 100 cases were {sucess_rate}.")
#Finding the BP only for people above 60
over_60 = dataset[:,1,] >60
avg_bp_over_60 = np.mean(over_60) 
#print(f"Avg BP (Seniors > 60): {avg_bp_over_60:.1f} mmHg.")
#Finding the people that were helped by the medication
super_responders = dataset[bp_drop > 30]
#print(f"Number of Super Responders with better health: {len(super_responders)}")

#FINALLY we print the last statements for which we put #'s in all the print statemnets so that we can draft the Final Report now:
print()
print("=" * 40)
print("CLINICAL TRIAL EXECUTIVE SUMMARY")
print("Total Patient Population: 100 Individuals")
print("Primary Variable: Systolic Blood Pressure Reduction")
print("_" * 40)
print("PATIENT DEMOGRAPHICS")
print("Target Age Range:", youngest, "to", oldest, "years")
print("Senior Demographic Mean Baseline BP:", round(avg_bp_over_60, 2), "mmHg")
print("_" * 40)
print("TREATMENT OUTCOMES")
print("Mean Group Improvement:", round(avg_drop, 2), "mmHg")
print("Maximum Observed Patient Improvement:", max_drop, "mmHg")
print("Treatment Standard Deviation:", round(std_drop, 2))
print("_" * 40)
print("EFFICACY AND RISK ASSESSMENT")
print("Total Patients with Significant Improvement:", len(super_responders))
print("Total Patients the drug failed:", len(failed_cases))
print("Overall Trial Success Rate Percentage:", sucess_rate)
print("=" * 40)
print("END OF REPORT")
print()