import main
import random
import copy
import math

classlist = main.classlist
studentSchedules = main.studentSchedules

currentBest = main.test_full_schedule(studentSchedules, 'SEM2')
currentBestSchedule = studentSchedules

iteration_count = 0
temperature = 1.0  # For simulated annealing


def run_optimizer_loop(schedules:list):
    global currentBest
    global currentBestSchedule
    global iteration_count
    global temperature

    iteration_count += 1
    
    # Simulated annealing: gradually cool down acceptance probability
    temperature = max(0.1, 1.0 - (iteration_count / 10000.0))

    noOptimizationFound = True
    while noOptimizationFound:
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
                    print("current best: "+str(currentBest)+" | swap result: "+str(swapResult)+" | temp: "+str(round(temperature, 3)))
                    
                    # Accept if better, OR accept worse swap with probability (simulated annealing)
                    if swapResult < currentBest:
                        print("found optimization! new best: "+str(swapResult))
                        currentBest=swapResult
                        schedules=swapSchedule
                        currentBestSchedule=swapSchedule
                        noOptimizationFound=False
                        return swapSchedule
                    elif temperature > 0.1:  # Still exploring
                        # Accept worse solution with decreasing probability
                        delta = swapResult - currentBest
                        acceptance_prob = math.exp(-delta / (currentBest * temperature))
                        if random.random() < acceptance_prob:
                            print(f"accepting worse swap (prob: {round(acceptance_prob, 3)}) - exploring...")
                            schedules=swapSchedule
                            currentBestSchedule=swapSchedule
                            noOptimizationFound=False
                            return swapSchedule



while True:
    run_optimizer_loop(currentBestSchedule)