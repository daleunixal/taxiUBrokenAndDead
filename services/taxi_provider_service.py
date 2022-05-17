import random

from collectors.era_data_collector import EraDataCollector
from models.taxi_model import TaxiModel

class TaxiProviderService:
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
