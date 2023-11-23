class Phone:
    def __init__(self, name, brand, probeg, price):
        self.name = name
        self.brand = brand
        self.probeg = probeg
        self.price = price

    def WhatIsPhone(self):
        print(f"Это же {self.name} от компании {self.brand}!!! С ума сойти!!!")

    def AdditionalInfo(self):
        print(f"А пробег то у него {self.probeg}... Ну на {self.price} денег, думаю, потянет. Ладно, свои задачи делает и хорошо.")

myPhone = Phone("Redmi Note 7", "Xiaomi", "4 года", "много")
myPhone.WhatIsPhone()
myPhone.AdditionalInfo()