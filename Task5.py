class Phone:
    def __init__(self, name, probeg, price):
        self.name = name
        self.probeg = probeg
        self.price = price
    def probegAndPriceAfter5Years(self):
        pass
class OldPhone(Phone):
    def __init__(self, name, probeg, price):
        super().__init__(name, probeg, price)
    def probegAndPriceAfter5Years(self):
        print(f"Телефону {self.name} станет {self.probeg + 5} лет, а про его стоимость вообще молчу.")

class NewPhone(Phone):
    def __init__(self, name, probeg, price):
        super().__init__(name, probeg, price)
    def probegAndPriceAfter5Years(self):
        print(f"Телефону {self.name} станет {self.probeg + 5} лет, а стоимость примерно {self.price - 5000}")

myPhone = NewPhone("Redmi Note 7", 4, 12000)
myOldPhone = OldPhone("Старый Кнопочный", 10, "немного")

myPhone.probegAndPriceAfter5Years()
myOldPhone.probegAndPriceAfter5Years()
