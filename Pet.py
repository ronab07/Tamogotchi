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
    def __init__(self, name: str):
        self.counter = 0
        self.state = "Baby"
        self.hunger = 30
        self.happiness = 100
        self.training = 20
        self.sickness = 0
        self.MAX_LIMIT_MEAL = 3
        self.weight = 5
        self.age = 0
        self.name = name
        self.SNACK_COUNT = 0
        self.EX_COUNT = 0

    def eat(self):
        if MAX_LIMIT_MEAL != 0:
            self.hunger += 10
            MAX_LIMIT_MEAL -=1
            counter +=1
        self.update_state()

    def play(self):
        self.happiness += 15
        counter +=1
        self.update_state()


    def sleep(self):
        self.happiness += 5
        self.sickness -= 7
        counter +=1
        self.update_state()


    def exercise(self):
        EX_COUNT +=1
        counter +=1
        if EX_COUNT>3:
            self.sickness +=15
        self.update_state()


    def snack(self):
        SNACK_COUNT += 1
        self.happiness += 8
        self.hunger += 5
        counter +=1
        if SNACK_COUNT>3:
            self.sickness += 7
        self.update_state()


    def check_age_and_weight(self):
        return "This tamagotchi's {self.name}\nweight is: {self.weight} \nage is: {self.age}"

    def update_state(self):
        # פונקציה שקוראים לה מתוך הפעולות של המשחק, אכילה וכו, משנה את המצב לפי המדדים השונים
        return
