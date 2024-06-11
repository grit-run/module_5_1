class House:
    def __init__(self, name):
        self.numberOfFloors = 0

    def newNumberOfFloors(self, floors):
        #        floors = int(input("Сколько будет этажей в здании : "))
        self.numberOfFloors = floors
        print("Меняем количество этажеЙ нв {}".format(self.numberOfFloors))


n = House("NN")
print("Сейчас в здании {} этажей".format(n.numberOfFloors))
n.newNumberOfFloors(10)
