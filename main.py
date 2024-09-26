from distutils.command.config import config

from Command import EatCommand, PlayCommand, SleepCommand, ExerciseCommand, FeedSnackCommand
from CommandRemote import CommandRemote
from OverviewFactory import FactoryOverview

def main():
    factory = FactoryOverview()

    # Opening game
    print("Hello! welcome to our awsome Tamagotchi game")
    tamg_name = input("Enter a name for you tamagotchi")

    # Create a pet using the Factory
    my_pet = factory.create_new_tamogotchi()  # needs to add parameters

    # Create commands for the pet
    eat_command = EatCommand(my_pet)
    play_command = PlayCommand(my_pet)
    sleep_command = SleepCommand(my_pet)
    exercise_command = ExerciseCommand(my_pet)
    snack_command = FeedSnackCommand(my_pet)

    remote = CommandRemote()

    # Playing:
    while True:
        command = input("Enter your command")
        if command.lower() == "play":
            remote.add_command(play_command)
        elif command.lower() == "snack":
            remote.add_command(snack_command)
        elif command.lower() == "sleep":
            remote.add_command(sleep_command)
        elif command.lower() == "eat":
            remote.add_command(eat_command)
        elif command.lower() == "exercise":
            remote.add_command(exercise_command)
        elif command.lower() == "exit":
            break
        else:
            print("Wrong input, try again")


if __name__ == "__main__":
    main()



