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
print(id(ts1))
print(id(ts2))
