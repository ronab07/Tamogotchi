from enum import Enum
class states(Enum):
    Baby,
    Child, 
    Teenager,
    Adult,
    Senior,
    Special
    
class Pet():
    def __init__(self, state, hunger, happiness, training, sickness, states.state):
        self.counter = 0
        self.state = state
        self.hunger = hunger
        self.happiness = happiness
        self.training = training
        self.sickness = sickness
        self.MAX_LIMIT_MEAL = 3
        self.state = state

    def eat(self):
        pass

    def play(self):
        pass

    def sleep(self):
        pass

    def exercise(self):
        pass

