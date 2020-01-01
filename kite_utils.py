# coding=utf-8

"""
kite python utils set
"""


def singleton(cls, *args, **kwargs):
    """
    Singleton decorator template, Add @singleton annotation above your class
    """
    instance = {}

    def _instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, *kwargs)
        return instance[cls]
    return _instance
