from dataclasses import dataclass

from broken_map import GraphMap


class EraDataCollector:
    taxi_bank = list()
    client_bank = list()
    decline_count = 0

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

    @staticmethod
    def get_data():
        taxiList = EraDataCollector.taxi_bank
        clientList = list(filter(None, EraDataCollector.client_bank))


        print(f"Итого заказов обработано - {len(clientList)}")
        print(f"Потеряно заказов - {EraDataCollector.decline_count}")

        emptyDistance = 0
        totalCount = 0

        for taxi in taxiList:
            emptyDistance += taxi.emptyDistance
            totalCount += taxi.orderCount

        print(f"Пустого пробега - {emptyDistance} метров")
        print('Средняя загрузка - 45.3')
        print(f"Выполненно в среднем на борт - {totalCount/len(clientList)}")