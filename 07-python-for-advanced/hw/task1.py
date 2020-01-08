"""
Реализовать такой метакласс, что экземпляры класса созданного с помощью него
будут удовлетворять следующим требованиям:
* объекты созданные с одинаковыми аттрибутами будут одним и тем же объектом
* объекты созданные с разными аттрибутами будут разными объектами
* у любого объекта есть мозможность получить доступ к другим объектам
    того же класса
>>> unit1 = SiamObj('1', '2', a=1)
>>> unit2 = SiamObj('1', '2', a=1)
>>> unit1 is unit2
True
>>> unit3 = SiamObj('2', '2', a=1)
>>> unit3.connect('1', '2', 1).a = 2
>>> unit2.a == 2
True
>>> pool = unit3.pool
>>> print(len(pool))
2
>>> del unit3
>>> print(len(pool))
1
"""

import weakref


class Meta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._instances = {}
        cls.pool = cls._instances

    def __call__(cls, *args, **kwargs):
        def connect(*args, **kwargs):
            arguments = args + tuple(kwargs.values())
            for key, value in cls._instances.items():
                if value == arguments:
                    return key()
            else:
                print(f"Instance with attributes {arguments} doesn't exist")

        def delete(instance):
            try:
                del cls._instances[weakref.ref(instance)]
            except KeyError:
                pass

        cls.__del__ = delete
        cls.connect = connect
        arguments = args + tuple(kwargs.values())
        instance = super().__call__(*args, **kwargs)
        for key, value in cls._instances.items():
            if value == arguments:
                return key()
        else:
            cls._instances[weakref.ref(instance)] = arguments
            return instance


class SiamObj(metaclass=Meta):
    def __init__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    unit0 = SiamObj()
    unit1 = SiamObj('1', '2', a=1, b=2, c=0)
    unit2 = SiamObj('1', '2', b=2, c=0, a=1)
    unit3 = SiamObj('2', '2', a=0, b=22)

    pool = unit3.pool
    print('pool len init', len(pool))
    del unit3
    print('pool len finish', len(pool))
