import wczyt


def sum_processing_time(index_job, data, nb_machines):
    sum_p = 0
    for i in range(nb_machines):
        sum_p += data[i][index_job]
    return sum_p


def order_neh(data, nb_machines, nb_jobs):
    my_seq = []
    for j in range(nb_jobs):
        my_seq.append(j)
    return sorted(my_seq, key=lambda x: sum_processing_time(x, data, nb_machines), reverse=True)


def insertion(sequence, index_position, value):
    new_seq = sequence[:]
    new_seq.insert(index_position, value)
    return new_seq


def neh(data, nb_machines, nb_jobs):
    order_seq = order_neh(data, nb_machines, nb_jobs)
    seq_current = [order_seq[0]]
    for i in range(1, nb_jobs):
        min_cmax = float("inf")
        for j in range(0, i + 1):
            tmp_seq = insertion(seq_current, j, order_seq[i])
            cmax_tmp = wczyt.makespan(tmp_seq, data, nb_machines)[nb_machines -1 ][len(tmp_seq)]
            print("Kolejność Wykonywania Zadań :", tmp_seq," | ", "Cmax: ", cmax_tmp)
            if min_cmax > cmax_tmp:
                best_seq = tmp_seq
                min_cmax = cmax_tmp
        seq_current = best_seq
    return seq_current, wczyt.makespan(seq_current, data, nb_machines)[nb_machines - 1][nb_jobs]


