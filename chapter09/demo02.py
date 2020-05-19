"""
@author: shoo Wang
@contact: wangsuoo@foxmail.com
@file: demo02.py
@time: 2020/5/19 0019
"""

# 多线程爬虫
import requests as req
from lxml import etree
import urllib
import threading
import time

lock = threading.Lock()
IMG_LIST = []
URL_LIST = []
flag = 0


# 生成爬取目标网站的链接
def getUrlList(num):
    base_url = 'https://www.doutula.com/photo/list/?page='
    for i in range(1, num + 1):
        x = base_url + str(i)
        URL_LIST.append(x)


# 获取网站的文本数据 url 为单个页面
def product():
    while URL_LIST:
        # 拿到这一页的地址
        url = URL_LIST.pop()
        html = etree.HTML(urlToText(url))
        img_url = html.xpath('//div[@class="page-content text-center"]//img/@data-original')
        # 获取线程锁
        lock.acquire()
        print('生产者将一页中的图片地址放进资源池')
        for img in img_url:
            # 对于每一页中的每一个图片都把他放进去
            IMG_LIST.append(img)
        lock.release()


# 将页的地址转为 text 格式
def urlToText(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'}
    resp = req.get(url, headers=header)
    resp.encoding = 'utf-8'
    return resp.text


def customer():
    global flag
    while True:
        if len(IMG_LIST) is 0:
            if flag:
                print('资源池中的数据已取完')
                break
            pass
        else:
            # 获取线程锁
            lock.acquire()
            img = IMG_LIST.pop()
            # 改完之后释放锁
            lock.release()
            fileName = img.split('/')[-1]
            path = './image/' + fileName
            urllib.request.urlretrieve(img, path)


def run_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('爬取成功! 请查阅当前目录下的 image 文件夹, 耗时: ', end-start, 's')
    return wrapper()


@run_time
def run():
    # 爬取的页数
    getUrlList(1)
    thrPros = []
    thrCuss = []
    for i in range(2):
        thrPro = threading.Thread(target=product)
        thrPro.start()
        thrPros.append(thrPro)
    for i in range(8):
        thrCus = threading.Thread(target=customer)
        thrCus.start()
        thrCuss.append(thrCus)
    for thPro in thrPros:
        thPro.join()
    '''
        ? 为什么 flag 要放在这里:
            - 他前面的是生产者线程的join方法,该方法执行完了则代表生产者线程肯定全部执行完了
            - 因为 join 相当于线程阻塞,只执行该线程,不执行其他线程
            - 肯定执行完了之后那 IMG 中肯定有数据,那么同时在执行的消费者肯定可以直接获取到
            - 如果这个时候还是空,那只有可能是他自己消耗完了,因为人家刚刚给你制造了那么多 IMG,不可能没有
            - 如果放在生产者的 join 方法前面的话,则可能生产者还没来得及制造资源
    '''
    global flag
    flag = 1
    for thCus in thrCuss:
        thCus.join()
