import csv

# writes class list in format 'Course Name': ['Term', 'Location', ['Period'], 'Teacher']
readcsv = csv.reader(open("Student_Schedules - Student_Schedules.csv"))
classlist={}
for row in readcsv:
    if not classlist.__contains__(row[1]):
        classlist[row[1]]=[row[5],row[4],[],row[3]]
    if not classlist[row[1]][2].__contains__(row[2]): #adds specific periods to each class
        classlist[row[1]][2].append(row[2])

iteration=0
readcsv = csv.reader(open("Student_Schedules - Student_Schedules.csv"))
for row in readcsv:
    if iteration != 5456:
        print(row)
    iteration+=1