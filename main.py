from getFormulaString import getFormulaString
from visualisation import visualisation
from goldstein import goldstein
import sympy as sp
from mns import mns
from functionStringParser import function_string_parser


def main():
    formula_string = getFormulaString()
    # goldstein(sp.Matrix([0, 0]), sp.Matrix([1, 0]), 2/5, 1, 0.001, formula_string)
    mns(sp.Matrix([4, 8]), 0.0001, 1000, 1 / 4, 3, formula_string)
    visualisation(function_string_parser(formula_string), 6)


if __name__ == "__main__":
    main()
