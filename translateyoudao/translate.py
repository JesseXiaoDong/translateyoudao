import requests
import hashlib
import json
from time import time
from copy import copy
from concurrent.futures import ThreadPoolExecutor, as_completed

from .settings import INDEX_URL, API_URL, HEADERS, BASIC_DATA, TIMEOUT


def request_api(word, proxies=None, word_from="AUTO", word_to="AUTO"):
    """
    模拟用户请求调用有道云翻译的web接口，取得翻译结果

    :param
        word_from: 当前语言
        word_to: 目标语言
        proxies: 代理设置

    :语言代号
        中文: 'zh-CHS', 英语: 'en', 日语: 'ja', 韩语: 'ko', 法语: 'fr', 俄语: 'ru',
        西班牙语: 'es', 葡萄牙语: 'pt', 越南语: 'vi'

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
        # 网络相关错误重试5次
        while n < 5:
            try:
                s.get(INDEX_URL, timeout=TIMEOUT, headers=HEADERS, proxies=proxies)
                res = s.post(API_URL, timeout=TIMEOUT, data=data, headers=HEADERS, proxies=proxies)
                res = json.loads(res.text)
                if res['errorCode'] != 0:
                    raise ValueError
            # 接口返回错误的结果
            except (ValueError, json.decoder.JSONDecodeError):
                return False
            # 网络相关错误
            except (
                requests.exceptions.Timeout, requests.exceptions.ConnectionError,
                requests.exceptions.ChunkedEncodingError
            ):
                n += 1
            else:
                return res['translateResult'][0][0]['tgt']
        else:
            return False


def translate(*words, proxies=None, word_from="AUTO", word_to="AUTO"):
    """
    翻译，支持多个词，默认自动检测语言，也可以自己设置

    :param
        word_from: 当前语言
        word_to: 目标语言
        proxies: 代理设置

    :语言代号
        中文: 'zh-CHS', 英语: 'en', 日语: 'ja', 韩语: 'ko', 法语: 'fr', 俄语: 'ru',
        西班牙语: 'es', 葡萄牙语: 'pt', 越南语: 'vi'

    :reutrn 返回一个包含单词和翻译后的字符串的字典，失败的单词键对应的值为False
    """
    with ThreadPoolExecutor() as executor:
        word_to_translate = {
            executor.submit(request_api, word, proxies, word_from, word_to): word
            for word in words
        }
        data = {}
        for future in as_completed(word_to_translate):
            word = word_to_translate[future]
            data[word] = future.result()

        return data
