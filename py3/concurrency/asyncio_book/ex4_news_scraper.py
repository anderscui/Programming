# coding=utf-8
from asyncio import gather, create_task
from string import Template

from aiohttp import web, ClientSession
from bs4 import BeautifulSoup


async def news_fetch(url, postprocess):
    proxy_url = (
        f'http://localhost:8050/render.html?url={url}&timeout=60&wait=1'
    )
    async with ClientSession() as session:
        async with session.get(proxy_url) as resp:
            data = await resp.read()
            data = data.decode('utf-8')
    return postprocess(url, data)


def cnblogs_articles(url, page_data):
    soup = BeautifulSoup(page_data, 'lxml')
    headlines = soup.find_all('a', class_='post-item-title')
    return [(hl['href'], hl.text, 'cnblogs') for hl in headlines]


def csdn_articles(url, page_data):
    soup = BeautifulSoup(page_data, 'lxml')
    def match(tag):
        return tag.has_attr('href') \
               and tag['href'].startswith('https://blog.csdn.net') \
               and tag.has_attr('data-report-click') \
               and '精选头条' in tag['data-report-click']

    headlines = soup.find_all(match)
    return [(hl['href'], hl.p.text, 'csdn') for hl in headlines]


async def news(request):
    sites = [('https://www.cnblogs.com/', cnblogs_articles),
             ('https://www.csdn.net/', csdn_articles)]
    tasks = [create_task(news_fetch(*s)) for s in sites]
    await gather(*tasks)

    items = {
        text: (f'<div class="box {kind}">'
               f'<span>'
               f'<a href="{href}">{text}</a>'
               f'</span>'
               f'</div>')
        for task in tasks for href, text, kind in task.result()
    }
    content = ''.join(items[x] for x in sorted(items))

    page = Template(open('index.html').read())
    return web.Response(
        body=page.safe_substitute(body=content),
        content_type='text/html'
    )

app = web.Application()
app.router.add_get('/news', news)
web.run_app(app, port=8080)
