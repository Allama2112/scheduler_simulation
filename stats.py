import matplotlib.pyplot as plt
import numpy as np

class Stats:
    def __init__(self):
        self.results = {}

    def record(self, algorithm, processes):
        waiting_times = [p.waiting_time for p in processes]
        turnaround_times = [p.completion_time - p.arrival_time for p in processes]

        self.results[algorithm] = {
            'avg_waiting_time': sum(waiting_times) / len(waiting_times),
            'avg_turnaround_time': sum(turnaround_times) / len(turnaround_times),
            'waiting_times': waiting_times,
            'turnaround_times': turnaround_times,
            'process_ids': [p.pid for p in processes]
        }

    def report(self):
        print("\n===== SCHEDULER SIMULATION RESULTS =====\n")
        for algorithm, data in self.results.items():
            print(f"Algorithm: {algorithm}")
            print(f"  Avg Waiting Time:     {data['avg_waiting_time']:.2f} ticks")
            print(f"  Avg Turnaround Time:  {data['avg_turnaround_time']:.2f} ticks")
            print()

        best = min(self.results, key=lambda a: self.results[a]['avg_waiting_time'])
        print(f"Best performing algorithm (lowest avg wait): {best}")

    def get(self, algorithm):
        return self.results.get(algorithm, None)

    def plot_waiting_times(self):
        algorithms = list(self.results.keys())
        process_ids = self.results[algorithms[0]]['process_ids']
        x = np.arange(len(process_ids))
        bar_width = 0.25

        fig, ax = plt.subplots(figsize=(10, 6))

        for i, algorithm in enumerate(algorithms):
            waiting_times = self.results[algorithm]['waiting_times']
            ax.bar(x + i * bar_width, waiting_times, bar_width, label=algorithm)

        ax.set_xlabel('Process ID')
        ax.set_ylabel('Waiting Time (ticks)')
        ax.set_title('Waiting Time per Process by Algorithm')
        ax.set_xticks(x + bar_width)
        ax.set_xticklabels([f'P{pid}' for pid in process_ids])
        ax.legend()
        plt.tight_layout()
        plt.savefig('waiting_times.png')
        plt.show()

    def plot_turnaround_times(self):
        algorithms = list(self.results.keys())
        process_ids = self.results[algorithms[0]]['process_ids']
        x = np.arange(len(process_ids))
        bar_width = 0.25

        fig, ax = plt.subplots(figsize=(10, 6))

        for i, algorithm in enumerate(algorithms):
            turnaround_times = self.results[algorithm]['turnaround_times']
            ax.bar(x + i * bar_width, turnaround_times, bar_width, label=algorithm)

        ax.set_xlabel('Process ID')
        ax.set_ylabel('Turnaround Time (ticks)')
        ax.set_title('Turnaround Time per Process by Algorithm')
        ax.set_xticks(x + bar_width)
        ax.set_xticklabels([f'P{pid}' for pid in process_ids])
        ax.legend()
        plt.tight_layout()
        plt.savefig('turnaround_times.png')
        plt.show()

    def plot_averages(self):
        algorithms = list(self.results.keys())
        avg_waiting = [self.results[a]['avg_waiting_time'] for a in algorithms]
        avg_turnaround = [self.results[a]['avg_turnaround_time'] for a in algorithms]
        x = np.arange(len(algorithms))
        bar_width = 0.35

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(x - bar_width / 2, avg_waiting, bar_width, label='Avg Waiting Time')
        ax.bar(x + bar_width / 2, avg_turnaround, bar_width, label='Avg Turnaround Time')

        ax.set_xlabel('Algorithm')
        ax.set_ylabel('Ticks')
        ax.set_title('Average Waiting Time vs Turnaround Time by Algorithm')
        ax.set_xticks(x)
        ax.set_xticklabels(algorithms)
        ax.legend()
        plt.tight_layout()
        plt.savefig('averages.png')
        plt.show()

    def plot_all(self):
        self.plot_waiting_times()
        self.plot_turnaround_times()
        self.plot_averages()