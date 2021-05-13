from getFormulaString import getFormulaString
from visualisation import visualisation
from goldstein import goldstein
import sympy as sp
from mns import mns
from functionStringParser import function_string_parser
from ui.ui import MainWindow
from PyQt5 import QtWidgets as qtw
import sys
from ui.ui_first_attempt import Ui_MainWindow
from PyQt5 import QtWidgets
from ui.gui import MainWindow as GuiWindow


def main():
    a = 2
    if a == 1:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    if a == 2:
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("Fusion")
        window = GuiWindow()
        window.show()
        sys.exit(app.exec_())

    if a == 3:
        app = qtw.QApplication(sys.argv)
        win = MainWindow()
        win.show()
        sys.exit(app.exec_())

    return 0


if __name__ == "__main__":
    main()
