from typing import Sequence, NamedTuple, List
import numpy as np


class Job(NamedTuple):
    id: int
    times: Sequence[int]

    def __eq__(self, other):
        return self.id == other.id

class Scheduler:

    def __init__(self, jobs: List[Job]) -> None:
        self.jobs = jobs

    def sim_annealing(self, initial_temp=100000, wychladzanie = 0.95, iterations=10000, swap_or_insert='insert', equalCmax=True):
        jobs = self.jobs.copy()
        if swap_or_insert == 'insert':
            swap_or_insert = random_insert
        else:
            swap_or_insert = random_swap

        for i in range(iterations):
            job_new = swap_or_insert(jobs)
            makespan = get_makespan(jobs)
            next_makespan = get_makespan(job_new)
            if not equalCmax and makespan == next_makespan:
                continue
            if (np.random.uniform(0, 1)
                < np.exp((makespan - next_makespan) / initial_temp)):
                jobs = job_new
                initial_temp *= wychladzanie
        solution_order = [job.id + 1 for job in jobs]
        print('kolejnosc:', solution_order)
        print('Cmax:', makespan)
        return get_makespan(jobs), solution_order

# losowo zamien 2 elementy miejscami
def random_swap(source_list: list):
    result_list = source_list.copy()
    x, y = (np.random.randint(len(source_list)), np.random.randint(len(source_list)))
    result_list[x], result_list[y] = result_list[x], result_list[y]
    return result_list

#losowo wyciagnij element i wstaw go do listy
def random_insert(source_list: list):
    result_list = source_list.copy()
    tmp = result_list.pop(np.random.randint(len(result_list)))
    result_list.insert(np.random.randint(len(result_list)), tmp)
    return result_list

def get_makespan(job_list: Sequence[Job]) -> int:
    times_arr = np.array([job.times for job in job_list])
    machine_times = count_job_times(times_arr)
    return machine_times[-1][-1]


def count_job_times(times_array: np.ndarray) -> np.ndarray:
    job_count, machine_count = times_array.shape
    makespan_array = np.pad(times_array, ((1, 0), (1, 0)), 'constant')
    for i in range(1, job_count + 1):
        for j in range(1, machine_count + 1):
            makespan_array[i, j] = max(makespan_array[i - 1, j], makespan_array[i, j - 1]) + makespan_array[i, j]
    return makespan_array