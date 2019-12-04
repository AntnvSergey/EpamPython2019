"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):

    def get_created_instances(*args, **kwargs):
        print(cls.number_of_copies)
        return cls.number_of_copies

    def reset_instances_counter(*args, **kwargs):
        count = cls.number_of_copies
        cls.number_of_copies = 0
        print(count)
        return count

    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    return cls


@instances_counter
class User:
    number_of_copies = 0

    def __init__(self, *args, **kwargs):
        User.number_of_copies += 1


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
