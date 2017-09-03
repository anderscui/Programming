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
    use_threads = False

    if use_threads:
        from multiprocessing.dummy import Pool
    else:
        from multiprocessing import Pool

    nbr_samples_in_total = 10**7
    nbr_parallel_blocks = 4

    # pool = Pool(processes=nbr_parallel_blocks)
    nbr_samples_per_worker = nbr_samples_in_total//nbr_parallel_blocks
    print('Making {} samples per worker'.format(nbr_samples_per_worker))

    t1 = time.time()
    pool = Pool()
    map_inputs = [nbr_samples_per_worker] * nbr_parallel_blocks
    results = pool.map(estimate_nbr_points_in_quarter_circle, map_inputs)
    pool.close()
    print('Took {}s'.format(time.time() - t1))

    nbr_in_circle = sum(results)
    combined_nbr_samples = sum(map_inputs)

    pi_estimate = nbr_in_circle/nbr_samples_in_total*4
    print('Estimated pi', pi_estimate)
    print('pi', np.pi)
