from dataclasses import dataclass


class EraDataCollector:
    taxi_bank = list()
    client_bank = list()


    @staticmethod
    def addTaxi(taxi):
        EraDataCollector.taxi_bank.append(taxi)

    @staticmethod
    def addTaxiList(taxi_list):
        EraDataCollector.taxi_bank += taxi_list

    @staticmethod
    def removeTaxi(taxi):
        EraDataCollector.taxi_bank.remove(taxi)

    @staticmethod
    def addClient(client):
        EraDataCollector.client_bank.append(client)

    @staticmethod
    def clear():
        EraDataCollector.taxi_bank = list()
        EraDataCollector.client_bank = list()
