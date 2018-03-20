INDEX_URL = 'http://fanyi.youdao.com/'

API_URL = INDEX_URL + 'translate_o?smartresult=dict&smartresult=rule'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0",
    "Origin": INDEX_URL,
    "Referer": INDEX_URL,
    "X-Requested-With": "XMLHttpRequest",
}

BASIC_DATA = {
    "smartresult": "dict",
    "client": "fanyideskweb",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "lan-select",
    "typoResult": "false",
}

TIMEOUT = 10

PROXY_API_URL = "http://api.ip.data5u.com/dynamic/get.html?order="
