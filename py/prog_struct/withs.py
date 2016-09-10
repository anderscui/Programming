from multiprocessing import Lock

lock = Lock()
with lock:
    print('Lock is held')
