"""
stats.py

Contains the Stats class, which will hold information about the stats of a process

record function will:
    Track waiting and turnaround times for all processes
    Calculate average waiting and average turnaround times

report function is a placeholder to print out information about the processes.
    Later functions will allow for graphing

"""

class Stats:
    def __init__(self):
        self.results = {}

    def record(self, algorithm, processes):
        waiting_times = [p.waiting_time for p in processes]
        turnaround_times = [p.completion_time - p.arrival_time for p in processes]

        self.results[algorithm] = {
            "avg_waiting_time": sum(waiting_times)/len(waiting_times),
            "avg_turnaround_time": sum(turnaround_times)/len(turnaround_times),
            "waiting_times": waiting_times,
            "turnaround_times": turnaround_times
        }

    def report(self):
        # Placeholder, will create graphs later
        print("Results:\n\n")
        for algorithm, data in self.results.items():
            print(f"Algorithm: {algorithm}")
            print(f"Average Waiting Time: {data['avg_waiting_time']:.2f} ticks")
            print(f"Average Turnaround Time: {data['avg_turnaround_time']:.2f} ticks\n")

            best = min(self.results, key=lambda a: self.results[a]['avg_waiting_time'])
            print(f"Lowest average wait: {best}")

    def get(self, algorithm):
        return self.results.get(algorithm, None)