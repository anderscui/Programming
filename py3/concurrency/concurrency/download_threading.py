import requests
import threading
import time

from concurrent.futures import ThreadPoolExecutor

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as resp:
        print(f'read {len(resp.content)} from {url}')


def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == '__main__':
    sites = ['https://realpython.com/',
             'https://www.cnblogs.com/'] * 10

    start = time.time()
    download_all_sites(sites)
    elapsed = time.time() - start
    # downloaded 20 in 1.5748848915100098 seconds.
    print(f'downloaded {len(sites)} in {elapsed} seconds.')
