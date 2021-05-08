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
    
    #eq = Equation();
    #print(eq.formula)
    #print(eq.variables)

    # nie wiem co zrobilem źle, tutaj przy tauR = 3.5 znajduje wynik po 12 iteracjach, a dla tauR = 3.7 nie znajduje
    goldstein(sp.Matrix([0, 0]), sp.Matrix([1, 0]), 2/5, 3.6, 0.001, 'atan(x1)+x2**2')


if __name__ == "__main__":
    main()
