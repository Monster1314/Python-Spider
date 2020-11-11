"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458
"""

import re

tel = "18123115458"

def func(temp):
    print(temp)
    str_ = temp.group(0)
    print(str_)
    return str_[:3] + '****' + str_[-4:]

# func 是sub方法会默认调用的函数, return返回的结果就是最终替换的结果
result = re.sub('\d{11}', func, tel, re.S)
print(result)
