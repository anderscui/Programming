# coding=utf-8
import subprocess
from time import time


def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


start = time()
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

for proc in procs:
    proc.communicate()

end = time()
print('Finished in %.3f seconds' % (end - start))
