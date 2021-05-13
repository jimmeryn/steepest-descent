from getFormulaString import getFormulaString
from visualisation import visualisation
from goldstein import goldstein
import sympy as sp
from mns import mns
from functionStringParser import function_string_parser
from ui.ui import MainWindow
from PyQt5 import QtWidgets as qtw
import sys
def main():
    # formula_string = getFormulaString()
    # mns(sp.Matrix([-1, -1]), 0.0001, 1000, 1 / 4, 3, formula_string)
    # visualisation(function_string_parser(formula_string), 6)
    app = qtw.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
