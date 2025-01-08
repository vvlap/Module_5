class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует в', self.name, '\n')
        else:
            for i in list(range(1, new_floor+1)):
                print(i)


house1 = House('ЖК Берег', 25)
house2 = House('ЖК Дачный', 12)
house1.go_to(26)
house2.go_to(6)
