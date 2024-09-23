from enum import Enum
class States(Enum):
    Baby = 1
    Child = 2
    Teenager = 3
    Adult = 4
    Senior = 5
    Special = 6
    Dead = 7
    
class Pet:
    def __init__(self, state: States, hunger: int, happiness: int, training: int, sickness: int, weight: int, name: str):
        self.counter = 0
        self.state = state
        self.hunger = hunger
        self.happiness = happiness
        self.training = training
        self.sickness = sickness
        self.MAX_LIMIT_MEAL = 3
        self.weight = weight
        self.age = 0
        self.name = name

    def eat(self):
        pass
        # self.update_state()

    def play(self):
        self.happiness *= 1.5
        self.update_state()


    def sleep(self):
        self.happiness *= 1.1
        self.sickness *= 0.75
        self.update_state()


    def exercise(self):
        pass
        # self.update_state()


    def snack(self):
        self.happiness *= 1.5
        self.hunger *= 1.25
        self.update_state()


    def check_age_and_weight(self):
        return "This tamagotchi's {self.name}\nweight is: {self.weight} \nage is: {self.age}"

    def update_state(self):
        # פונקציה שקוראים לה מתוך הפעולות של המשחק, אכילה וכו, משנה את המצב לפי המדדים השונים
        return
