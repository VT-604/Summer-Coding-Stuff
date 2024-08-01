#VT-604
# #Date
# #Reading CSV Files

#Initial
import csv
import random
csvFile="scores.csv"
studentNames=[]
studentScores=[]
#Functions
#Main
with open(csvFile,"r") as file:
    reader=csv.reader(file)
    for row in reader:
        studentNames.append(row[0])
        studentScores.append(row[1])
perfectScore=[]
for i in range(len(studentNames)):
    student=studentNames[i]
    score=studentScores[i]
    if score=="100":
        perfectScore.append(student)
winner=random.choice(perfectScore)
print("The winner is... "+winner)

