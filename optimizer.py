import main
import random

classlist = main.classlist
studentSchedules = main.studentSchedules

currentBest = studentSchedules

def run_optimizer_loop(schedules:list):
    noOptimazitionFound = True
    while noOptimazitionFound:
        editingSchedule = random.randint(0,(len(schedules)-1))
        swapPeriod1=random.randint(1,8)

        #print(schedules[editingSchedule][swapPeriod1])
        #print(schedules[editingSchedule])
        swapPeriod1Periods=classlist[schedules[editingSchedule][swapPeriod1][1]][2]
        swapPossibleCandidates=[]
        if not len(swapPeriod1Periods) > 1:
            for i in swapPeriod1Periods:
                if (classlist[schedules[editingSchedule][int(i)-1][1]][2] == classlist[schedules[editingSchedule][swapPeriod1][1]][2]) and not (schedules[editingSchedule][swapPeriod1] == 'SEM2' or schedules[editingSchedule][int(i)-1] == 'SEM2'):
                    swapPossibleCandidates.append(int(i)-1)
    print(swapPossibleCandidates)
    for i in swapPossibleCandidates:
        swapSchedule1 = schedules
        swapSchedule1[editingSchedule][swapPeriod1], swapSchedule1[editingSchedule][i] =  swapSchedule1[editingSchedule][i], swapSchedule1[editingSchedule][swapPeriod1]
        if main.test_full_schedule(swapSchedule1,'SEM2') < currentBest:
            currentBest = swapSchedule1
            noOptimazitionFound = False
    print("New current best is %s, starting was 39.62037037037037, the improvement is %s" % (main.test_full_schedule(currentBest,'SEM2'),39.62037037037037/(39.62037037037037-main.test_full_schedule(currentBest,'SEM2'))))

while True:
    run_optimizer_loop(currentBest)
#print(classlist)s