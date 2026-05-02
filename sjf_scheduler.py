from typing import List
from process import Process

def run_sjf_nonpreemptive(processes: List[Process]) -> List[Process]:
    """
    Non-preemptive SJF:
    - all processes assumed arrival_time == 0
    - choose smallest next CPU burst among ready processes
    - run chosen process to completion of that CPU burst (no preemption)
    """
    if not processes:
        return processes

    time = min(p.arrival_time for p in processes)
    ready = [p for p in processes if p.arrival_time <= time]
    not_arrived = [p for p in processes if p.arrival_time > time]
    blocked = []  # tuples: (process, unblock_time)

    for p in processes:
        p.state = "ready"

    while True:
        # Move newly arrived processes into ready queue
        arrived_now = [p for p in not_arrived if p.arrival_time <= time]
        for p in arrived_now:
            ready.append(p)
        not_arrived = [p for p in not_arrived if p.arrival_time > time]

        # Unblock I/O-completed processes
        newly_ready = []
        for p, unblock_time in blocked:
            if unblock_time <= time:
                p.state = "ready"
                newly_ready.append((p, unblock_time))
                ready.append(p)
        blocked = [(p, t_unblock) for (p, t_unblock) in blocked if (p, t_unblock) not in newly_ready]

        # Done?
        if all(p.state == "terminated" for p in processes):
            break

        # If nothing ready, jump to next unblock time
        if not ready:
            next_times = []
            if blocked:
                next_times.append(min(t_unblock for _, t_unblock in blocked))
            if not_arrived:
                next_times.append(min(p.arrival_time for p in not_arrived))

            if next_times:
                time = min(next_times)
                continue
            else:
                break

        # SJF pick: shortest next CPU burst, tie by pid
        ready.sort(key=lambda p: (p.next_cpu_burst(), p.pid))
        current = ready.pop(0)
        current.state = "running"

        cpu = current.next_cpu_burst()

        # Everyone else waits while current runs
        for p in ready:
            p.waiting_time += cpu

        time += cpu
        io = current.next_io_burst()
        current.cycles_done += 1

        if current.cycles_done >= current.num_cycles:
            current.state = "terminated"
            current.completion_time = time
        else:
            current.state = "blocked"
            blocked.append((current, time + io))

    return processes
