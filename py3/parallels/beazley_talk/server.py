# coding=utf-8
from socket import *
from threading import Thread
from concurrent.futures import ProcessPoolExecutor as Pool

from beazley import fib

pool = Pool(4)


def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        future = pool.submit(fib, n)
        result = future.result()
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    print('Closed')


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print('Connection', addr)
        Thread(target=fib_handler, args=(client,), daemon=True).start()


fib_server(('', 25000))
