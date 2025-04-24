import numpy as np

class Sched:


    def __init__(self,JobList: list):

        self.JobList = JobList

    def SchedulabilityAnalysis(self) -> float:

        return sum([self.JobList[i].GetCPUUse() for i in range(len(self.JobList))])
    
    def IsSchedulable(self) -> bool:

        return self.SchedulabilityAnalysis() < 1.0
    
    def ComputeScheduling(self) -> None:
        

        for i in range(80):

            [self.JobList[j].Tick() for j in range(len(self.JobList))]
            
            for j in range(len(self.JobList)):
                
                if(self.JobList[j].IsRunning()):
                
                    break

            else:
                
                for j in range(len(self.JobList)):

                    if(self.JobList[j].IsWaitingForScheduling()):
                        
                        self.JobList[j].Run()
                        break

            

            for j in range(len(self.JobList)):

                print(str(self.JobList[j].GetStatusID()) + " ", end=" ")

            
            print()

