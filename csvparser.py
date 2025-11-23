import csv
import sys

# writes class list in format 'Course Name': ['Term', 'Location', ['Period'], 'Teacher']
readcsv = csv.reader(open("Student_Schedules - Student_Schedules.csv"))
classList={}
for row in readcsv:
    if not classList.__contains__(row[1]):
        classList[row[1]]=[row[5],row[4],[],row[3]]
    if not classList[row[1]][2].__contains__(row[2]): #adds specific periods to each class
        classList[row[1]][2].append(row[2])


# create array of each individual schedule
studentSchedules=[[0]]

iteration=0

currentSchedule=0
currentScheduleSize=10

lastPeriod=[]

readcsv = csv.reader(open("Student_Schedules - Student_Schedules.csv"))
for row in readcsv:
    if iteration!=0:
        if row[5]=='SEM1':
            currentScheduleSize+=1
        if currentScheduleSize == 0:
            studentSchedules[currentSchedule].append(lastPeriod)
            currentSchedule+=1
            currentScheduleSize=10
            if row[0]=='12':
                currentScheduleSize=9
            studentSchedules.append([])
        if row[2]=='10':
            lastPeriod=row
        else:
            studentSchedules[currentSchedule].append(row)
        currentScheduleSize-=1

    iteration+=1
studentSchedules[currentSchedule].append(lastPeriod)

print(len(studentSchedules))
print(studentSchedules[137])
