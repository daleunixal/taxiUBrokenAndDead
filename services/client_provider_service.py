import random

from collectors.era_data_collector import EraDataCollector
from models.client_model import ClientModel

class ClientProviderService:
    @staticmethod
    def begin_model_recreate():
        client_container = list()

        for i in range(random.randint(30, 40)):
            client_container.append(ClientModel())

        print(list)

        return client_container

    @staticmethod
    def on_epoch():
        chance = 0.11

        total_new_instance = 0

        while random.random() < chance:
            total_new_instance += 1
            EraDataCollector.client_bank.append(ClientModel())

        if total_new_instance > 0:
            print('New instances of Client = ', total_new_instance)


