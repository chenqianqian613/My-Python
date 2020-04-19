#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#
# @Author  : cqq
#
class Foo(object):
    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))
    @classmethod
    def class_method(cls):
        print("是类方法")
    @staticmethod
    def static_method():
        print('是静态方法')
foo = Foo()
foo.instance_method()
foo.static_method()
foo.class_method()
print('----------------')
Foo.static_method()
Foo.class_method()