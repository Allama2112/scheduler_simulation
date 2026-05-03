def run_simulation(processes, scheduler_fn):
    time = 0
    completed = []
    ready_queue = []
    blocked = []
    current_process = None

    while len(completed) < len(processes):

        # Put processes in ready queue
        for p in processes:
            if p.state == 'ready' and p.arrival_time <= time and p not in ready_queue:
                ready_queue.append(p)

        # If a blocked process as finished I/O, put it in ready queue
        for p in blocked[:]:
            p.current_io_burst -= 1
            if p.current_io_burst == 0:
                blocked.remove(p)
                p.state = 'ready'
                p.current_cpu_burst = p.next_cpu_burst()
                ready_queue.append(p)

        # If CPU is idle, then assign next process
        if current_process is None and ready_queue:
            current_process = scheduler_fn(ready_queue)
            ready_queue.remove(current_process)
            current_process.state = 'running'

        # Tick the running process
        if current_process:
            current_process.current_cpu_burst -= 1

            if current_process.current_cpu_burst == 0:
                current_process.cycles_done += 1

                # Check if process has more cycles
                if current_process.cycles_done < current_process.num_cycles:
                    # Send to I/O
                    current_process.current_io_burst = current_process.next_io_burst()
                    current_process.state = 'blocked'
                    blocked.append(current_process)
                else:
                    # Terminate
                    current_process.state = 'terminated'
                    current_process.completion_time = time + 1
                    completed.append(current_process)

                current_process = None

        # Increment waiting time
        for p in ready_queue:
            p.waiting_time += 1

        time += 1

    # Return total simulation time
    return time