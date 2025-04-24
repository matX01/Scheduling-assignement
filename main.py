from Job import Job
from Sched import Sched

JobList = [Job(2,10),
           Job(3,10),
           Job(2,20),
           Job(2,20),
           Job(2,40),
           Job(2,40),
           Job(3,80)]



Scheduler = Sched(JobList)

print(Scheduler.SchedulabilityAnalysis())

if(Scheduler.IsSchedulable()):

    print("Task is schedulable.")

else:

    print("Task is not schedulable")
Scheduler.ComputeScheduling()
