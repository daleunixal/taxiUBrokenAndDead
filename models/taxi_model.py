import random
from dataclasses import dataclass

from networkx.classes.reportviews import NodeView


@dataclass
class TaxiModel:
    is_busy: bool
    gps: NodeView
    is_spec_equip: bool
    currentOrderId: str

    def __init__(self, is_busy=False):
        if is_busy:
            self.is_busy = True
        else:
            self.is_busy = False

        chance = 0.1
        generated_value = random.random()

        if generated_value < chance:
            self.is_spec_equip = True
        else:
            self.is_spec_equip = False

    # Should return VOID
    def on_complete_order(self):
        raise Exception('Method not implemented')

    # Should return VOID
    def on_epoch(self):
        # print(f"Suka, ja taxi. I have spec => {self.is_spec_equip}")
        pass

    # Should return VOID
    def on_order_begin(self):
        raise Exception('Method not implemented')

    # Should return Number
    def get_current_distance(self):
        print(self.gps)

        return 0
