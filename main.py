import matplotlib.pyplot as plt
import numpy as np
from goldstein import goldstein
import sympy as sp
from testFunctions import modified_himmelblau_function, geem_function, test_function
from mns import mns

def main():
    # TEST
    # mns = MNS()
    # mns.test()
    
    #eq = Equation();
    #print(eq.formula)
    #print(eq.variables)

    # goldstein(sp.Matrix([0, 0]), sp.Matrix([1, 0]), 2/5, 1, 0.001, test_function())
    mns(sp.Matrix([4, 8]), 0.0001, 1000, 1/4, 3, modified_himmelblau_function())

if __name__ == "__main__":
    main()
