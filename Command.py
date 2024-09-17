from abc import ABC, abstractmethod


class Command (ABC):
    def execute(self):
        pass


class PlayCommand(Command):
    def __init__(self, tamagotchi):
        self.tamagotchi = tamagotchi
