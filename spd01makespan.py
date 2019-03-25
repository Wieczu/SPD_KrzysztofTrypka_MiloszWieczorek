from typing import Sequence
from spd01zad import Job
from spd01czas import compile_timeline


def get_makespan(job_list: Sequence[Job]) -> int:
    timeline = compile_timeline(job_list)
    return timeline[-1][-1] + job_list[-1].czas[-1]
