from Pet import Pet
import datetime


class FactoryOverview:
    def __init__(self):
        self.class_time_daily = datetime.datetime(year=2024, month=9, day=27)
        self.class_time_hourly = datetime.datetime(year=2024, month= 9, day= 27, hour=18, minute=0, second=0)
        self.game = True

    def create_new_tamogotchi(self, tamgotchi_name: str):
        # creation of new tamgotchi
        return Pet(name=tamgotchi_name)


    def changeSettings(self, tamogotchi):
        # automatic change in settings of tamgotchi
        delta_daily = datetime.timedelta(days=1)
        delta_hourly = datetime.timedelta(hours=1)
        while True:
            if datetime.datetime.now() >= self.class_time_daily:
                tamogotchi.MAX_LIMIT_MEAL = 3
                tamogotchi.SNACK_COUNT = 0
                tamogotchi.EX_COUNT = 0
                self.class_time_daily += delta_daily

            elif datetime.datetime.now() >= self.class_time_hourly:
                tamogotchi.happiness -= 5
                tamogotchi.sickness += 1
                tamogotchi.hunger += 5
                tamogotchi.training -= 5
                self.class_time_hourly += delta_hourly

            if not self.game:
                break



