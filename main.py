import csvparser as parser
import visualizer
import time
import NetworkPathfinding as pathfinder
import gLib

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
    return segmentusage

def avg_from_schedule_period(segmentsinput):
    segments=[0,0,0,0,0,0,0,0,0,0,0,0]
    for key, value in segmentsinput.items():
        value2 =  0
        
        value2 = value

            
        
        




        if key == 'H11':
            segments[11] = value2
        if key == 'H10':
            segments[10] = value2
        if key == 'H9':
            segments[9] = value2
        if key == 'H8':
            segments[8] = value2
        if key == 'H7':
            segments[7] = value2
        if key == 'H6':
            segments[6] = value2
        if key == 'H5':
            segments[5] = value2
        if key == 'H4':
            segments[4] = value2
        if key == 'H3':
            segments[3] = value2
        if key == 'H2':
            segments[2] = value2
        if key == 'H1':
            segments[1] = value2
        if key == 'H0':
            segments[0] = value2
    avg = segments[0]+segments[1]+segments[2]+segments[3]+segments[4]+segments[5]+segments[6]+segments[7]+segments[8]+segments[9]+segments[10]+segments[11]
    #print("\n\n"+str(avg)+"\n\n")
    avg = avg / 12
    return avg

def test_full_schedule(schedules,notSemester):
    fullAvg = avg_from_schedule_period(test_schedule(schedules,1,notSemester))
    fullAvg += avg_from_schedule_period(test_schedule(schedules,2,notSemester))
    fullAvg += avg_from_schedule_period(test_schedule(schedules,3,notSemester))
    fullAvg += avg_from_schedule_period(test_schedule(schedules,4,notSemester))
    fullAvg += avg_from_schedule_period(test_schedule(schedules,5,notSemester))
    fullAvg += avg_from_schedule_period(test_schedule(schedules,6,notSemester))
    fullAvg += avg_from_schedule_period(test_schedule(schedules,7,notSemester))
    fullAvg += avg_from_schedule_period(test_schedule(schedules,8,notSemester))
    fullAvg += avg_from_schedule_period(test_schedule(schedules,9,notSemester))
    fullAvg = fullAvg / 9
    return fullAvg

#for a in range(1500):
#    test_schedule(studentSchedules,9,'SEM2')
#    t=time.time()*1000
#    print(time.time()*1000-t)

gLib.draw_map(test_schedule(studentSchedules,1,'SEM2'))
gLib.draw_map(test_schedule(studentSchedules,2,'SEM2'))
gLib.draw_map(test_schedule(studentSchedules,3,'SEM2'))
gLib.draw_map(test_schedule(studentSchedules,4,'SEM2'))
gLib.draw_map(test_schedule(studentSchedules,5,'SEM2'))
gLib.draw_map(test_schedule(studentSchedules,6,'SEM2'))
gLib.draw_map(test_schedule(studentSchedules,7,'SEM2'))
gLib.draw_map(test_schedule(studentSchedules,8,'SEM2'))
gLib.draw_map(test_schedule(studentSchedules,9,'SEM2'))



print(test_full_schedule(studentSchedules,'SEM2'))