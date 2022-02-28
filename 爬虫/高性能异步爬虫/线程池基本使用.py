import time
from multiprocessing.dummy import Pool
start_time=time.time()
def get_page(str):
    print("正在下载:",str)
    time.sleep(2)
    print("下载成功",str)
name_list=['y','aa','b','c']
pool=Pool(4)
pool.map(get_page,name_list)
end_time=time.time()
print(end_time-start_time)
