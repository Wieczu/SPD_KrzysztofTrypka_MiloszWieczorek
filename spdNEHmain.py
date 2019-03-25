from spdNEH import neh
import wczyt

nbm, nbj, p_ij = wczyt.read_from_file("example3.txt")
seq, cmax = neh(p_ij, nbm, nbj)
print("Ilosc Maszyn:", nbm)
print("Ilość Zadanń:", nbj)
print(" ")
print("Czas przetwarzania zadań(Wiersz maszyny, kolumna zadania)\n", p_ij)
print("NEH: \n","Kolejność Wykonywania Zadań: ", seq, "Cmax", cmax)
