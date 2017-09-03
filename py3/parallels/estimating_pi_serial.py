# coding=utf-8
"""Estimate Pi using blocks of serial work on 1 CPU."""
import time
import numpy as np


def estimate_nbr_points_in_quarter_circle(nbr_samples):
    np.random.seed()
    xs = np.random.uniform(0.0, 1.0, nbr_samples)
    ys = np.random.uniform(0.0, 1.0, nbr_samples)

    points_in_quarter_circle = (xs*xs + ys*ys) <= 1
    return sum(points_in_quarter_circle)


if __name__ == '__main__':
    nbr_samples_in_total = 1e7
    nbr_parallel_blocks = 4

    nbr_samples_per_worker = int(nbr_samples_in_total/nbr_parallel_blocks)
    print('Making {} samples per worker'.format(nbr_samples_per_worker))

    t1 = time.time()
    nbr_in_circle = 0
    for npb in range(nbr_parallel_blocks):
        nbr_in_circle += estimate_nbr_points_in_quarter_circle(nbr_samples_per_worker)

    print('Took {}s'.format(time.time() - t1))

    pi_estimate = nbr_in_circle/nbr_samples_in_total*4
    print('Estimated pi', pi_estimate)
    print('pi', np.pi)
