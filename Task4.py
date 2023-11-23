class Phone:
    def __init__(self, name, brand, probeg, price):
        self._name = name
        self.brand = brand
        self.probeg = probeg
        self.__price = price

    def whatIsPhone(self):
        print(f"Это же {self._name} от компании {self.brand}!!! С ума сойти!!!")

    def additionalInfo(self):
        print(f"А пробег то у него {self.probeg}... Ну на {self.__price} денег, думаю, потянет. Ладно, свои задачи делает и хорошо.")


class OldPhone(Phone):
    def __init__(self, name, brand, probeg, price, buttons):
        super().__init__(name, brand, probeg, price)
        self._buttons = buttons
    def whatButtons(self):
        print(self._buttons)

myPhone = Phone("Redmi Note 7", "Xiaomi", "4 года", "много")
myPhone.whatIsPhone()
myPhone.additionalInfo()

myOldPhone = OldPhone("Старый Кнопочный", "NOKIA", "10 лет", "немного", "Много больших кнопок.")
myOldPhone.whatIsPhone()
myOldPhone.whatButtons()

print(myPhone._name)
print(myOldPhone._buttons)