
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def menya_zvati(self):
        print(f"моего пса зовут {self.name}",
              f"ему {self.age} лет")
    def guf(self):
        print("aуф ауф ауф")
class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def menya_zvati(self):
        print(f"моего кота зовут {self.name}",
              f"ему {self.age} лет")

    def guf(self):
        print("мяуф мяуф мяуф")
a = Cat("мяуф","5")
b = Dog("ауф","5")
for i in (a,b):
    i.guf()
    i.menya_zvati()