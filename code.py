import threading, time, random
import time
import os 

class color:
   Purple = '\033[95m'
   Cyan = '\033[96m'
   Darkcyan = '\033[36m'
   Blue = '\033[94m'
   Green = '\033[92m'
   Yellow = '\033[93m'
   Red = '\033[91m'
   Bold = '\033[1m'
   Underline = '\033[4m'
   End = '\033[0m'


my_mutex = threading.Lock()

class thread_one(threading.Thread):
    def run(self):
        global my_mutex
        print (color.Bold+color.Green+"The  thread is now sleeping\n"+color.End)
        time.sleep(3)
        print(color.Bold+color.Red+"Thread is finished"+color.End)
        my_mutex.release()


print("Enter The Number Of The Process To Be Executed")
m=int(input())
print("-------------------------------------------------------------------")

print("Enter The Name Of The Process")
Processes=input().strip().split()
print("-------------------------------------------------------------------")

print("Enter The Number of resource")
n=int(input())
print("-------------------------------------------------------------------")

print("Enter The Resource Name")
Resources=input().strip().split()
print("-------------------------------------------------------------------")

Allocated_Value=[]
MaxValue=[]
Need_Value=[]

print("Enter the allocated value of the each process one by one")
for i in range(m):
    print("For process ",Processes[i],"=>")
    Allocated_Value.append(list(map(int,input().strip().split())))
print("-------------------------------------------------------------------")

print("Enter the Maximum needed value by the process")
for j in range(m):
    print("For process ",Processes[j],"=>")
    MaxValue.append(list(map(int,input().strip().split())))
print("-------------------------------------------------------------------")

print("Enter the available resource")    
AvailableValue=list(map(int,input().strip().split()))
AvailableCopy=AvailableValue[:]

for i in range(m):
    a=[]
    for j in range(n):
        a.append(MaxValue[i][j]-Allocated_Value[i][j])
    Need_Value.append(a)
    
NeedCopy=Need_Value[:]    
    
def Executed():
  
    Unable=[]
    Out=1
    for i in range(n):
        Inspect_Value=0
        for j in range(m):
            Inspect_Value+=Allocated_Value[j][i]
        Inspect_Value+=AvailableValue[i]
        CheckPoint=1
        for k in range(m):
            if(MaxValue[k][i]>Inspect_Value):
                CheckPoint=0
                Unable.append(Processes[k])
                break
        if(CheckPoint==0):
            Out=0
    if Out:
        return Unable,1
    else:
        return Unable,0
    
Unable,Inspect_Value=Executed()
if(Inspect_Value==0):
    print("There is no Safe sequence  ")
    print(*Unable," Process can't be executed")
else:
    Safe_Sequence=[]
    while(Inspect_Value and len(Safe_Sequence)<m):
        for i in range(len(Need_Value)):
            if Processes[i] not in Safe_Sequence:
                CheckPoint=1
                for z in range(n):
                    if(Need_Value[i][z]>AvailableValue[z]):
                        CheckPoint=0
                if CheckPoint:
                    
                    for z in range(n):
                        AvailableValue[z]+=Allocated_Value[i][z]
                    Safe_Sequence.append(Processes[i])
    print("Safe sequence is =>")
    print(*Safe_Sequence,sep=" ")
    print("\n\n")

NewAvailable=AvailableCopy
if Inspect_Value==1:
    

    for i in range(len(Safe_Sequence)):
        my_mutex.acquire()

        t1 = thread_one()
        t1.start()
        AllocatedCopy=Allocated_Value[i]
        
        print("\nProcess",Safe_Sequence[i],":")
        j=Processes.index(Safe_Sequence[i])
        print("    Allocated     =>",Allocated_Value[i])
        print("    Available     =>",NewAvailable)
        print("    Need          =>",NeedCopy[j])
        time.sleep(1)
        print("    Resource Allocated!  ") 
        time.sleep(1)
        print("    Process Code Running..")  
        time.sleep(1)
        print("    Process Code Completed...\n    Process Releasing Resource...\n ")
        time.sleep(1)
        print("    Resource Released!")
        for i in range(len(Resources)):
            NewAvailable[i]=AllocatedCopy[i]+NewAvailable[i]
        time.sleep(1)
        print("    New Available =>",NewAvailable)
        print("\n\n")
        time.sleep(2)
    
