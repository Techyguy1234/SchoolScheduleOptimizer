import csvparser as parser
import visualizer
import time
import NetworkPathfinding as pathfinder

classlist=parser.classList
studentSchedules=parser.studentSchedules

#print(studentSchedules[len(studentSchedules)-1])

#visualizer.visualize()



def test_schedule(schedules,period,notSemester):
    segmentusage={}
    #print(schedules)
    for i in schedules:
        #print(len(i))
        c=i
        for b in i:
            if b[5]==notSemester:
                c.pop(c.index(b))
        if period != 10 and (len(c)>period):
            for a in pathfinder.get_path(c[period-1][4],c[period][4]):
                if not segmentusage.__contains__(a):
                    segmentusage[a]=0
                segmentusage[a]+=1
    print(segmentusage)

for a in range(1500):
    test_schedule(studentSchedules,9,'SEM2')
    t=time.time()*1000
    print(time.time()*1000-t)