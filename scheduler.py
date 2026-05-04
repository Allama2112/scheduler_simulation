def fcfs(ready_queue):
    return ready_queue[0]

def sjf(ready_queue):
    return min(ready_queue, key=lambda p: p.current_cpu_burst)

def priority(ready_queue):
    return max(ready_queue, key=lambda p: p.priority)