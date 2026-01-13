import main
import random
import copy

classlist = main.classlist
studentSchedules = main.studentSchedules

currentBest = main.test_full_schedule(studentSchedules, 'SEM2')
currentBestSchedule = studentSchedules

iterations_without_improvement = 0


def run_optimizer_loop(schedules:list):
    global currentBest
    global currentBestSchedule
    global iterations_without_improvement

    # If stuck for too long, do a random multi-swap to escape and keep exploring
    if iterations_without_improvement > 300:
        print(f"\n>>> STUCK for {iterations_without_improvement} iterations - doing random escape...\n")
        selectedScheduleIndex = random.randint(0, len(currentBestSchedule)-1)
        swapSchedule = copy.deepcopy(currentBestSchedule)
        
        # Random swap to escape
        idx1 = random.randint(1, 8)
        idx2 = random.randint(1, 8)
        if idx1 != idx2:
            swapSchedule[selectedScheduleIndex][idx1], swapSchedule[selectedScheduleIndex][idx2] = \
                swapSchedule[selectedScheduleIndex][idx2], swapSchedule[selectedScheduleIndex][idx1]
        
        testResult = main.test_full_schedule(swapSchedule, 'SEM2')
        print(f"Random escape result: {testResult}\n")
        currentBestSchedule = swapSchedule
        iterations_without_improvement = 0
        return None

    found_improvement = False
    
    #pick a random schedule to optimize
    selectedScheduleIndex = random.randint(0, len(schedules)-1)
    selectedSchedule = schedules[selectedScheduleIndex]

    #picks a random period and checks other periods for possible swaps
    swapClass1Index=random.randint(1, 8)
    swapClass1=selectedSchedule[swapClass1Index]

    for i in classlist[swapClass1[1]][2]:
        #check periods of class 1 for possible swaps with 2
        swapClass2Index=int(i)-1

        #i dont want to figure out how the heck to fix the parse for 10th period classes right now, so i just wont
        if swapClass2Index==9:
            swapClass2Index=8
        swapClass2=selectedSchedule[swapClass2Index]

        if swapClass2==swapClass1:
            pass#print("same class, skipping")
        else:
            if classlist[swapClass2[1]][2].__contains__(swapClass1[2]):
                print("found possible swap between period "+str(swapClass1Index+1)+" and "+str(swapClass2Index+1))

                swapSchedule = copy.deepcopy(schedules)
                swapSchedule[selectedScheduleIndex][swapClass1Index] = swapClass2
                swapSchedule[selectedScheduleIndex][swapClass2Index] = swapClass1
                swapResult=main.test_full_schedule(swapSchedule, 'SEM2')
                print("current best: "+str(currentBest)+" | swap result: "+str(swapResult)+" | no_improve: "+str(iterations_without_improvement))
                
                if swapResult<currentBest:
                    print("found optimization! new best: "+str(swapResult))
                    currentBest=swapResult
                    schedules=swapSchedule
                    currentBestSchedule=swapSchedule
                    iterations_without_improvement = 0
                    found_improvement = True
                    return swapSchedule
    
    # If we get here, no improvement was found in this iteration
    if not found_improvement:
        iterations_without_improvement += 1
    
    return None



while True:
    run_optimizer_loop(currentBestSchedule)