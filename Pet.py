from enum import Enum
class States(Enum):
    Baby = 1
    Child = 2
    Teenager = 3
    Adult = 4
    Senior = 5
    Special = 6
    Dead = 7
    
class Pet():
    def __init__(self, state: States, hunger: int, happiness: int, training: int, sickness: int):
        self.counter = 0
        self.state = state
        self.hunger = hunger
        self.happiness = happiness
        self.training = training
        self.sickness = sickness
        self.MAX_LIMIT_MEAL = 3

    def eat(self):
        pass

    def play(self):
        pass

    def sleep(self):
        pass

    def exercise(self):
        pass

