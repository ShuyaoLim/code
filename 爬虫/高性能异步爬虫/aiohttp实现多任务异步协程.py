import requests
import asyncio
import time
import aiohttp
start=time.time()
urls=[
    'http://127.0.0.1:5000/yuyuan',
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/yao'
]
async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            page_text=await response.text()
            print(page_text)
tasks=[]
for url in urls:
    c = get_page(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end=time.time()
print('总耗时',end-start)