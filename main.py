import matplotlib.pyplot as plt
import numpy as np
from mns import MNS
from goldstein import goldstein
import sympy as sp

def main():
    # TEST
    # mns = MNS()
    # mns.test()

    goldstein(sp.Matrix([3, 2, 1]), sp.Matrix([1, 0, 0]), 0, 0, 0, 0)


if __name__ == "__main__":
    main()
