import asyncio
import time
async def request(url):
    print('正在下载',url)
    await asyncio.sleep(2)
    print('下载完毕',url)
start=time.time()
urls=[
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com'
]
stasks=[]
for url in urls:
    c=request(url)
    task=asyncio.ensure_future(c)
    stasks.append(task)
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(stasks))
print(time.time()-start)
