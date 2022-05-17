import math


class EpochController:

    def __init__(self, *args):
        self.entity_collection = list(args)

    def begin_new_era(self, epoch_duration, era_duration):
        """
            Начать отсчет эпохи с конфигурацией инстанса

            :param epoch_duration - длительность одной эпохи в мс

            :param era_duration - длительность эры в мс

        """
        total_epoch_count = math.floor(era_duration/epoch_duration)

        for epoch in range(total_epoch_count):
            print(f"_____EPOCH {epoch}_____")
            for entity in self.entity_collection:
                if type(entity) is list:
                    for nested in entity:
                        nested.on_epoch()
                else:
                    entity.on_epoch()

        print()
