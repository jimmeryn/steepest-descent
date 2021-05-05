import matplotlib.pyplot as plt
import numpy as np
from mns import MNS
from goldstein import Goldstein

def main():
    # TEST
    mns = MNS()
    mns.test()
    x = np.linspace(0, 20, 100)
    plt.plot(x, np.sin(x))
    plt.show()
    Goldstein()


if __name__ == "__main__":
    main()
