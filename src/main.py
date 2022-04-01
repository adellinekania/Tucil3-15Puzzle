from branchBoundPuzzle import findKurang, solve15Puzzle, printTreeData
from treePuzzle import Tree
from colorama import Fore
from queue import PriorityQueue

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

from generatePuzzle import read15PuzzleFromFile, createRandomPuzzle

inputType = input(f"{Fore.WHITE}Jenis Input Data 15 Puzzle yang Diberikan:\n1. File\n2. Random{Fore.LIGHTCYAN_EX}\n(Pilih 1 atau 2){Fore.YELLOW}\n>>> ")

if int(inputType) == 1 :
    filepath = input(f"\n{Fore.WHITE}Masukkan path file...\n{Fore.LIGHTCYAN_EX}(ex: ./test/tes1solved.txt)\n{Fore.YELLOW}>>> ")
    data = read15PuzzleFromFile(filepath)
else:
    data = createRandomPuzzle()

rootTree = Tree(data, None, 0, None)
print(f"{Fore.LIGHTCYAN_EX}\n15 Puzzle yang Dihasilkan:{Fore.WHITE}")
printTreeData(rootTree.data)
print(f"{Fore.WHITE}Jumlah Nilai Kurang: {Fore.LIGHTYELLOW_EX}{findKurang(rootTree.data)}\n")

queueTree = []

solutionTree = []
if (findKurang(data) % 2 == 0):
    solve15Puzzle(rootTree, rootTree, queueTree, solutionTree, 0)
else:
    print(f"{Fore.LIGHTRED_EX}15 Puzzle Tidak Bisa Diselesaikan....{Fore.WHITE}")
