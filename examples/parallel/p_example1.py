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

n = 1048576
A = np.empty(shape=(1, n))
chunk = n / size

if rank == 0:
    B = np.random.rand(1, n)
    C = np.random.rand(1, n)
else:
    B = C = None

start = MPI.Wtime()

B = comm.bcast(B, root=0)
C = comm.bcast(C, root=0)

for i in range(int(chunk * rank), int(chunk * (rank+1))):
    A[0][i] = B[0][i] + C[0][i]

if rank != 0:
    comm.send(A, dest=0, tag=rank)

if rank == 0:
    for rank_num in range(1, size):
        A = np.add(A, comm.recv(source=rank_num, tag=MPI.ANY_TAG))

end = MPI.Wtime()

MPI.Finalize()

if rank == 0:
    # print(A)
    print("Total TIME:", end - start)

