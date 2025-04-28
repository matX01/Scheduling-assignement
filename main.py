from Job import Job
from Sched import Sched

CONST_TRY_WITH_T5_MISS = False


if(not CONST_TRY_WITH_T5_MISS):
    JobList = [Job("T1",2,10),
            Job("T2",3,10),
            Job("T3",2,20),
            Job("T4",2,20),
            Job("T5",2,40),
            Job("T6",2,40),
            Job("T7",3,80)]
else:
    JobList = [Job("T1",2,10),
            Job("T2",3,10),
            Job("T3",2,20),
            Job("T4",2,20),
            Job("T6",2,40),
            Job("T7",3,80),
            Job("T5",2,40)]



Scheduler = Sched(JobList)

print(Scheduler.SchedulabilityAnalysis())

if(Scheduler.IsSchedulable()):

    print("Task is schedulable.")

else:

    print("Task is not schedulable")


Scheduler.ComputeScheduling()
