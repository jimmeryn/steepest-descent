import numpy as np


class MNS:
    def __init__(self):
        self.alpha = 1  # mnożnik antygradientu
        self.start = np.array([0, 0])  # punkt startowy algorytmu
        self.epsilon = 1e-3  # błąd potrzebny do kryteriów stopu mniejszy lub równy 10^(-3)

    def test(self):
        print(self.alpha)
        print(self.start)
        print(self.epsilon)
