# banker_algorithm_with_mutex_lock
Write a multithreaded program that implements the banker's algorithm. Create n threads that request and release resources from the bank. The banker will grant the request only if it leaves the system in a safe state. It is important that shared data be safe from concurrent access. To ensure safe access to shared data, you can use mutex locks.



Enter The Number Of The Process To Be Executed
3
-------------------------------------------------------------------
Enter The Name Of The Process
a s d
-------------------------------------------------------------------
Enter The Number of resource
2
-------------------------------------------------------------------
Enter The Resource Name
d f
-------------------------------------------------------------------
Enter the allocated value of the each process one by one
For process  a =>
2 3
For process  s =>
3 4
For process  d =>
3 4
-------------------------------------------------------------------
Enter the Maximum needed value by the process
For process  a =>
5 6
For process  s =>
4 5
For process  d =>
5 6
-------------------------------------------------------------------
Enter the available resource
90 90
Safe sequence is =>
a s d



The  thread is now sleeping


Process a :
    Allocated     => [2, 3]
    Available     => [90, 90]
    Need          => [3, 3]
    Resource Allocated!  
    Process Code Running..
Thread is finished
    Process Code Completed...
    Process Releasing Resource...
 
    Resource Released!
    New Available => [92, 93]



The  thread is now sleeping

Process s :
    Allocated     => [3, 4]
    Available     => [92, 93]
    Need          => [1, 1]
    Resource Allocated!  
    Process Code Running..
Thread is finished
    Process Code Completed...
    Process Releasing Resource...
 
    Resource Released!
    New Available => [95, 97]



The  thread is now sleeping

Process d :
    Allocated     => [3, 4]
    Available     => [95, 97]
    Need          => [2, 2]

    Resource Allocated!  
    Process Code Running..
Thread is finished
    Process Code Completed...
    Process Releasing Resource...
 
    Resource Released!
    New Available => [98, 101]
