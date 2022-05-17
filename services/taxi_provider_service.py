import random

from collectors.era_data_collector import EraDataCollector
from models.taxi_model import TaxiModel

####################################################

# Я у тебя тут попишу, но свой код закоментирую :з #

####################################################

'''
Буду выделять свой код с двух сторон такими строчками:
# please work #
'''


class TaxiProviderService:
    # please work #
    dist: float
    time: int

    @property
    def get_dist(self):
        return self.dist

    @get_dist.setter
    def get_dist(self, dist):
        self.dist = dist

    @property
    def get_time(self):
        return self.time

    @get_time.setter
    def get_time(self, time):
        self.time = time
    # please work #

    @staticmethod
    def begin_model_recreate():
        taxi_container = list()

        for i in range(random.randint(680, 720)):
            taxi_container.append(TaxiModel())

        print(list)

        return taxi_container

    @staticmethod
    def on_epoch():
        chance = 0.07

        total_new_instance = 0

        while random.random() < chance:
            total_new_instance += 1
            EraDataCollector.taxi_bank.append(TaxiModel())

        if total_new_instance > 0:
            print('New instances of Taxi = ', total_new_instance)
