""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:
    def __init__(self, *exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.exception)


with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")

