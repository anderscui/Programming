import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as resp:
        proc_name = multiprocessing.current_process().name
        print(f'{proc_name} - {id(session)} read {len(resp.content)} from {url}')


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == '__main__':
    sites = ['https://realpython.com/',
             'https://www.cnblogs.com/'] * 10

    start = time.time()
    download_all_sites(sites)
    elapsed = time.time() - start
    # downloaded 20 in 2.4319159984588623 seconds.
    print(f'downloaded {len(sites)} in {elapsed} seconds.')
