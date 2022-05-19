import random

from collectors.era_data_collector import EraDataCollector
from models.taxi_model import TaxiModel
# please work #
from broken_map import GraphMap
# please work #

####################################################

# Я у тебя тут попишу, но свой код закоментирую :з #

####################################################
from singleton.singleton_provider import SingleMap

'''
Буду выделять свой код с двух сторон такими строчками:
# please work #
'''


class TaxiProviderService:

    @staticmethod
    def begin_model_recreate():
        # please work #
        # is_busy = False
        # is_spec_equip = False

        # graph_map = SingleMap.getGraph()
        # strategy = graph_map.get_strategy()
        # please work #
        taxi_container = list()

        for i in range(random.randint(680, 720)):
            taxi_container.append(TaxiProviderService.createTaxi())

        taxi_container = sorted(taxi_container, key=lambda taxi_model: taxi_model.gps)
        print(taxi_container)

        return taxi_container

    @staticmethod
    def on_epoch():
        chance = 0.07

        total_new_instance = 0

        while random.random() < chance:
            total_new_instance += 1
            EraDataCollector.taxi_bank.append(TaxiProviderService.createTaxi())

        if total_new_instance > 0:
            print('New instances of Taxi = ', total_new_instance)


    @staticmethod
    def createTaxi():

        graph_map = SingleMap.getGraph()

        chance = 0.1
        generated_value = random.random()

        if generated_value < chance:
            is_spec_equip = True
        else:
            is_spec_equip = False

        return TaxiModel(is_busy=False, is_spec_equip=is_spec_equip, gps=graph_map.get_random_node())
