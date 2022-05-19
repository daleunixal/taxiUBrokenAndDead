import random
from dataclasses import dataclass

from networkx.classes.reportviews import NodeView

from models.client_model import ClientModel
from singleton.singleton_provider import SingleMap

'''
Буду выделять свой код с двух сторон такими строчками:
# please work #
'''


class TaxiModel:
    is_busy: bool
    gps: NodeView
    is_spec_equip: bool
    currentClient: ClientModel or None
    currentTarget: NodeView or None
    totalProgress: int
    withClient: bool
    # currentOrderId: str
    # dist: float
    # time: int
    emptyDistance: float
    orderCount: float

    def __init__(self, gps, is_spec_equip, is_busy=False):
        self.is_busy = is_busy
        self.gps = gps
        self.is_spec_equip = is_spec_equip
        self.currentClient = None
        self.emptyDistance = 0
        self.orderCount = 0
        self.withClient = False
        self.totalProgress = 9999999

    # Should return VOID
    def on_complete_order(self):

        self.currentClient = None
        self.withClient = False


    # Should return VOID
    def on_epoch(self):
        if not self.currentClient:
            return

        self.totalProgress -= 5000

        if self.totalProgress < 5000:
            if self.withClient:
                self.on_complete_order()
            else:
                self.withClient = True
                self.currentTarget = self.currentClient.endPoint
                self.totalProgress = SingleMap.G.get_path_time_min(self.gps, self.currentTarget) * 60 * 1000
        # print(f"Suka, ja taxi. I have spec => {self.is_spec_equip}")
        pass

    # Should return VOID
    def on_order_begin(self, client):
            self.currentClient = client
            self.currentTarget = client.startPoint

            self.emptyDistance += SingleMap.G.get_path_dist_m(self.gps, self.currentTarget)
            self.orderCount += 1

            self.totalProgress = SingleMap.G.get_path_time_min(self.gps, self.currentTarget) * 60 * 1000

    # Should return Number
    def get_current_distance(self):
        print(self.gps)

        return 0
