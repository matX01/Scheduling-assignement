import numpy as np

class Sched:


    def __init__(self,JobList: list):

        self.JobList = JobList

    def SchedulabilityAnalysis(self) -> float:

        return sum([self.JobList[i].GetCPUUse() for i in range(len(self.JobList))])
    
    def IsSchedulable(self) -> bool:

        return self.SchedulabilityAnalysis() < 1.0
    
    def ComputeScheduling(self) -> None:
        print("    ",end="")
        for j in range(len(self.JobList)):

            print(self.JobList[j].getName(),end="|")
        
        print()

        for i in range(80):

            # tick through each task (make them move by 1 second)
            [self.JobList[j].Tick() for j in range(len(self.JobList))]
            

            # find if a job is currently running (it would be faster to store running job in a variable to prevent the need of a loop)
            for j in range(len(self.JobList)):
                
                if(self.JobList[j].IsRunning()):
                
                    break

            else:
                
                #if no jobs are currently running, find the highest priority job that is waiting and execute it
                for j in range(len(self.JobList)):

                    if(self.JobList[j].IsWaitingForScheduling()):
                        
                        self.JobList[j].Run()
                        break

            #display the results
            print("{0:0=2d}s|".format(i+1),end="")

            for j in range(len(self.JobList)):

                print(str(self.JobList[j].GetStatusID()) + " ", end=" ")

            
            print()

