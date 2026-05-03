from process import Process
from scheduler import fcfs, sjf, priority
from simulation import run_simulation
from stats import Stats

# Create processes once
processes = [
    Process(pid=1, arrival_time=0, priority=3),
    Process(pid=2, arrival_time=2, priority=1),
    Process(pid=3, arrival_time=4, priority=4),
    Process(pid=4, arrival_time=6, priority=2),
    Process(pid=5, arrival_time=8, priority=5),
]

stats = Stats()

for algorithm_name, scheduler_fn in [('FCFS', fcfs), ('SJF', sjf), ('Priority', priority)]:
    for p in processes:
        p.reset()
    run_simulation(processes, scheduler_fn)
    stats.record(algorithm_name, processes)

stats.report()
stats.plot_all()