class Job:



    def __init__(self,C: int,Ti: int) -> None:
        
        self.C = C
        self.Ti = Ti
        self.PeriodRemaining = self.Ti
        self.RunningTime = 0
        self.State = "WAITING"
    
    def GetLength(self) -> int:

        return self.C

    def GetPeriod(self) -> int:

        return self.Ti
    
    def IsRunning(self) -> bool:

        return self.State == "RUNNING"

    def IsWaitingForScheduling(self) -> bool:

        return self.State == "WAITING"
    
    def Run(self) -> None:

        self.State = "RUNNING"

    def GetStatus(self) -> str:

        return self.State
    
    def GetStatusID(self) -> int:

        ReturnST = -1
        if(self.State == "IDLE"):
            ReturnST = 0
        if(self.State == "WAITING"):
            ReturnST = 1
        if(self.State == "RUNNING"):
            ReturnST = 2

        return ReturnST

    def GetCPUUse(self) -> float:

        return self.C/self.Ti

    def Tick(self) -> None:

        if(self.State == "RUNNING"):
            self.RunningTime += 1

            if(self.RunningTime == self.C):

                self.State = "IDLE"
                self.RunningTime = 0


        if(self.PeriodRemaining == 0):

            if(self.State == "WAITING"):
                print("ERROR JOB NOT SCHEDULED")
            self.State = "WAITING"
            self.PeriodRemaining = self.Ti
            
        self.PeriodRemaining -= 1


            