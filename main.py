from getFormulaString import getFormulaString
from visualisation import visualisation
from goldstein import goldstein
import sympy as sp
from mns import mns
from functionStringParser import function_string_parser
from ui.ui_first_attempt import Ui_MainWindow
from PyQt5 import QtWidgets
def main():
    # formula_string = getFormulaString()
    # mns(sp.Matrix([-1, -1]), 0.0001, 1000, 1 / 4, 3, formula_string)
    # visualisation(function_string_parser(formula_string), 6)
    return 0;

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
