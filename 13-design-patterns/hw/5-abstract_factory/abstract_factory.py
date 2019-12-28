"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""
import yaml


class AbstractFactory:
    def __init__(self, menu):
        self.menu = menu

    def create_first_courses(self, day):
        pass

    def create_second_courses(self, day):
        pass

    def create_drinks(self, day):
        pass


class Vegan(AbstractFactory):
    def create_first_courses(self, day):
        return self.menu[day]['first_courses']['vegan']

    def create_second_courses(self, day):
        return self.menu[day]['second_courses']['vegan']

    def create_drinks(self, day):
        return self.menu[day]['drinks']['vegan']


class Child(AbstractFactory):
    def create_first_courses(self, day):
        return self.menu[day]['first_courses']['child']

    def create_second_courses(self, day):
        return self.menu[day]['second_courses']['child']

    def create_drinks(self, day):
        return self.menu[day]['drinks']['child']


class China(AbstractFactory):
    def create_first_courses(self, day):
        return self.menu[day]['first_courses']['china']

    def create_second_courses(self, day):
        return self.menu[day]['second_courses']['china']

    def create_drinks(self, day):
        return self.menu[day]['drinks']['china']


file = open('menu.yml', 'r', encoding="utf8")
menu = yaml.load(file, Loader=yaml.FullLoader)
vegan = Vegan(menu)
print(vegan.create_drinks('Saturday'))