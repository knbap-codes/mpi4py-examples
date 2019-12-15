import numpy as np
import random

from mpi4py import MPI

"""
Parallel computation using Collective Communication Operations (CCO)
within Python objects exposing memory buffers (requires NumPy).
usage::
  $ mpiexec -n <nprocs> python cpi-buf.py
"""

def get_n():
    n = 1048576
    return n

def add_vectors(n, myrank=0, nprocs=0):
    pass
    
def print_result():
    pass


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

A = []
B = []
C = []

n = 1048576
# n = 8

# sendbuf = None

# if myrank == 0:
#     # for i in range(n):
#     #     B.append(random.random())
#     #     C.append(random.random())
#     sendbuf = np.empty([nprocs, 100], dtype='i')
#     sendbuf.T[:,:] = range(nprocs)

# recvbuf = np.empty(100, dtype='i')

# # data = comm.scatter(B, root=0)
# data = comm.scatter(sendbuf, recvbuf, root=0)
# assert np.allclose(recvbuf, rank)


# print('Rank: ', myrank, 'data: ', data)

if rank == 0:
    for i in range(n):
        B.append(random.random())
        C.append(random.random())
        # B.append(random.randint(0, 3))
        # C.append(random.randint(0, 3))

# dividing data into chunks
    chunks_B = [[] for _ in range(size)]
    for i, chunk in enumerate(B):
        chunks_B[i % size].append(chunk)
    chunks_C = [[] for _ in range(size)]
    for i, chunk in enumerate(C):
        chunks_C[i % size].append(chunk)
else:
    B = None
    C = None
    chunks_B = None
    chunks_C = None

start = MPI.Wtime()

data_B = comm.scatter(chunks_B, root=0)
data_C = comm.scatter(chunks_C, root=0)

# print('\nRank:', rank, 'Data B:', data_B, 'Data C:', data_C, '\n')

for i in range(len(data_B)):
    A.append(data_B[i] + data_C[i])


# print('\nA: ', A, '\n')


A = comm.gather(A)

end = MPI.Wtime()


if rank == 0:
    # print(A)
    print(A[0][0])
    print("Start time:",start)
    print("End time:", end)
    print("Total TIME:", end - start)

# B = np.array([])
# C = np.array([])
# B = []
# C = []
# A = []
# for i in range(1048576):
#     B.append(random.random())
#     C.append(random.random())

# # print(B)

# for i in range(1048576):
#     A.append(B[i] + C[i])


# print(A[0])