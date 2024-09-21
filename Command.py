from abc import ABC, abstractmethod


class Command(ABC):
    def execute(self):
        pass


class PlayCommand(Command):
    def __init__(self, tamagotchi):
        self.tamagotchi = tamagotchi

    def execute(self):
        self.tamagotchi.play()

class EatCommand(Command):
    def __init__(self, tamagotchi):
        self.tamagotchi = tamagotchi

    def execute(self):
        self.tamagotchi.eat()

class SleepCommand(Command):
    def __init__(self, tamagotchi):
        self.tamagotchi = tamagotchi

    def execute(self):
        self.tamagotchi.sleep()

class ExerciseCommand(Command):
    def __init__(self, tamagotchi):
        self.tamagotchi = tamagotchi

    def execute(self):
        self.tamagotchi.exercise()

class FeedSnackCommand(Command):
    def __init__(self, tamagotchi):
        self.tamagotchi = tamagotchi

    def execute(self):
        self.tamagotchi.snack()
