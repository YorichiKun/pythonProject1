class Transport:
    def __init__(self,motor,power,type,skill):
        self.motor = motor
        self.power = power
        self.type = type
        self.skill = skill

class Tank(Transport):
    def __init__(self,motor,power,type,skill):
        super().__init__(motor,power,type,skill)
    def attack(self):
        print("Танк к бою готов!!!")
    def retreat(self):
        print("Развернулся!")
    def honor(self):
        print("*Отдал честь*")
class Track(Transport):
    def __init__(self,motor,power,type,skill):
        super().__init__(motor,power,type,skill)
    def attack(self):
        print("Экипаж трака доставлен!!")
    def retreat(self):
        print("Экипаж трака экстренно эвакуирован!")
    def honor(self):
        print("*Отдали честь!!!*")


class Submarine(Transport):
    def __init__(self,motor,power,type,skill):
        super().__init__(motor,power,type,skill)
    def attack(self):
        print("Торпеда субмарины заряжена!!")
    def retreat(self):
        print("Вражеский корабаль нас засек , сварачиваем от курса на 12.34 градуса!")
    def honor(self):
        print("*Вынурныли из воды отдавая честь!!!*")


a = Tank(10,4000,"tank","shooting")
b = Track(1.5,110,"track","no")
c = Submarine(4,400,"submarine","launching torpedoes")


for i in (a,b,c):
    i.attack()
    i.retreat()
    i.honor()
    print("\n-------------------------------------------------------------\n")