import matplotlib.pyplot as plt
import numpy as np
from mns import MNS
from goldstein import goldstein
import sympy as sp
from Equation import Equation
from visualisation import visualisation
from testFunctions import goldstein_price_function


def main():
    visualisation(goldstein_price_function)
    
    #eq = Equation();
    #print(eq.formula)
    #print(eq.variables)

    # nie wiem co zrobilem źle, tutaj przy tauR = 3.5 znajduje wynik po 12 iteracjach, a dla tauR = 3.7 nie znajduje
    goldstein(sp.Matrix([0, 0]), sp.Matrix([1, 0]), 2/5, 3.6, 0.001, 'atan(x1)+x2**2')


if __name__ == "__main__":
    main()
