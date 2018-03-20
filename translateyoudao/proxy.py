import requests
from threading import Thread
from time import sleep

from .settings import PROXY_API_URL, TIMEOUT


def get_proxy_ip(order_no):
    """
    请求无忧代理IP获取API地址，返回新的IP

    这里使用的是无忧IP代理，官网：http://www.data5u.com/，你也可以使用其他的IP代理方案，
    重写这个函数即可

    :param order_no: 无忧IP代理订单号
    """
    api_url = PROXY_API_URL + order_no
    with requests.Session() as s:
        response = s.get(api_url, timeout=TIMEOUT).text
    # 订单号不存在
    if 'false' in response:
        raise ValueError('无忧IP代理订单号无效或设置错误')
    proxy_ip = response.strip('\n')

    return 'http://' + proxy_ip


def flush_proxies(func, args, proxies, sleep_time):
    """
    定时切换代理IP，改变已经存在IP代理字典对象

    :param
        func: 获取代理IP的函数
        args: 获取代理IP函数所需参数
        proxies: IP代理字典
    """
    while True:
        sleep(sleep_time)
        proxy_ip = func(*args)
        proxies['https'] = proxies['http'] = proxy_ip


def get_proxies(func, args, sleep_time=5):
    """
    根据所传入的获取代理IP函数获取代理IP，并构造requests所需格式的IP代理字典，
    并另起一个守护线程每隔5秒更新一次IP代理。

    :param
        func: 获取代理IP的函数
        args: 获取代理IP函数所需参数
        sleep_time: 刷新IP代理的间隔时间，默认5秒
    """
    proxy_ip = func(*args)
    proxies = {}
    proxies['https'] = proxies['http'] = proxy_ip
    t1 = Thread(target=flush_proxies, args=(func, args, proxies, sleep_time), daemon=True)
    t1.start()

    return proxies
