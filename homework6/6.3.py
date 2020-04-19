#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
# 定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})
class dictclass():
    def __init__(self, dict):
        self.dict=dict

    def del_dict(self,key):
        del self.dict[key]

    def get_dict(self,key):
        if key in self.dict:
            return self.dict[key]
        else:
            return 'not found'

    def get_key(self):
        dictlist = []
        for k in self.dict.keys():
            dictlist.append(k)
        return dictlist

    def update_dict(self,dict2):
        for i, k in dict2.items():
            self.dict[i] = k
        return [k for i, k in self.dict.items()]

d1 = dictclass({'ruanjian': 45,'jisuan': 56,'wulian': 40})
d2 = {'gaoshu': 72,'xiandai': 79,'wuli': 90}
d1.del_dict('wulian')
print(d1.get_dict('ruanjian'))
print(d1.get_dict('wulian'))
print(d1.get_key())
print(d1.update_dict(d2))
