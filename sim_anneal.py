from SA import Job, Scheduler
import wczyt
import numpy as np


np.seterr(all="ignore")

if __name__ == '__main__':
#    nbm, nbj, p_ij = wczyt.read_from_file("example4.txt")
    job_data = np.loadtxt('example4.txt', dtype=int, skiprows=2)
    jobs = [Job(job_id, times) for job_id, times in enumerate(job_data)]
    sched = Scheduler(jobs)
    print(" Wyżarzanie ")
    print(" ")
#    print("Ilosc Maszyn:", nbj)
#   print("Ilość Zadanń:", nbm)
    makespans = [sched.sim_annealing(equalCmax=True)[0] for _ in range(1)]
    print('Średnia: ',  sum(makespan for makespan in makespans) / len(makespans))
    print('')
    print('Rożne Cmax`y:')
    makespans = [sched.sim_annealing(equalCmax=False)[0] for _ in range(1)]
    print('Średnia(różne Cmax`y): ', sum(makespan for makespan in makespans) / len(makespans))


