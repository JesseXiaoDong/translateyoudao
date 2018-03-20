"""
使用代理设置
"""
import re

from translateyoudao.translate import translate
from translateyoudao.proxy import get_proxies, get_proxy_ip

p = re.compile(r'[a-zA-Z]+')
text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
words = re.findall(p, text)

# 代理订单号
order_no = '28f69ed72e7024d8fe1988d4bf6f8e54'
# 获得代理对象
proxies = get_proxies(get_proxy_ip, args=(order_no, ))
# 建议一次不要传入太多单词
print(translate(*words, proxies=proxies))
