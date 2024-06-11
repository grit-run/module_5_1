class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.apart_info()

    def go_to(self, new_floor):
        if new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i, "Едем этажом выше")
        else:
            print("Такого этажа не существует")

    def apart_info(self):
        print(self.name, self.number_of_floors)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.apart_info()
h1.go_to(5)
h2.apart_info()
h2.go_to(10)
