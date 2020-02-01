import random
import sys

import numpy as np

from mpi4py import MPI

"""
Parallel computation using Collective Communication Operations (CCO)
within Python objects exposing memory buffers (requires NumPy).
usage::
    $ mpiexec -n <nprocs> python file.py
"""

np.set_printoptions(threshold=sys.maxsize, precision=2, suppress=True)


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 1024
chunk = n / size
B = np.zeros(shape=(1, 100))

def generate_input_file():
    f = open('in.txt', 'w')
    for i in range(n):
        f.write('{}\n'.format(random.randrange(0, 100)))

    f.close()

if rank == 0:
    generate_input_file()
    numbers = []
    with open('in.txt') as f:
        numbers = [line.rstrip() for line in f]
else:
    numbers = None


start = MPI.Wtime()

numbers = comm.bcast(numbers, root=0)

for i in range(int(chunk * rank), int(chunk * (rank+1))):
    for j in range(100):
        if int(numbers[i]) == j:
            B[0][j] += 1


if rank != 0:
    comm.send(B, dest=0, tag=rank)

if rank == 0:
    for rank_num in range(1, size):
        B = np.add(B, comm.recv(source=rank_num, tag=MPI.ANY_TAG))

end = MPI.Wtime()

MPI.Finalize()


if rank == 0:
    # print(B)
    print("\nTotal TIME:", end - start)