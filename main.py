import random

class Cat:
    def __init__(self, color, name, eyes, gender, bored, cathunger):
        self.color = color
        self.name = name
        self.eyes = eyes
        self.gender = gender
        self.bored = bored
        self.cathunger = cathunger
    def activities(self):
        if self.bored:
            print(f"Day {day}: -Meow!")
            self.bored = False
    def hunger(self):
        if self.cathunger:
            print(f"Day {day}: -MEOW!")
            self.cathunger = False
    def catinfo(self):
        print(f"Cat's color: {self.color}. \nCat's name: {self.name}. \nCat's eyes color: {self.eyes}. \nCat's gender: {self.gender}")
day = 1
while day <= 7:
    color = "ginger"
    name = "Boris"
    eyes = "green"
    gender = "male"
    bored = random.choice([True, False])
    cathunger = random.choice([True, False])
    Boris = Cat(color, name, eyes, gender, bored, cathunger)
    Boris.activities()
    Boris.hunger()
    
    day += 1

Boris.catinfo()
