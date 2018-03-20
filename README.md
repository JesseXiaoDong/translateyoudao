# translateyoudao
基于有道云web翻译接口的翻译工具，翻译结果基于 **[有道云翻译web版](http://fanyi.youdao.com/)** ，无需有道云账号，设置动态代理后理论上可无限调用，适合翻译大量词汇。
内置多线程和动态代理的实现方案，以及基于 **[无忧代理IP（付费的）](https://www.python.org/downloads/)** 的代理IP获取方法。

有道云翻译有开放的翻译接口，不过免费账号有字符限制（土豪当我没说~），所以我就实现了一个基于有道云翻译web版的翻译工具。

### 如果是高频次大量的翻译一定要设置IP代理，不然会被有道云那边封掉IP

## 安装
### 需要手动安装的依赖

* **[Python 3.6+](https://www.python.org/downloads/)**

### 使用pip安装

    $ pip3 install translateyoudao

upgrade:

    $ pip3 install -U translateyoudao


## 开始使用

简单使用:

demo.py
```console
from translateyoudao.translate import translate

# 支持多个词一起翻译
print(translate('hello', '再见'))
```

设置代理(无忧代理IP):

demo.py
```console
from translateyoudao.translate import translate
from translateyoudao.proxy import get_proxies, get_proxy_ip

# 代理订单号
order_no = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# 获得代理对象
proxies = get_proxies(get_proxy_ip, args=(order_no, ))
# 建议一次不要传入太多词
print(translate('hello', '再见', 'world', proxies=proxies))
```

自定义设置当前语言和目标语言:

demo.py
```console
from translateyoudao.translate import translate

# 中文到日语
print(translate('你好', '再见', word_from='zh-CHS', word_to='ja'))
```

## 语言代号
* 中文: 'zh-CHS'
* 英语: 'en'
* 日语: 'ja'
* 韩语: 'ko'
* 法语: 'fr'
* 俄语: 'ru'
* 西班牙语: 'es'
* 葡萄牙语: 'pt'
* 越南语: 'vi'

## 支持的语言翻译方向
* 中文->英语
* 英语->中文
* 中文->日语
* 日语->中文
* 中文->韩语
* 韩语->中文
* 中文->法语
* 法语->中文
* 中文->俄语
* 俄语->中文
* 中文->西班牙语
* 西班牙语->中文
* 中文->葡萄牙语
* 葡萄牙语->中文
* 中文->越南语
* 越南语->中文

## Note
* 如果想用其他代理方案，只需重写translateyoudao.translate模块下的get_proxy_ip函数
* 如果是高频次大量的翻译一定要设置IP代理，不然会被有道云那边封掉IP
