import asyncio

async def request(url):
    print('正在请求的url是',url)
    print('请求成功',url)
    return url
c=request('www.baidu.com')
#
# loop=asyncio.get_event_loop()
# loop.run_until_complete(c)

#task
# loop=asyncio.get_event_loop()
# task=loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

#future
# loop=asyncio.get_event_loop()
# task=asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)
def callback_func(task):
    print(task.result())
#绑定回调
loop=asyncio.get_event_loop()
task=asyncio.ensure_future(c)
task.add_done_callback(callback_func)
loop.run_until_complete(task)
