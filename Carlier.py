from typing import List, Optional
import numpy as np

class Job:
    def __init__(self, id: int, prep: int, exec: int, dlvr: int):
        self.id = id
        self.prep = prep
        self.exec = exec
        self.dlvr = dlvr

    def __eq__(self, other):
        return self.id == other.id



def schrage(jobs: List[Job]) -> List[Job]:
    jobs = jobs.copy()
    time = min(job.prep for job in jobs)
    perm = []
    rd_jobs = []
    while jobs or rd_jobs:
        if jobs:
            rd_jobs.extend(job for job in jobs if job.prep <= time)
            jobs = [job for job in jobs if job not in rd_jobs]
        if not rd_jobs:
            time = min(job.prep for job in jobs)
        else:
            longest = max(job.dlvr for job in rd_jobs)
            longest_job = next(job for job in rd_jobs if job.dlvr == longest)
            rd_jobs.pop(rd_jobs.index(longest_job))
            perm.append(longest_job)
            time += longest_job.exec
    return perm


def schrage_podzial(jobs: List[Job]) -> int:
    makespan = 0
    perm = []
    jobs = jobs.copy()
    time = min(job.prep for job in jobs)
    rd_jobs = []
    current_dlvr = float('inf')
    current_job = jobs[0]
    while jobs or rd_jobs:
        while jobs and min(job.prep for job in jobs) <= time:
            shortest_job = next(job for job in jobs if job.prep == min(job.prep for job in jobs))
            rd_jobs.append(shortest_job)
            jobs = [job for job in jobs if job not in rd_jobs]
            if shortest_job.dlvr > current_dlvr:
                current_job.exec = time - shortest_job.prep
                time = shortest_job.prep
                if current_job.exec > 0:
                    rd_jobs.append(current_job)
        if not rd_jobs:
            time = min(job.prep for job in jobs)
        else:
            longest = max(job.dlvr for job in rd_jobs)
            longest_job = next(job for job in rd_jobs if job.dlvr == longest)
            rd_jobs.pop(rd_jobs.index(longest_job))
            current_job = longest_job
            current_dlvr = current_job.dlvr
            time += longest_job.exec
            makespan = max(makespan, time + longest_job.dlvr)
    return makespan

def carlier(jobs: List[Job]):
    jobs = schrage(jobs)
    cmax = makespan_list(jobs)
    UB = max(cmax)
    b = cmax.argmax()
    a = find_a(jobs, b, UB)
    c = find_c(jobs, a, b)
    if c is None:
        return jobs
    block = jobs[(c+1):(b+1)]
    block_params = finder_par(block)
    jobs[c].prep = max(jobs[c].prep, block_params[0] + block_params[1])
    LB = schrage_podzial(jobs)
    LB = max(sum(block_params), sum(finder_par(block + [jobs[c]])), LB)
    if LB < UB:
        return carlier(jobs)
    jobs[c].dlvr = max(jobs[c].dlvr, block_params[1] + block_params[2])
    LB = schrage_podzial(jobs)
    LB = max(sum(block_params), sum(finder_par(block + [jobs[c]])), LB)
    if LB < UB:
        return carlier(jobs)



def find_a(jobs: List[Job], b_index: int, makespan: int) -> int:
    sumaP = sum(job.exec for job in jobs[:b_index + 1])
    q_max = jobs[b_index].dlvr
    for i, job in enumerate(jobs):
        if job.prep + sumaP + q_max == makespan:
            return i
        sumaP -= job.exec


def find_c(jobs: List[Job], a_index: int, b_index: int) -> Optional[int]:
    highest_dlvr = [index for index, job in enumerate(jobs[a_index:b_index])
                          if job.dlvr < jobs[b_index].dlvr]
    return highest_dlvr[-1] + a_index if highest_dlvr else None


def finder_par(block: List[Job]):
    return (min(job.prep for job in block), sum(job.exec for job in block),
            min(job.dlvr for job in block))


def makespan_list(permutation: List[Job]) -> np.ndarray:
    time = 0
    makespans = []
    for job in permutation:
        job_makespan = max(time, job.prep) + job.exec + job.dlvr
        if job.prep > time:
            time += job.prep - time + job.exec
        else:
            time += job.exec
        makespans.append(job_makespan)
    return np.array(makespans)


def compute_makespan(permutation: List[Job]) -> int:
    makespans = makespan_list(permutation)
    return np.max(makespans)

if __name__ == '__main__':

    #in200
        print()
        print("in200")
        job_data = np.loadtxt('in200.txt', dtype=int, skiprows=0)
        jobs = [Job(job_id, *times) for job_id, times in enumerate(job_data, 1)]
        perm = schrage(jobs)
        makespan = compute_makespan(perm)
   #     print(f'Kolejnosc Schrage            : {[job.id for job in perm]}')
        print(f'Makespan Schrage             : {makespan}')
        perm = carlier(jobs)
    #    print(f'Kolejnosc Schrage z podzialem: {[job.id for job in perm]}')
        print(f'Makespan Schrage z podzialem : {schrage_podzial(jobs)}')
        perm = carlier(jobs)
        makespan = compute_makespan(perm)
     #   print(f'Kolejnosc Carlier            : {[job.id for job in perm]}')
        print(f'Makespan Carlier             : {makespan}')


# In100
        print()
        print("in100")
        job_data = np.loadtxt('in100.txt', dtype=int, skiprows=0)
        jobs = [Job(job_id, *times) for job_id, times in enumerate(job_data, 1)]
        perm = schrage(jobs)
        makespan = compute_makespan(perm)
 #       print(f'Kolejnosc Schrage            : {[job.id for job in perm]}')
        print(f'Makespan Schrage             : {makespan}')
        perm = schrage(jobs)
 #       print(f'Kolejnosc Schrage z podzialem: {[job.id for job in perm]}')
        print(f'Makespan Schrage z podzialem : {schrage_podzial(jobs)}')
        perm = carlier(jobs)
        makespan = compute_makespan(perm)
  #      print(f'Kolejnosc Carlier       : {[job.id for job in perm]}')
        print(f'Makespan Carlier             : {makespan}')
        print()

        print("inmak")
        job_data = np.loadtxt('inmak.txt', dtype=int,skiprows=1)
        jobs = [Job(job_id, *times) for job_id, times in enumerate(job_data, 1)]
        perm = carlier(jobs)
        makespan = compute_makespan(perm)
        print(f'Kolejnosc Carlier       : {[job.id for job in perm]}')
        print(f'Makespan Carlier             : {makespan}')
        print()
        print("inmak3")
        job_data = np.loadtxt('inmak3.txt', dtype=int, skiprows=0)
        jobs = [Job(job_id, *times) for job_id, times in enumerate(job_data, 1)]
        perm = carlier(jobs)
        makespan = compute_makespan(perm)
        print(f'Kolejnosc Carlier       : {[job.id for job in perm]}')
        print(f'Makespan Carlier             : {makespan}')
        print()
        print("inmak5")
        job_data = np.loadtxt('inmak5.txt', dtype=int, skiprows=0)
        jobs = [Job(job_id, *times) for job_id, times in enumerate(job_data, 1)]
        perm = carlier(jobs)
        makespan = compute_makespan(perm)
        print(f'Kolejnosc Carlier       : {[job.id for job in perm]}')
        print(f'Makespan Carlier             : {makespan}')

        print("inmak2")
        job_data = np.loadtxt('inmak2.txt', dtype=int, skiprows=0)
        jobs = [Job(job_id, *times) for job_id, times in enumerate(job_data, 1)]
        perm = carlier(jobs)
        makespan = compute_makespan(perm)
        print(f'Kolejnosc Carlier       : {[job.id for job in perm]}')
        print(f'Makespan Carlier             : {makespan}')

        print("int50")
        job_data = np.loadtxt('in50.txt', dtype=int, skiprows=0)
        jobs = [Job(job_id, *times) for job_id, times in enumerate(job_data, 1)]
        perm = schrage(jobs)
        makespan = compute_makespan(perm)
 #       print(f'Kolejnosc Schrage            : {[job.id for job in perm]}')
        print(f'Makespan Schrage             : {makespan}')
 #       perm = schrage(jobs)
#        print(f'Kolejnosc Schrage z podzialem: {[job.id for job in perm]}')
        print(f'Makespan Schrage z podzialem : {schrage_podzial(jobs)}')
        perm = carlier(jobs)
        makespan = compute_makespan(perm)
      #  print(f'Kolejnosc Carlier            : {[job.id for job in perm]}')
        print(f'Makespan Carlier             : {makespan}')