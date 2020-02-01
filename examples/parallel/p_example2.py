import math
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


if rank == 0:
    A = np.random.rand(1, n)
else:
    A = None

start = MPI.Wtime()

A = comm.bcast(A, root=0)

total_proc_sum = 0

for i in range(int(chunk * rank), int(chunk * (rank+1))):
    square = A[0][i]**2
    total_proc_sum += square

if rank != 0:
    comm.send(total_proc_sum, dest=0, tag=rank)

if rank == 0:
    for rank_num in range(1, size):
        total_proc_sum += comm.recv(source=rank_num, tag=MPI.ANY_TAG)
        
end = MPI.Wtime()

MPI.Finalize()

if rank == 0:
    # print(math.sqrt(total_proc_sum))
    print("Total TIME:", end - start)