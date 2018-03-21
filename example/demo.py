"""
不使用代理设置
"""
from translateyoudao.translate import translate

# 支持多个词一起翻译，返回值为翻以前和翻译后的键值对字典，翻译失败的词对应的键值为False，大家请自行判断翻译成功与否
print(translate('hello', '再见'))
