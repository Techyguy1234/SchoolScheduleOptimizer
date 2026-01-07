import main
import random

classlist = main.classlist
studentSchedules = main.studentSchedules

currentBest = main.test_full_schedule(studentSchedules, 'SEM2')
currentBestSchedule = studentSchedules

def run_optimizer_loop(schedules:list):
    pass
while True:
    run_optimizer_loop(currentBest)