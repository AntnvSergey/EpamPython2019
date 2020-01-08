"""
Написать свое property c кэшем и таймаутом
полностью повторяет поведение стандартной property за исключением:
    * хранит результат работы метода некоторое время, которое передается
      параметром в инициализацию проперти
    * пересчитывает значение, если таймер истек
"""

import time
import uuid


def timer_property(t):

    time_to_reset = t

    class CacheProperty(object):
        def __init__(self, fget=None, fset=None, fdel=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            self.current_time = 0
            self.cache = 0

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError("unreadable attribute")
            if self.current_time == 0 or time.time() - self.current_time > time_to_reset:
                self.cache = self.fget(obj)
                self.current_time = time.time()
            return self.cache

        def __set__(self, obj, value):
            if self.fset is None:
                raise AttributeError("Can't set attribute")
            self.current_time = time.time()
            self.cache = value

        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError("Can't delete attribute")
            self.fdel(obj)

        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel)

        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel)

        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel)

    return CacheProperty


class Message:

    @timer_property(t=10)
    def msg(self):
        self._msg = self.get_message()
        return self._msg

    @msg.setter # reset timer also
    def msg(self, param):
        self._msg = param

    def get_message(self):
        """
        Return random string
        """
        return uuid.uuid4().hex


if __name__ == '__main__':
    m = Message()
    initial = m.msg
    assert initial is m.msg
    time.sleep(2)
    assert initial is not m.msg
