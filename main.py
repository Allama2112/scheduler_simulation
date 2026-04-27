from scheduler import priority_scheduler

from scheduler import SJF
from scheduler import FCFS

from stats import Stats
from process import Process



def initprocess():
    return [
        Process(1, 0, 2),
        Process(2, 1, 1),
        Process(3, 2, 3),
        Process(4, 3, 2),
        Process(5, 4, 1),
        Process(6, 5, 1),
        Process(7, 6, 1),
        Process(8, 7, 1),
        Process(9, 8, 1),
        Process(10, 9, 1),
        Process(11, 10, 1),
        Process(12, 11, 1),
        Process(13, 12, 1),
        Process(14, 13, 1),
        Process(15, 14, 1),
        Process(16, 15, 1),
        Process(17, 16, 1),
        Process(18, 17, 1),
        Process(19, 18, 1),
        Process(20, 19, 1),
    ]

stats = Stats()

#####

#processes = initprocess()
#SFJ(processes)
#stats.record("Shortest Job First", processes)

#processes = initprocess()
#FCFS(processes)
#stats.record("First Come First Serve", processes)

processes = initprocess()
priority_scheduler(processes)
stats.record("Priority", processes)



stats.report()