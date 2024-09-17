from enum import Enum
public Enum states{
    Baby,
    Child, 
    Teenager,
    Adult,
    Senior,
    Special
}
class Pet():
    def __init__(self, counter, state, hunger, happiness, training, sickness, states.state):
        self.counter = counter
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

