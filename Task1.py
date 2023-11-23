class Phone:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def WhatIsPhone(self):
        print(f"Это же {self.name} от компании {self.brand}!!! С ума сойти!!!")

myPhone = Phone("Redmi Note 7", "Xiaomi")
myPhone.WhatIsPhone()

