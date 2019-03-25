from typing import List
from spd01zad import Job
from itertools import permutations
from spd01makespan import get_makespan


class Scheduler:
    def __init__(self, jobs: List[Job]) -> None:
        self.jobs = jobs

    def complete_review(self):  #optymalna kolejnosc przy uzyciu przeglądu zupełnego
        permutation = list(permutations(self.jobs))
        makespans = []
        for p in permutation:
            makespans.append(get_makespan(p))

        makespan = min(makespans)

        return permutation[makespans.index(makespan)], makespan

    def johnsons_algorithm(self):
        machines_count = max(len(job.czas) for job in self.jobs)
        if machines_count == 3:
            order = self._johnsons3(self.jobs.copy())
        else:
            order = self.johnsons2(self.jobs.copy())
        makespan = get_makespan(order)
        return order, makespan

    @staticmethod
    def johnsons2(jobs: List[Job]):
        begin_list = []
        end_list = []

        while jobs:
            min_time = min(time for job in jobs for time in job.czas)
            shortest_jobs = [job for job in jobs if min_time in job.czas]
            job = shortest_jobs[0]
            job_index = jobs.index(job)
            machine_index = job.czas.index(min_time)
            if machine_index == 0:
                begin_list.append(jobs.pop(job_index))
            else:
                end_list.insert(0, jobs.pop(job_index))

        return begin_list + end_list


    def _johnsons3(self, jobs):
        johnson3 = [
            Job(job.nr, (job.czas[0] + job.czas[1], job.czas[1] + job.czas[2]))
            for job in jobs
        ]
        return self.johnsons2(johnson3)


