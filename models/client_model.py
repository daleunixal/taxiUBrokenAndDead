import random
from dataclasses import dataclass


@dataclass
class ClientModel:
    priority: float
    is_panic_order: bool
    is_have_spec: bool

    def __init__(self):
        self.priority = random.randint(0, 100)

        chance_panic = 0.05
        if random.random() < chance_panic:
            self.is_panic_order = True
        else:
            self.is_panic_order = False

        chance_spec = 0.05
        if random.random() < chance_spec:
            self.is_have_spec = True
        else:
            self.is_have_spec = False
