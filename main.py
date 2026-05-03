from process import Process
from scheduler import fcfs, sjf, priority
from simulation import run_simulation
from stats import Stats

# Create processes
processes = [
    Process(pid=1, arrival_time=0, priority=3),
    Process(pid=2, arrival_time=2, priority=1),
    Process(pid=3, arrival_time=4, priority=4),
    Process(pid=4, arrival_time=6, priority=2),
    Process(pid=5, arrival_time=8, priority=5),
    Process(pid=6, arrival_time=10, priority=7),
    Process(pid=7, arrival_time=12, priority=6),
    Process(pid=8, arrival_time=14, priority=10),
    Process(pid=9, arrival_time=16, priority=9),
    Process(pid=10, arrival_time=18, priority=11),
    Process(pid=11, arrival_time=20, priority=8),
    Process(pid=12, arrival_time=22, priority=15),
    Process(pid=13, arrival_time=24, priority=14),
    Process(pid=14, arrival_time=26, priority=12),
    Process(pid=15, arrival_time=28, priority=13),
]

stats = Stats()

for algorithm_name, scheduler_fn in [('FCFS', fcfs), ('SJF', sjf), ('Priority', priority)]:
    for p in processes:
        p.reset()
    run_simulation(processes, scheduler_fn)
    stats.record(algorithm_name, processes)

stats.report()
stats.plot_all()