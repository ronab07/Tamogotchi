public enum{
    Baby,
    Child, 
    Teenager,
    Adult,
    Senior,
    Special
}
class Pet():
    def __init__(self, counter, state, hunger, happiness, training, sickness, MAX_LIMIT_MEAL):
        self.counter = counter
        self.state = state
        self.hunger = hunger
        self.happiness = happiness
        self.training = training
        self.sickness = sickness
        self.MAX_LIMIT_MEAL = MAX_LIMIT_MEAL

    def eat(self):
        pass

    def play(self):
        pass

    def sleep(self):
        pass

    def exercise(self):
        pass

