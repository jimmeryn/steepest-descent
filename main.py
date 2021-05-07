import matplotlib.pyplot as plt
import numpy as np
from mns import MNS
from goldstein import goldstein
import sympy as sp
from Equation import Equation


def main():
    # TEST
    # mns = MNS()
    # mns.test()
    
    eq = Equation();
    print(eq.formula)
    print(eq.variables)
    goldstein(sp.Matrix([3, 2, 1]), sp.Matrix([1, -1, 1]), 0, 0.01, 0, 0)


if __name__ == "__main__":
    main()
