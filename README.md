# banker_algorithm_with_mutex_lock
Write a multithreaded program that implements the banker's algorithm. Create n threads that request and release resources from the bank. The banker will grant the request only if it leaves the system in a safe state. It is important that shared data be safe from concurrent access. To ensure safe access to shared data, you can use mutex locks.



Enter The Number Of The Process To Be Executed:-

5
-------------------------------------------------------------------
Enter The Name Of The Process:-

P0 P1 P2 P3 P4
-------------------------------------------------------------------
Enter The Number of resource:-
3
-------------------------------------------------------------------
Enter The Resource Name:-
R1 R2 R3
-------------------------------------------------------------------
Enter the allocated value of the each process one by one
For process  P0 =>
0 1 0
For process  P1 =>
2 0 0
For process  P2 =>
3 0 2
For process  P3 =>
2 1 1
For process  P4 =>
0 0 2
-------------------------------------------------------------------
Enter the Maximum needed value by the process
For process  P0 =>
7 5 3
For process  P1 =>
3 2 2
For process  P2 =>
9 0 2
For process  P3 =>
2 2 2
For process  P4 =>
4 3 3
-------------------------------------------------------------------
Enter the available resource
3 3 2
Safe sequence is =>
P1 P3 P4 P0 P2



The  thread is now sleeping


Process P1 :
    Allocated     => [0, 1, 0]
    Available     => [3, 3, 2]
    Need          => [1, 2, 2]
    Resource Allocated!  
    Process Code Running..
Thread is finished
    Process Code Completed...
    Process Releasing Resource...
 
    Resource Released!
    New Available => [3, 4, 2]



The  thread is now sleeping

Process P3 :
    Allocated     => [2, 0, 0]

    Available     => [3, 4, 2]
    Need          => [0, 1, 1]
    Resource Allocated!  
    Process Code Running..
Thread is finished
    Process Code Completed...
    Process Releasing Resource...
 
    Resource Released!
    New Available => [5, 4, 2]



The  thread is now sleeping


Process P4 :
    Allocated     => [3, 0, 2]
    Available     => [5, 4, 2]
    Need          => [4, 3, 1]
    Resource Allocated!  
    Process Code Running..
Thread is finished
    Process Code Completed...
    Process Releasing Resource...
 
    Resource Released!
    New Available => [8, 4, 4]



The  thread is now sleeping


Process P0 :
    Allocated     => [2, 1, 1]
    Available     => [8, 4, 4]
    Need          => [7, 4, 3]
    Resource Allocated!  
    Process Code Running..
Thread is finished
    Process Code Completed...
    Process Releasing Resource...
 
    Resource Released!
    New Available => [10, 5, 5]



The  thread is now sleeping

Process
 P2 :
    Allocated     => [0, 0, 2]
    Available     => [10, 5, 5]
    Need          => [6, 0, 0]
    Resource Allocated!  
    Process Code Running..
Thread is finished
    Process Code Completed...
    Process Releasing Resource...
 
    Resource Released!
    New Available => [10, 5, 7]
