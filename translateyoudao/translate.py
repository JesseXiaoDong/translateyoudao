import requests
import hashlib
import json
from time import time
from copy import copy
from concurrent.futures import ThreadPoolExecutor, as_completed

from .settings import INDEX_URL, API_URL, HEADERS, BASIC_DATA, TIMEOUT


def request_api(word, proxies=None, word_from='AUTO', word_to='AUTO', retry_count=20):
    """
    模拟用户请求调用有道云翻译的web接口，取得翻译结果

    :param
        word_from: 当前语言
        word_to: 目标语言
        proxies: 代理设置
        retry_count: 请求重试次数，默认20次

    :语言代号
        中文: 'zh-CHS', 英语: 'en', 日语: 'ja', 韩语: 'ko', 法语: 'fr', 俄语: 'ru',
        西班牙语: 'es', 葡萄牙语: 'pt', 越南语: 'vi'

    :支持的语言方向
        自动检测语言
        中文->英语, 英语->中文, 中文->日语, 日语->中文, 中文->韩语, 韩语->中文
        中文->法语, 法语->中文, 中文->俄语, 俄语->中文, 中文->西班牙语
        西班牙语->中文, 中文->葡萄牙语, 葡萄牙语->中文, 中文->越南语, 越南语->中文

    :return 成功返回翻译后的字符串，失败返回False
    """
    # 单词不超过5000字符
    word = str(word)[:int(5e3)]
    data = copy(BASIC_DATA)
    data['i'] = word
    data['from'] = word_from
    data['to'] = word_to
    data['salt'] = str(round(time() * 1000))
    sign = data['client'] + word + data['salt'] + 'ebSeFb%=XZ%T[KZ)c(sy!'
    m2 = hashlib.md5()
    m2.update(sign.encode())
    data['sign'] = m2.hexdigest()

    with requests.Session() as s:
        n = 0
        # 网络相关错误重试
        while n < retry_count:
            try:
                s.get(INDEX_URL, timeout=TIMEOUT, headers=HEADERS, proxies=proxies)
                res = s.post(API_URL, timeout=TIMEOUT, data=data, headers=HEADERS, proxies=proxies)
                res = json.loads(res.text)
                if res['errorCode'] != 0:
                    raise ValueError
            # 网络相关错误和接口返回错误的结果
            except (
                requests.exceptions.Timeout, requests.exceptions.ConnectionError,
                requests.exceptions.ChunkedEncodingError, ValueError, json.decoder.JSONDecodeError
            ):
                n += 1
            else:
                return res['translateResult'][0][0]['tgt']
        else:
            return False


def translate(
    *words, proxies=None, word_from='AUTO', word_to='AUTO', retry_count=20, max_workers=10
):
    """
    翻译，支持多个词，默认自动检测语言，也可以自己设置

    :param
        word_from: 当前语言
        word_to: 目标语言
        proxies: 代理设置
        retry_count: 请求重试次数，默认20次
        max_workers: 最大线程数量，默认10个

    :语言代号
        中文: 'zh-CHS', 英语: 'en', 日语: 'ja', 韩语: 'ko', 法语: 'fr', 俄语: 'ru',
        西班牙语: 'es', 葡萄牙语: 'pt', 越南语: 'vi'

    :支持的语言方向
        自动检测语言
        中文->英语, 英语->中文, 中文->日语, 日语->中文, 中文->韩语, 韩语->中文
        中文->法语, 法语->中文, 中文->俄语, 俄语->中文, 中文->西班牙语
        西班牙语->中文, 中文->葡萄牙语, 葡萄牙语->中文, 中文->越南语, 越南语->中文

    :reutrn 返回一个包含单词和翻译后的字符串的字典，失败的单词键对应的值为False
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        word_to_translate = {
            executor.submit(request_api, word, proxies, word_from, word_to, retry_count): word
            for word in words
        }
        data = {}
        for future in as_completed(word_to_translate):
            word = word_to_translate[future]
            data[word] = future.result()

        return data
