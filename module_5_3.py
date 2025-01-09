class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return len(self) == len(other)
        elif isinstance(other, int):
            return len(self) == other
        else:
            return 'Other может быть класса House либо класса int'

    def __lt__(self, other):
        if isinstance(other, House):
            return len(self) < len(other)
        elif isinstance(other, int):
            return len(self) < other
        else:
            return 'Other может быть класса House либо класса int'

    def __le__(self, other):
        if isinstance(other, House):
            return len(self) <= len(other)
        elif isinstance(other, int):
            return len(self) <= other
        else:
            return 'Other может быть класса House либо класса int'

    def __gt__(self, other):
        if isinstance(other, House):
            return len(self) > len(other)
        elif isinstance(other, int):
            return len(self) > other
        else:
            return 'Other может быть класса House либо класса int'

    def __ge__(self, other):
        if isinstance(other, House):
            return len(self) >= len(other)
        elif isinstance(other, int):
            return len(self) >= other
        else:
            return 'Other может быть класса House либо класса int'

    def __ne__(self, other):
        if isinstance(other, House):
            return len(self) != len(other)
        elif isinstance(other, int):
            return len(self) != other
        else:
            return 'Other может быть класса House либо класса int'

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return 'Количество этажей может быть только класса int'

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            return 'Количество этажей может быть только класса int'

    def __sub__(self, value):
        if isinstance(value, int):
            self.number_of_floors -= value
            return self
        else:
            return 'Количество этажей может быть только класса int'

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует в', self.name, '\n')
        else:
            for i in list(range(1, new_floor+1)):
                print(i)


house1 = House('ЖК Берег', 25)
house2 = House('ЖК Дачный', 12)
print(house1)
print(house2)
print(house1 != 33)
print(house1 >= 50)
print(house1 < house2)
house2 += 10
print(house2)
house1 = house1 - 3
print(house1)
print(house1 == house2)
print(50 <= house1)