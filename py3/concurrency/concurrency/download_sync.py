import requests
import time


def download_site(url, session):
    with session.get(url) as resp:
        print(f'read {len(resp.content)} from {url}')


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == '__main__':
    sites = ['https://realpython.com/',
             'https://www.cnblogs.com/'] * 10

    start = time.time()
    download_all_sites(sites)
    elapsed = time.time() - start
    # downloaded 20 in 5.453153133392334 seconds.
    print(f'downloaded {len(sites)} in {elapsed} seconds.')
