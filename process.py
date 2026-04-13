import random

"""
Process.py

Contains the Process class, which will hold information about each process.
This information includes:
    pid: Process ID
    arrival_time: Time of arrival of the process
    priority: The priority of the process
    num_cycles: The number of CPU/IO bursts it need sto complete before terminating

The __init__ function will pre-generate all CPU and IO bursts at the beginning so we don't re-randomize

Other important information:
    state: What state the process is in (ready, running, blocked, terminated)
    cycles_done: How many cycles have been completed

The process will also keep track of their waiting time and completion time.

Functions exist for:
    Checking next CPU/IO burst
    Checking if the process is terminated
    Resetting the process
"""

class Process:
    def __init__(self, pid, arrival_time, priority, num_cycles=4):
        self.pid = pid
        self.arrival_time = arrival_time
        self.priority = priority
        self.num_cycles = num_cycles
    

        # Generating all bursts
        self.cpu_bursts = [random.randint(1, 10) for _ in range(num_cycles)]
        self.io_bursts = [random.randint(1, 20) for _ in range(num_cycles)]

        # State (Ex: ready, running, blocked, terminated)
        self.state = "ready"
        self.cycles_done = 0

        # Burst tracking
        self.current_cpu_burst = self.cpu_bursts[0]
        self.current_io_burst = 0

        # Stats
        self.waiting_time = 0
        self.completion_time = 0

    def next_cpu_burst(self):
        return self.cpu_bursts[self.cycles_done]
    
    def next_io_burst(self):
        return self.io_bursts[self.cycles_done]
    
    def is_terminated(self):
        return self.state == "terminated"
    
    def reset(self):
        self.state = "ready"
        self.cycles_done = 0
        self.current_cpu_burst = self.cpu_bursts[0]
        self.current_io_burst = 0
        self.waiting_time = 0
        self.completion_time = 0