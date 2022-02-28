import requests
import asyncio
import time
start=time.time()
urls=[
    'http://127.0.0.1:5000/yuyuan',
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/yao'
]
async def get_page(url):
    print('正在下载',url)
    response=requests.get(url=url)
    print('下载完毕:',response.text)
tasks=[]
for url in urls:
    c = get_page(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end=time.time()
print('总耗时',end-start)

