import random
from collectors.era_data_collector import EraDataCollector
from models.client_model import ClientModel
from singleton.singleton_provider import SingleMap

graph_map = SingleMap.getGraph()


class ClientProviderService:
    @staticmethod
    def begin_model_recreate():
        client_container = list()

        for i in range(random.randint(30, 40)):
            client_container.append(ClientProviderService.create_client())

        print(list)

        return client_container

    @staticmethod
    def on_epoch():
        chance = 0.11

        total_new_instance = 0

        while random.random() < chance:
            total_new_instance += 1
            EraDataCollector.client_bank.append(ClientProviderService.create_client())

        if total_new_instance > 0:
            print('New instances of Client = ', total_new_instance)


    @staticmethod
    def create_client():

        chance_panic = 0.05
        if random.random() < chance_panic:
            is_panic_order = True
        else:
            is_panic_order = False
        chance_spec = 0.05
        if random.random() < chance_spec:
            is_have_spec = True
        else:
            is_have_spec = False



        is_sucess = False

        while not is_sucess:
            start_point = graph_map.get_random_node()
            end_point = graph_map.get_random_node()

            try:
                path = graph_map.get_path_dist_m(start_point, end_point)
            except:
                continue

            is_sucess = True




        client = ClientModel(is_have_spec=is_have_spec, startPoint=start_point,
                             endPoint=end_point)
        try:
            taxi = graph_map.closer_taxi_to_client(EraDataCollector.taxi_bank, client.startPoint)
            taxi.on_order_begin(client)
        except:
            EraDataCollector.decline_count += 1
            client = None

        return client
