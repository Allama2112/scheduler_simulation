

def FCFS(processes):
    print()

def SJF(processes):
    print()

def priority_scheduler(processes):

    for p in processes:
        p.reset()

    time = 0
    completed = []
    ready_queue = []

    while len(completed) < len(processes):

        for p in processes:
            if p not in completed and p not in ready_queue and p.arrival_time <= time:
                ready_queue.append(p)

        if not ready_queue:
            time += 1
            continue

        ready_queue.sort(key=lambda p: p.priority)
        current = ready_queue.pop(0)

        current.waiting_time = time - current.arrival_time

        cpu_time = current.current_cpu_burst
        time += cpu_time

        current.completion_time = time
        current.state = "terminated"
        completed.append(current)