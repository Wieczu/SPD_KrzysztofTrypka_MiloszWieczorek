from spd01s import Scheduler
from spd01zad import Job


if __name__ == '__main__':
    jobs = [Job(0, (3, 4)), Job(1, (5, 8)), Job(2, (5, 7)), Job(3, (2, 4)), Job(4, (2, 2))]
    sched = Scheduler(jobs)
    print('Dwie maszyny: ')
    print("Algorytm Johnsona ", sched.johnsons_algorithm())
    print("Przegląd zupełny ", sched.complete_review())
    print(" ")
    print(" ")

    jobs = [Job(0, (3, 2, 1)), Job(1, (2, 8, 4)), Job(2, (5, 1, 1)), Job(3, (4, 5, 6)), Job(4, (7, 8, 9))]
    sched = Scheduler(jobs)
    print('Trzy Maszyny: ')
    print("Algorytm Johnsona: ", sched.johnsons_algorithm())
    print("Przegląd zupełny ", sched.complete_review())