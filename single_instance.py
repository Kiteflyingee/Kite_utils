# coding=utf-8

# 使用装饰器实现单例模式


def singleton(cls, *args, **kwargs):
    """
    单例模版,作为类的装饰器
    """
    instance = {}

    def _instance():
        if cls not in instance:
            instance[cls] = cls(*args, *kwargs)
        return instance[cls]
    return _instance


@singleton
class Test_singleton:
    def __init__(self):
        self.num = 0

    def add(self):
        self.num = 99


ts1 = Test_singleton()
ts2 = Test_singleton()
# 等价于 a1 = singleton(Test_singleton)
# 只调用了一次singleton方法，创建了一个绑定变量instance，对于他的闭包来说都是可访问的
# ts2 = a1()
# ts1 = a1()
print(id(ts1))
print(id(ts2))
