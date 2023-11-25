class Tomato:
    _states = {0: 'absent', 1: 'colored', 2: 'green', 3: 'red'}
    # Объявление статического атрибута, который содержит все состояния цветения помидоров
    def __init__(self, index):
        self._index = index
        self._states = self._states[0]
        # Объявление динамических атрибутов
        # в _states находится первый элемент статического словаря
        """
        Эти два свойства являются защищёнными атрибутами
        """
    def grow(self):
        key_value_now = list(Tomato._states.values()).index(self._states) + 1
        # Определение индекса следующего состояния цветения томата.
        if key_value_now>3:
            key_value_now = 0
        # Границы кюча от 0 до 3. Чтобы не выходил за рамки статического словаря
        self._states = Tomato._states[key_value_now]
        # Новое состояние помидора!
        print(self._states)
    def is_ripe(self):
        # Если состояние помидора = 'red', то помидор считается зрелым
        if self._states==Tomato._states[3]:
            print(f"Помидор {self._index} созрел!")
        else:
            print(f"Помидор {self._index} ещё не созрел.")

class TomatoBush:
    def __init__(self, amount):
        self.amount = amount
        self.tomatoes = [Tomato(i) for i in range(amount)] #Создание списка из экземпляоров класса Tomato

    def grow_all(self):
        for i in self.tomatoes:
            i.grow() # Используя метод класса Tomato, мы обновляем статус зрелости каждого помидора на +1

    def all_are_ripe(self):
        count = 0
        for i in self.tomatoes:
            if i._states == Tomato._states[3]:
                count = count+1 # Считаем количество зрелых помидоров
            else:
                break
        return count == self.amount # Если счётчик равен количеству помидоров в кусте, то возвращаем True

    def give_away_all(self):
        self.tomatoes = [Tomato(i) for i in range(self.amount)] # Чистим список

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
        """
        name - публичный атрибут, _plant - защищённый
        """

    def work(self):
        self._plant.grow_all() # С помощью метода класса TomatoBush добавляем всем зрелость
    def harvest(self):
        if self._plant.all_are_ripe():
            print("Время собирать урожай!")
        else:
            print("Ещё рано собирать урожай.")
    @staticmethod
    def knowladge_base():
        print("Справка по садоводству!")


Gardener.knowladge_base()
tomatoBush1 = TomatoBush(5)
gardener = Gardener("Alex", tomatoBush1)
print("")
gardener.work()
print("")
gardener.harvest()
print("")
gardener.work()
print("")
gardener.work()
print("")
gardener.harvest()