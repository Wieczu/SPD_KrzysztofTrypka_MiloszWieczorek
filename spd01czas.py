from typing import Sequence, List
from spd01zad import Job



def compile_timeline(job_list: Sequence[Job]) -> List[List[int]]:

    machines_count = max(len(job.czas) for job in job_list)

    machine_times = [[] for machine in range(machines_count)]
    machine_times[0].append(0)

    jobs_iter = iter(job_list)
    first_job = next(jobs_iter)

    for machine_index in range(1, machines_count):
        machine_times[machine_index].append(
            machine_times[machine_index - 1][0] + first_job.czas[machine_index - 1]
        )

    prev_job = first_job

    for job_index in range(1, len(job_list)):
        job = job_list[job_index]
        machine_times[0].append(machine_times[0][-1] + prev_job.czas[0])

        for machine_index in range(1, machines_count):
            machine_times[machine_index].append(
                max(machine_times[machine_index - 1][job_index] + job.czas[machine_index - 1],
                    machine_times[machine_index][job_index - 1] + prev_job.czas[machine_index])
            )
        prev_job = job
    return machine_times