"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""
class BaseHandler:
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        self.next = handler
        return self.next


class Fridge:
    def __init__(self, eggs=0, flour=0, milk=0.0,
                sugar=0, sunflower_oil=0, butter=0):
        self.eggs = eggs
        self.flour = flour
        self.milk = milk
        self.sugar = sugar
        self.sunflower_oil = sunflower_oil
        self.butter = butter


class EggsHandler(BaseHandler):
    def handle(self, fridge: Fridge):
        if fridge.eggs < 2:
            print(f'Need {2-fridge.eggs} eggs')
        if self.next:
            self.next.handle(fridge)


class FlourHandler(BaseHandler):
    def handle(self, fridge: Fridge):
        if fridge.flour < 300:
            print(f'Need {300-fridge.flour} gram of flour')
        if self.next:
            self.next.handle(fridge)


class MilkHandler(BaseHandler):
    def handle(self, fridge: Fridge):
        if fridge.milk < 0.5:
            print(f'Need {0.5-fridge.milk} liter of milk')
        if self.next:
            self.next.handle(fridge)


class SugarHandler(BaseHandler):
    def handle(self, fridge: Fridge):
        if fridge.sugar < 100:
            print(f'Need {100-fridge.sugar} gram of sugar')
        if self.next:
            self.next.handle(fridge)


class SunflowerOilHandler(BaseHandler):
    def handle(self, fridge: Fridge):
        if fridge.sunflower_oil < 10:
            print(f'Need {10-fridge.sunflower_oil} milliliter of '
                  f'sunflower oil')
        if self.next:
            self.next.handle(fridge)


class ButterHandler(BaseHandler):
    def handle(self, fridge: Fridge):
        if fridge.butter < 120:
            print(f'Need {120-fridge.butter} gram of butter')
        if self.next:
            self.next(fridge)


fridge = Fridge()
another_fridge = Fridge(eggs=3, butter=200, milk=0.3)
eggs_handler = EggsHandler()
flour_handler = FlourHandler()
milk_handler = MilkHandler()
sugar_handler = SugarHandler()
sunflower_handler = SunflowerOilHandler()
butter_handler = ButterHandler()
eggs_handler.set_next(flour_handler).set_next(milk_handler)
milk_handler.set_next(sugar_handler).set_next(sunflower_handler)
sunflower_handler.set_next(butter_handler)
eggs_handler.handle(fridge)
print(30*'-')
eggs_handler.handle(another_fridge)