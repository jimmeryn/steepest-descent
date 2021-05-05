import matplotlib.pyplot as plt
import numpy as np
from mns import MNS
from goldstein import goldstein

def main():
    # TEST
    # mns = MNS()
    # mns.test()

    goldstein(np.array([0, 0, 0]), np.array([1, 0, 0]), 0, 0, 0, 0)


if __name__ == "__main__":
    main()
