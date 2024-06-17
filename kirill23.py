class House():
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

House = House()

House.setNewNumberOfFloors(25)

print(House.numberOfFloors)

House.setNewNumberOfFloors(123)
House.setNewNumberOfFloors(12333)
House.setNewNumberOfFloors(1233333)

print(House.numberOfFloors)