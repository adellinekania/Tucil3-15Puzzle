from generatePuzzle import read15PuzzleFromFile, createRandomPuzzle
from branchBoundPuzzle import findKurang, printTreeData, solve15Puzzle
from treePuzzle import Tree
from colorama import Fore
from queue import PriorityQueue
import time

print(f'''{Fore.LIGHTCYAN_EX}
  █████████████████████████████████████████████████████████████
  █▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─▄▄─█
  ██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█████─███─██─█
  ▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀
''')

print(f'''{Fore.LIGHTYELLOW_EX}
░░███╗░░███████╗  ██████╗░██╗░░░██╗███████╗███████╗██╗░░░░░███████╗
░████║░░██╔════╝  ██╔══██╗██║░░░██║╚════██║╚════██║██║░░░░░██╔════╝
██╔██║░░██████╗░  ██████╔╝██║░░░██║░░███╔═╝░░███╔═╝██║░░░░░█████╗░░
╚═╝██║░░╚════██╗  ██╔═══╝░██║░░░██║██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░
███████╗██████╔╝  ██║░░░░░╚██████╔╝███████╗███████╗███████╗███████╗
╚══════╝╚═════╝░  ╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝╚══════╝╚══════╝
''')

print(f'''{Fore.LIGHTRED_EX}
===================================================================
{Fore.WHITE}
           Tugas Kecil 3 IF2211 Strategi Algoritma
          Adelline Kania Setiyawan / 13520084 / K03
{Fore.LIGHTRED_EX}
===================================================================
''')


# Meminta input dari pengguna berupa data puzzle dari file atau random
inputType = input(f"{Fore.WHITE}Jenis Input Data 15 Puzzle yang Diberikan:\n1. File\n2. Random{Fore.LIGHTCYAN_EX}\n(Pilih 1 atau 2){Fore.YELLOW}\n>>> ")

if int(inputType) == 1 :
    filepath = input(f"\n{Fore.WHITE}Masukkan path file...\n{Fore.LIGHTCYAN_EX}(ex: ./tes/solved1.txt)\n{Fore.YELLOW}>>> ")
    data = read15PuzzleFromFile(filepath)
else:
    data = createRandomPuzzle()


# Menampilkan 15 Puzzle yang dihasilkan beserta nilai kurangnya
print(f"{Fore.LIGHTCYAN_EX}\n15 Puzzle yang Dihasilkan:{Fore.WHITE}")
printTreeData(data)
print(f"{Fore.WHITE}Jumlah Nilai Kurang: {Fore.LIGHTYELLOW_EX}{findKurang(data)}\n")


# Apabila nilai kurang berjumlah genap, maka akan dicarikan solusi dari 15 Puzzle
if (findKurang(data) % 2 == 0):
    # Menginisiasi sebuah kelas Tree untuk menampung semua kemungkinan Tree yang terbentuk
    rootTree = Tree(data, None, 0, None)

    # Membuat suatu priority queue untuk menampun semua kemungkinan solusi matriks
    # yang terurut berdasarkan nilai cost suatu matriks
    queueTree = PriorityQueue()
    queueTree.put((rootTree.countC, 0, rootTree))

    # Memanggil prosedur solve15Puzzle untuk menyelesaikan 15 Puzzle
    startTime = time.time()
    solve15Puzzle(queueTree)
    finishTime = time.time()
    print("Total Waktu Eksekusi: {:.5f} sekon".format(finishTime - startTime))
    print()

# Apabila nilai kurang berjumlah ganjil, maka akan ditampilkan pesan bahwa 15 Puzzle tidak bisa diselesaikan
else:
    print(f"{Fore.LIGHTRED_EX}15 Puzzle Tidak Bisa Diselesaikan....{Fore.WHITE}")