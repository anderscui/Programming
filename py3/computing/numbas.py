# coding=utf-8
from datetime import datetime
from timeit import timeit

from numba import jit
from numpy import arange


@jit
def sum2d_1(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i, j]
    return result


a = arange(9000000).reshape(3000, 3000)
start = datetime.now()
print(sum2d_1(a))
print(datetime.now() - start)
